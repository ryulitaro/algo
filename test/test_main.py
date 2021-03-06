import unittest
from unittest.mock import Mock

from fairy import FairyType, MagicType
from leaf_fairy import LeafFairy
import click

class TestFairy(unittest.TestCase):
    def test_magic_type(self):
        leaf_fairy = LeafFairy()
        magic_type = leaf_fairy.get_magic_type_list()
        self.assertTrue(MagicType.POWDER in magic_type)
        leaf_fairy.capability = Mock(
            return_value=[FairyType.LEAF_TYPE, FairyType.COMMON]
        )
        self.assertEqual(leaf_fairy.get_unique_type(), FairyType.LEAF_TYPE)


if __name__ == "__main__":
    unittest.main()
