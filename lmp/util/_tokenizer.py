r"""Helper function for loading tokenizer.

Usage:
    import lmp.util

    tokenizer = lmp.util.load_tokenizer(...)
    tokenizer = lmp.util.load_tokenizer_by_config(...)
"""

# built-in modules

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

# self-made modules

import lmp.tokenizer
import lmp.config


def load_tokenizer(
        checkpoint: int,
        experiment: str,
        is_uncased: bool,
        tokenizer_class: str
) -> lmp.tokenizer.BaseTokenizer:
    r"""Helper function for constructing tokenizer.

    Supported options:
        --tokenizer_class char_dict
        --tokenizer_class char_list
        --tokenizer_class whitespace_dict
        --tokenizer_class whitespace_list

    Load pre-trained tokenizer when `checkpoint != -1`.

    Args:
        checkpoint:
            Whether to load pre-trained tokenizer. Must be bigger than or equal
            to `-1`.
        experiment:
            Name of the pre-trained experiment. Must not be empty when
            `checkpoint != -1`.
        is_uncased:
            Whether to convert upper cases to lower cases.
        tokenizer_class:
            Which tokenizer class to construct.

    Raises:
        TypeError:
            When one of the arguments are not an instance of their type
            annotation respectively.
        ValueError:
            When one of the arguments do not follow their constraints. See
            docstring for arguments constraints.

    Returns:
        `CharDictTokenizer` if `tokenizer_class == 'char_dict'`.
        `CharListTokenizer` if `tokenizer_class == 'char_list'`.
        `WhitespaceDictTokenizer` if `tokenizer_class == 'whitespace_dict'`.
        `WhitespaceListTokenizer` if `tokenizer_class == 'whitespace_list'`.
    """
    # Type check.
    if not isinstance(checkpoint, int):
        raise TypeError('`checkpoint` must be an instance of `int`.')

    if not isinstance(experiment, str):
        raise TypeError('`experiment` must be an instance of `str`.')

    if not isinstance(is_uncased, bool):
        raise TypeError('`is_uncased` must be an instance of `bool`.')

    if not isinstance(tokenizer_class, str):
        raise TypeError('`tokenizer_class` must be an instance of `str`.')

    # Value Check.
    if checkpoint < -1:
        raise ValueError('`checkpoint` must be bigger than or equal to `-1`.')

    if tokenizer_class == 'char_dict':
        tokenizer = lmp.tokenizer.CharDictTokenizer(is_uncased=is_uncased)

    elif tokenizer_class == 'char_list':
        tokenizer = lmp.tokenizer.CharListTokenizer(is_uncased=is_uncased)

    elif tokenizer_class == 'whitespace_dict':
        tokenizer = lmp.tokenizer.WhitespaceDictTokenizer(
            is_uncased=is_uncased
        )

    elif tokenizer_class == 'whitespace_list':
        tokenizer = lmp.tokenizer.WhitespaceListTokenizer(
            is_uncased=is_uncased
        )

    else:
        raise ValueError(
            f'tokenizer `{tokenizer_class}` does not support.\n' +
            'Supported options:' +
            ''.join(list(map(
                lambda option: f'\n\t--tokenizer_class {option}',
                [
                    'char_dict',
                    'char_list',
                    'whitespace_dict',
                    'whitespace_list',
                ]
            )))
        )

    if checkpoint > 0:
        tokenizer = tokenizer.load(experiment=experiment)

    return tokenizer


def load_tokenizer_by_config(
        checkpoint: int,
        config: lmp.config.BaseConfig
) -> lmp.tokenizer.BaseTokenizer:
    r"""Helper function for constructing tokenizer.

    Load pre-trained tokenizer when `checkpoint != -1`.

    Args:
        checkpoint:
            Whether to load pre-trained tokenizer. Must be bigger than or equal
            to `-1`.
        config:
            Configuration object with attributes `is_uncased`,
            `experiment` and `tokenizer_class`.

    Raises:
        TypeError:
            When one of the arguments are not an instance of their type
            annotation respectively.
        ValueError:
            When `checkpoint < -1`.

    Returns:
        Same as `load_tokenizer`.
    """
    # Type check.
    if not isinstance(config, lmp.config.BaseConfig):
        raise TypeError(
            '`config` must be an instance of `lmp.config.BaseConfig`.'
        )

    return load_tokenizer(
        checkpoint=checkpoint,
        experiment=config.experiment,
        is_uncased=config.is_uncased,
        tokenizer_class=config.tokenizer_class
    )
