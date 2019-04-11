# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from typing import Iterator, Optional, List, Union
import numpy as np
from .. import optimization
from ..optimization import optimizerlib
from ..functions import ArtificialFunction
from .xpbase import registry
from .xpbase import create_seed_generator
from .xpbase import Experiment
# pylint: disable=stop-iteration-return, too-many-nested-blocks


@registry.register
def basic(seed: Optional[int] = None) -> Iterator[Experiment]:
    """Test settings
    """
    seedg = create_seed_generator(seed)
    function = ArtificialFunction(name="sphere", block_dimension=2, noise_level=1)
    np.random.seed(seed)  # seed before initializing the function!
    # initialization uses randomness
    function.transform_var._initialize()
    return iter([Experiment(function, optimizer="OnePlusOne", num_workers=2, budget=4, seed=next(seedg))])


@registry.register
def repeated_basic(seed: Optional[int] = None) -> Iterator[Experiment]:
    """Test settings
    """
    seedg = create_seed_generator(seed)
    function = ArtificialFunction(name="sphere", block_dimension=2, noise_level=1)
    optims: List[Union[str, optimizerlib.base.OptimizerFamily]] = ["OnePlusOne", optimizerlib.DifferentialEvolution()]
    for _ in range(5):
        for optim in optims:
            yield Experiment(function.duplicate(), optimizer=optim, num_workers=2, budget=4, seed=next(seedg))


@registry.register
def small_discrete(seed: Optional[int] = None) -> Iterator[Experiment]:
    # prepare list of parameters to sweep for independent variables
    seedg = create_seed_generator(seed)
    names = ["hardonemax5", "hardjump5", "hardleadingones5"]
    optims = sorted(x for x, y in optimization.registry.items() if "iscrete" in x and "epea" not in x and "DE" not in x
                    and "SSNEA" not in x)
    functions = [ArtificialFunction(name, block_dimension=bd, num_blocks=n_blocks, useless_variables=bd * uv_factor * n_blocks)
                 for name in names for bd in [30] for uv_factor in [5, 10] for n_blocks in [1]]
    # functions are not initialized and duplicated at yield time, they will be initialized in the experiment (no need to seed here)
    for func in functions:
        for optim in optims:
            for budget in [100, 400, 700, 1000, 1300, 1600, 1900, 2200, 2500, 2800, 3000]:  # , 10000]:
                yield Experiment(func.duplicate(), optim, budget=budget, num_workers=1, seed=next(seedg))


@registry.register
def illcond(seed: Optional[int] = None) -> Iterator[Experiment]:
    """All optimizers on ill cond problems
    """
    seedg = create_seed_generator(seed)
    for budget in [500, 1000, 2000, 4000]:
        for optim in ["SQP", "DE", "CMA", "PSO", "RotationInvariantDE", "NelderMead"]:
            for rotation in [True, False]:
                for name in ["ellipsoid", "cigar"]:
                    function = ArtificialFunction(name=name, rotation=rotation, block_dimension=100)
                    yield Experiment(function, optim, budget=budget, seed=next(seedg))


@registry.register
def compabasedillcond(seed: Optional[int] = None) -> Iterator[Experiment]:
    """All optimizers on ill cond problems
    """
    seedg = create_seed_generator(seed)
    for budget in [500, 1000, 2000, 4000, 8000]:
        for optim in ["DE", "CMA", "PSO", "BPRotationInvariantDE", "RotationInvariantDE",
                      "AlmostRotationInvariantDE", "AlmostRotationInvariantDEAndBigPop"]:
            for rotation in [True, False]:
                for name in ["ellipsoid", "cigar"]:
                    function = ArtificialFunction(name=name, rotation=rotation, block_dimension=30)
                    yield Experiment(function, optim, budget=budget, seed=next(seedg))


@registry.register
def noise(seed: Optional[int] = None) -> Iterator[Experiment]:
    """All optimizers on ill cond problems
    """
    seedg = create_seed_generator(seed)
    optims = sorted(x for x, y in optimization.registry.items()
                    if ("TBPSA" in x or "ois" in x or "CMA" in x or "epea" in x) and "iscr" not in x)
    for budget in [500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 128000]:
        for optim in optims:
            for rotation in [True, False]:
                for name in ["sphere", "cigar", "sphere4"]:
                    function = ArtificialFunction(name=name, rotation=rotation, block_dimension=20, noise_level=10)
                    yield Experiment(function, optim, budget=budget, seed=next(seedg))


