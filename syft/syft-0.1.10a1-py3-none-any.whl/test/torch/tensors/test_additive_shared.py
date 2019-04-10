import pytest
import random
import torch
import torch as th
import syft

from syft.frameworks.torch.tensors.interpreters import AdditiveSharingTensor


def test_wrap(workers):
    """
    Test the .on() wrap functionality for AdditiveSharingTensor
    """

    x_tensor = torch.Tensor([1, 2, 3])
    x = AdditiveSharingTensor().on(x_tensor)
    assert isinstance(x, torch.Tensor)
    assert isinstance(x.child, AdditiveSharingTensor)
    assert isinstance(x.child.child, torch.Tensor)


def test_encode_decode(workers):

    t = torch.tensor([1, 2, 3])
    x = t.share(workers["bob"], workers["alice"], workers["james"])

    x = x.get()

    assert (x == t).all()


def test_virtual_get(workers):
    t = torch.tensor([1, 2, 3])
    x = t.share(workers["bob"], workers["alice"], workers["james"])

    x = x.child.virtual_get()

    assert (x == t).all()


def test_send_get(workers):
    bob, alice, james = (workers["bob"], workers["alice"], workers["james"])
    x_sh = th.tensor([[3, 4]]).share(alice, bob, crypto_provider=james)

    alice_t_id = x_sh.child.child["alice"].id_at_location
    assert alice_t_id in alice._objects

    ptr_x = x_sh.send(james)
    ptr_x_id_at_location = ptr_x.id_at_location
    assert ptr_x_id_at_location in james._objects
    assert alice_t_id in alice._objects

    x_sh_back = ptr_x.get()
    assert ptr_x_id_at_location not in james._objects
    assert alice_t_id in alice._objects

    x = x_sh_back.get()
    assert alice_t_id not in alice._objects


def test_add(workers):

    t = torch.tensor([1, 2, 3])
    x = torch.tensor([1, 2, 3]).share(workers["bob"], workers["alice"], workers["james"])

    y = (x + x).get()

    assert (y == (t + t)).all()


def test_sub(workers):

    t = torch.tensor([1, 2, 3])
    x = torch.tensor([1, 2, 3]).share(workers["bob"], workers["alice"], workers["james"])

    y = (x - x).get()

    assert (y == (t - t)).all()


def test_mul(workers):
    bob, alice, james = (workers["bob"], workers["alice"], workers["james"])
    t = torch.tensor([1, 2, 3, 4.0])
    x = t.fix_prec().share(bob, alice, crypto_provider=james)
    y = (x * x).get().float_prec()

    assert (y == (t * t)).all()


def test_mul_with_no_crypto_provider(workers):
    bob, alice = (workers["bob"], workers["alice"])
    x = torch.tensor([1, 2, 3, 4.0]).fix_prec().share(bob, alice)
    with pytest.raises(AttributeError):
        y = (x * x).get().float_prec()


def test_matmul(workers):
    bob, alice, james = (workers["bob"], workers["alice"], workers["james"])

    m = torch.tensor([[1, 2], [3, 4.0]])
    x = m.fix_prec().share(bob, alice, crypto_provider=james)
    y = (x @ x).get().float_prec()

    assert (y == (m @ m)).all()


def test_fixed_precision_and_sharing(workers):

    bob, alice = (workers["bob"], workers["alice"])

    t = torch.tensor([1, 2, 3, 4.0])
    x = t.fix_prec().share(bob, alice)
    out = x.get().float_prec()

    assert (out == t).all()

    x = t.fix_prec().share(bob, alice)

    y = x + x

    y = y.get().float_prec()
    assert (y == (t + t)).all()


def test_get_item(workers):
    alice, bob, james = workers["alice"], workers["bob"], workers["james"]
    x = th.tensor([[3.1, 4.3]]).fix_prec().share(alice, bob, crypto_provider=james)
    idx = torch.tensor([0]).send(alice, bob)

    assert x.child.child[:, idx].get() == torch.tensor([[3100]])

    x = th.tensor([[3, 4]]).share(alice, bob, crypto_provider=james)
    idx = torch.tensor([0]).send(alice, bob)
    assert x[:, idx].get() == torch.tensor([[3]])


def test_eq(workers):
    alice, bob, james = workers["alice"], workers["bob"], workers["james"]

    x = th.tensor([3.1]).fix_prec().share(alice, bob, crypto_provider=james)
    y = th.tensor([3.1]).fix_prec().share(alice, bob, crypto_provider=james)

    assert (x == y).get().float_prec()

    x = th.tensor([3.1]).fix_prec().share(alice, bob, crypto_provider=james)
    y = th.tensor([2.1]).fix_prec().share(alice, bob, crypto_provider=james)

    assert not (x == y).get().float_prec()

    x = th.tensor([-3.1]).fix_prec().share(alice, bob, crypto_provider=james)
    y = th.tensor([-3.1]).fix_prec().share(alice, bob, crypto_provider=james)

    assert (x == y).get().float_prec()


def test_comp(workers):
    alice, bob, james = workers["alice"], workers["bob"], workers["james"]

    x = th.tensor([3.1]).fix_prec().share(alice, bob, crypto_provider=james)
    y = th.tensor([3.1]).fix_prec().share(alice, bob, crypto_provider=james)

    assert (x >= y).get().float_prec()
    assert (x <= y).get().float_prec()
    assert not (x > y).get().float_prec()
    assert not (x < y).get().float_prec()

    x = th.tensor([-3.1]).fix_prec().share(alice, bob, crypto_provider=james)
    y = th.tensor([-3.1]).fix_prec().share(alice, bob, crypto_provider=james)

    assert (x >= y).get().float_prec()
    assert (x <= y).get().float_prec()
    assert not (x > y).get().float_prec()
    assert not (x < y).get().float_prec()

    x = th.tensor([3.1]).fix_prec().share(alice, bob, crypto_provider=james)
    y = th.tensor([2.1]).fix_prec().share(alice, bob, crypto_provider=james)

    assert (x >= y).get().float_prec()
    assert not (x <= y).get().float_prec()
    assert (x > y).get().float_prec()
    assert not (x < y).get().float_prec()

    x = th.tensor([-2.1]).fix_prec().share(alice, bob, crypto_provider=james)
    y = th.tensor([-3.1]).fix_prec().share(alice, bob, crypto_provider=james)

    assert (x >= y).get().float_prec()
    assert not (x <= y).get().float_prec()
    assert (x > y).get().float_prec()
    assert not (x < y).get().float_prec()
