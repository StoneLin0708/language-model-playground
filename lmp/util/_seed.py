r"""Helper function for setting random seed.

Usage:
    import lmp.util

    lmp.set_seed(...)
    lmp.set_seed_by_config(...)
"""

# built-in modules

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import random

# 3rd-party modules

import numpy as np
import torch

# self-made modules

import lmp.config


def set_seed(seed: int) -> None:
    r"""Helper function for setting random seed.

    Args:
        seed:
            Control random seed and let experiment reproducible. Must be bigger
            than or equal to `1`.

    Raises:
        TypeError:
            When `seed` is not an instance of `int`.
        ValueError:
            When `seed < 1`.
    """
    # Type check.
    if not isinstance(seed, int):
        raise TypeError('`seed` must be an instance of `int`.')

    # Value check.
    if seed < 1:
        raise ValueError('`seed` must be bigger than or equal to `1`.')

    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)

    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False


def set_seed_by_config(config: lmp.config.BaseConfig) -> None:
    r"""Helper function for setting random seed.

    Args:
        config:
            Configuration object with attribute `seed`.

    Raises:
        TypeError:
            When `config` is not an instance of `lmp.config.BaseConfig`.
    """
    # Type check.
    if not isinstance(config, lmp.config.BaseConfig):
        raise TypeError(
            '`config` must be an instance of `lmp.config.BaseConfig`.'
        )

    set_seed(config.seed)