@registry.register
def dim10_smallbudget(seed: Optional[int] = None) -> Iterator[Experiment]:
    # prepare list of parameters to sweep for independent variables
    seedg = create_seed_generator(seed)
    names = ["sphere"]
    optims = sorted(x for x, y in optimization.registry.items() if y.one_shot and "arg" not in x and "mal" not in x)
    functions = [ArtificialFunction(name, block_dimension=bd, num_blocks=n_blocks, useless_variables=bd * uv_factor * n_blocks)
                 for name in names for bd in [10] for uv_factor in [0] for n_blocks in [1]]
    # functions are not initialized and duplicated at yield time, they will be initialized in the experiment (no need to seed here)
    for func in functions:
        for optim in optims:
            for budget in [4, 8, 16, 32]:
                # duplicate -> each Experiment has different randomness
                yield Experiment(func.duplicate(), optim, budget=budget, num_workers=1, seed=next(seedg))


@registry.register
def dim10_select_two_features(seed: Optional[int] = None) -> Iterator[Experiment]:     # 2 variables matter - Scrambled Hammersley rules.
    # prepare list of parameters to sweep for independent variables
    seedg = create_seed_generator(seed)
    names = ["sphere"]
    optims = sorted(x for x, y in optimization.registry.items() if y.one_shot and "arg" not in x and "mal" not in x)
    functions = [ArtificialFunction(name, block_dimension=bd, num_blocks=n_blocks, useless_variables=bd * uv_factor * n_blocks)
                 for name in names for bd in [2] for uv_factor in [5] for n_blocks in [1]]
    # functions are not initialized and duplicated at yield time, they will be initialized in the experiment (no need to seed here)
    for func in functions:
        for optim in optims:
            for budget in [4, 8, 16, 32]:
                # duplicate -> each Experiment has different randomness
                yield Experiment(func.duplicate(), optim, budget=budget, num_workers=1, seed=next(seedg))


@registry.register
def dim10_select_one_feature(seed: Optional[int] = None) -> Iterator[Experiment]:    # One and only one variable matters - LHS wins.
    # prepare list of parameters to sweep for independent variables
    seedg = create_seed_generator(seed)
    names = ["sphere"]
    optims = sorted(x for x, y in optimization.registry.items() if y.one_shot and "arg" not in x and "mal" not in x)
    functions = [ArtificialFunction(name, block_dimension=bd, num_blocks=n_blocks, useless_variables=bd * uv_factor * n_blocks)
                 for name in names for bd in [1] for uv_factor in [10] for n_blocks in [1]]
    # functions are not initialized and duplicated at yield time, they will be initialized in the experiment (no need to seed here)
    for func in functions:
        for optim in optims:
            for budget in [8, 10, 12, 14, 16, 18, 20]:
                # duplicate -> each Experiment has different randomness
                yield Experiment(func.duplicate(), optim, budget=budget, num_workers=1, seed=next(seedg))


@registry.register
def doe_dim4(seed: Optional[int] = None) -> Iterator[Experiment]:  # Here, QR performs best, then Random, then LHS, then Cauchy.
    # prepare list of parameters to sweep for independent variables
    seedg = create_seed_generator(seed)
    names = ["sphere"]  # n for n in ArtificialFunction.list_sorted_function_names() if "sphere" in n]
    optims = sorted(x for x, y in optimization.registry.items() if y.one_shot and "arg" not in x and "mal" not in x)
    functions = [ArtificialFunction(name, block_dimension=bd, num_blocks=n_blocks, useless_variables=bd * uv_factor * n_blocks)
                 for name in names for bd in [4] for uv_factor in [0] for n_blocks in [1]]
    # functions are not initialized and duplicated at yield time, they will be initialized in the experiment (no need to seed here)
    for func in functions:
        for optim in optims:
            for budget in [30, 100, 3000, 10000]:
                # duplicate -> each Experiment has different randomness
                yield Experiment(func.duplicate(), optim, budget=budget, num_workers=1, seed=next(seedg))


