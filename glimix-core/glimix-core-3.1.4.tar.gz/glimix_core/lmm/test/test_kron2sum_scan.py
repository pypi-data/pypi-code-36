import scipy.stats as st
from numpy import concatenate, empty, kron
from numpy.random import RandomState
from numpy.testing import assert_allclose
from numpy_sugar.linalg import economic_qs

from brent_search import minimize
from glimix_core._util import assert_interface, vec
from glimix_core.lmm import Kron2Sum, KronFastScanner, FastScanner


def test_lmm_kron_scan():
    random = RandomState(0)
    n = 5
    Y = random.randn(n, 3)
    A = random.randn(3, 3)
    A = A @ A.T
    F = random.randn(n, 2)
    G = random.randn(n, 6)
    lmm = Kron2Sum(Y, A, F, G, restricted=True)
    lmm.fit(verbose=False)
    scan = lmm.get_fast_scanner()

    m = lmm.mean()
    K = lmm.covariance()

    def func(scale):
        mv = st.multivariate_normal(m, scale * K)
        return -mv.logpdf(vec(Y))

    s = minimize(func, 1e-3, 5.0, 1e-5)[0]

    assert_allclose(scan.null_lml(), st.multivariate_normal(m, s * K).logpdf(vec(Y)))
    assert_allclose(kron(A, F) @ scan.null_beta, m)

    A1 = random.randn(3, 2)
    F1 = random.randn(n, 4)

    r = scan.scan(A1, F1)
    assert_allclose(r["scale"], 0.3000748879939645, rtol=1e-3)

    m = kron(A, F) @ vec(r["effsizes0"]) + kron(A1, F1) @ vec(r["effsizes1"])

    def func(scale):
        mv = st.multivariate_normal(m, scale * K)
        return -mv.logpdf(vec(Y))

    s = minimize(func, 1e-3, 5.0, 1e-5)[0]

    assert_allclose(r["lml"], st.multivariate_normal(m, s * K).logpdf(vec(Y)))

    r = scan.scan(empty((3, 0)), F1)
    assert_allclose(r["lml"], -10.96414417860732, rtol=1e-4)
    assert_allclose(r["scale"], 0.5999931720566452, rtol=1e-3)
    assert_allclose(
        r["effsizes0"],
        [
            [1.411082677273241, 0.41436234081257045, -1.5337251391408189],
            [-0.6753042112998789, -0.20299590400182352, 0.6723874047807074],
        ],
        rtol=1e-2,
        atol=1e-2,
    )
    assert_allclose(r["effsizes1"], [])


def test_lmm_kron_scan_with_lmm():
    random = RandomState(0)
    n = 5
    Y = random.randn(n, 3)
    A = random.randn(3, 3)
    A = A @ A.T
    F = random.randn(n, 2)
    G = random.randn(n, 6)

    klmm = Kron2Sum(Y, A, F, G, restricted=True)
    klmm.fit(verbose=False)
    kscan = klmm.get_fast_scanner()

    K = klmm.covariance()

    X = kron(A, F)
    QS = economic_qs(K)
    scan = FastScanner(vec(Y), X, QS, 0.0)

    assert_allclose(klmm.covariance(), K)
    assert_allclose(kscan.null_scale, scan.null_scale)
    assert_allclose(kscan.null_beta, scan.null_beta)
    assert_allclose(kscan.null_lml(), scan.null_lml())
    assert_allclose(kscan.null_beta_covariance, scan.null_beta_covariance)

    A1 = random.randn(3, 2)
    F1 = random.randn(n, 2)
    M = kron(A1, F1)

    kr = kscan.scan(A1, F1)
    r = scan.scan(M)
    assert_allclose(kr["lml"], r["lml"])
    assert_allclose(kr["scale"], r["scale"])
    assert_allclose(vec(kr["effsizes0"]), r["effsizes0"])
    assert_allclose(vec(kr["effsizes1"]), r["effsizes1"])
    assert_allclose(vec(kr["effsizes0_se"]), r["effsizes0_se"])
    assert_allclose(vec(kr["effsizes1_se"]), r["effsizes1_se"])


def test_lmm_kron_scan_unrestricted():
    random = RandomState(0)
    n = 5
    Y = random.randn(n, 3)
    A = random.randn(3, 3)
    A = A @ A.T
    F = random.randn(n, 2)
    G = random.randn(n, 6)
    lmm = Kron2Sum(Y, A, F, G, restricted=False)
    lmm.fit(verbose=False)
    scan = lmm.get_fast_scanner()

    assert_allclose(scan.null_scale, 1.0, rtol=1e-3)
    assert_allclose(lmm.beta_covariance, scan.null_beta_covariance, rtol=1e-3)


def test_lmm_kron_scan_redundant():
    random = RandomState(0)
    n = 5
    Y = random.randn(n, 3)
    A = random.randn(3, 3)
    A = A @ A.T
    F = random.randn(n, 2)
    G = random.randn(n, 6)
    G = concatenate([G, G], axis=1)
    lmm = Kron2Sum(Y, A, F, G, restricted=True)
    lmm.fit(verbose=False)
    scan = lmm.get_fast_scanner()

    m = lmm.mean()
    K = lmm.covariance()

    def func(scale):
        mv = st.multivariate_normal(m, scale * K)
        return -mv.logpdf(vec(Y))

    s = minimize(func, 1e-3, 5.0, 1e-5)[0]

    assert_allclose(scan.null_lml(), st.multivariate_normal(m, s * K).logpdf(vec(Y)))
    assert_allclose(kron(A, F) @ scan.null_beta, m)

    A1 = random.randn(3, 2)
    F1 = random.randn(n, 4)
    F1 = concatenate([F1, F1], axis=1)

    r = scan.scan(A1, F1)
    assert_allclose(r["scale"], 0.3005376956901813, rtol=1e-3)

    m = kron(A, F) @ vec(r["effsizes0"]) + kron(A1, F1) @ vec(r["effsizes1"])

    def func(scale):
        mv = st.multivariate_normal(m, scale * K)
        return -mv.logpdf(vec(Y))

    s = minimize(func, 1e-3, 5.0, 1e-5)[0]

    assert_allclose(r["lml"], st.multivariate_normal(m, s * K).logpdf(vec(Y)))


def test_lmm_kron_scan_public_attrs():
    assert_interface(
        KronFastScanner,
        ["null_lml", "scan"],
        ["null_beta", "null_beta_covariance", "null_beta_se", "null_scale"],
    )
