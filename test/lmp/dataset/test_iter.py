r"""Test `lmp.dataset.BaseDataset.__iter__`.

Usage:
    python -m unittest test.lmp.dataset.test_iter
"""

# built-in modules

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import inspect
import unittest

from typing import Iterable
from typing import Generator

# self-made modules

from lmp.dataset import BaseDataset


class TestIter(unittest.TestCase):
    r"""Test case for `lmp.dataset.BaseDataset.__iter__`."""

    def test_signature(self):
        r"""Ensure signature consistency."""
        msg = 'Inconsistenct method signature.'

        self.assertEqual(
            inspect.signature(BaseDataset.__iter__),
            inspect.Signature(
                parameters=[
                    inspect.Parameter(
                        name='self',
                        kind=inspect.Parameter.POSITIONAL_OR_KEYWORD,
                        default=inspect.Parameter.empty
                    ),
                ],
                return_annotation=Generator[str, None, None]
            ),
            msg=msg
        )

    def test_yield_value(self):
        r"""Is an iterable which yield sequences in order."""
        msg = 'Must be an iterable which yield sequences in order.'
        examples = (
            [
                'Hello',
                'World',
                'Hello World',
            ],
            [
                'Mario use Kimura Lock on Luigi, and Luigi tap out.',
                'Mario use Superman Punch.',
                'Luigi get TKO.',
                'Toad and Toadette are fightting over mushroom (weed).',
            ],
            [''],
            [],
        )

        for batch_sequences in examples:
            dataset = BaseDataset(batch_sequences=batch_sequences)
            self.assertIsInstance(dataset, Iterable, msg=msg)

            for ans_sequence, sequence in zip(batch_sequences, dataset):
                self.assertIsInstance(sequence, str, msg=msg)
                self.assertEqual(sequence, ans_sequence, msg=msg)


if __name__ == '__main__':
    unittest.main()