@registry.register
def oneshot4(seed: Optional[int] = None) -> Iterator[Experiment]:
    # General experiment comparing one-shot optimizers, excluding those with "large" or "small"
    # in the name.
    seedg = create_seed_generator(seed)
    names = ["sphere", "cigar", "ellipsoid", "rosenbrock", "rastrigin"]
    optims = sorted(x for x, y in optimization.registry.items() if y.one_shot and "arg" not in x and "mal" not in x)
    functions = [ArtificialFunction(name, block_dimension=bd, num_blocks=n_blocks, useless_variables=bd * uv_factor * n_blocks)
                 for name in names for bd in [1, 4, 20] for uv_factor in [0, 10] for n_blocks in [1]]
    # functions are not initialized and duplicated at yield time, they will be initialized in the experiment
    for func in functions:
        for optim in optims:
            for budget in [30, 100, 3000]:
                # duplicate -> each Experiment has different randomness
                yield Experiment(func.duplicate(), optim, budget=budget, num_workers=1, seed=next(seedg))


@registry.register
def oneshot3(seed: Optional[int] = None) -> Iterator[Experiment]:
    # General experiment comparing one-shot optimizers, excluding those with "large" or "small"
    # in the name.
    seedg = create_seed_generator(seed)
    names = ["sphere", "altcigar", "cigar", "ellipsoid", "rosenbrock", "rastrigin", "altellipsoid"]
    optims = sorted(x for x, y in optimization.registry.items() if y.one_shot and "arg" not in x and "mal" not in x)
    functions = [ArtificialFunction(name, block_dimension=bd) for name in names for bd in [4, 20]]
    # functions are not initialized and duplicated at yield time, they will be initialized in the experiment
    for func in functions:
        for optim in optims:
            for budget in [30, 60, 100]:
                # duplicate -> each Experiment has different randomness
                yield Experiment(func.duplicate(), optim, budget=budget, num_workers=1, seed=next(seedg))


@registry.register
def oneshot2(seed: Optional[int] = None) -> Iterator[Experiment]:
    # Experiment comparing one-shot optimizers in the context of useless vars vs critical vars.
    seedg = create_seed_generator(seed)
    names = ["sphere", "altcigar", "cigar", "ellipsoid", "rosenbrock", "rastrigin", "altellipsoid"]
    optims = sorted(x for x, y in optimization.registry.items() if y.one_shot and "arg" not in x and "mal" not in x)
    functions = [ArtificialFunction(name, block_dimension=2, num_blocks=1, useless_variables=20) for name in names]
    # functions are not initialized and duplicated at yield time, they will be initialized in the experiment
    for func in functions:
        for optim in optims:
            for budget in [30, 60, 100]:
                # duplicate -> each Experiment has different randomness
                yield Experiment(func.duplicate(), optim, budget=budget, num_workers=1, seed=next(seedg))


@registry.register
def oneshot1(seed: Optional[int] = None) -> Iterator[Experiment]:
    """Comparing one-shot optimizers as initializers for Bayesian Optimization.
    """
    seedg = create_seed_generator(seed)
    for budget in [25, 31, 37, 43, 50, 60]:  # , 4000, 8000, 16000, 32000]:
        for optim in sorted(x for x, y in optimization.registry.items() if "BO" in x):
            for rotation in [False]:
                for d in [20]:
                    for name in ["sphere", "cigar", "hm", "ellipsoid"]:  # , "hm"]:
                        for u in [0]:
                            function = ArtificialFunction(name=name, rotation=rotation, block_dimension=d,
                                                          useless_variables=d*u, translation_factor=1.)
                            yield Experiment(function, optim, budget=budget, seed=next(seedg))


@registry.register
def metanoise(seed: Optional[int] = None) -> Iterator[Experiment]:
    seedg = create_seed_generator(seed)
    optims = ["NoisyBandit", "TBPSA", "NaiveTBPSA"]
    for budget in [15, 31, 62, 125, 250, 500, 1000, 2000, 4000, 8000]:
        for optim in optims:
            for noise_dissymmetry in [False, True]:
                function = ArtificialFunction(name="sphere", rotation=True, block_dimension=1, noise_level=10,
                                              noise_dissymmetry=noise_dissymmetry, translation_factor=10.)
                yield Experiment(function, optim, budget=budget, seed=next(seedg))
