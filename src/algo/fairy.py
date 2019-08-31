from enum import Enum


class FairyType(Enum):
    COMMON = "turns into"
    LEAF_TYPE = "controls plants:"
    MERMAID_TYPE = "controls sea plants:"


class MagicType(Enum):
    POWDER = "powder"
    PERFUME = "perfume"
    WAND = "magic wand"
    BLACK_CAT = "black cat"
    BOOK = "book"


magic_map = {
    FairyType.COMMON: [MagicType.WAND],
    FairyType.LEAF_TYPE: [MagicType.POWDER, MagicType.BOOK],
    FairyType.MERMAID_TYPE: [MagicType.PERFUME, MagicType.BLACK_CAT],
}


class Fairy:
    def __init__(self):
        self.capability = [FairyType.COMMON]

    def do_magic(self, target):
        for item in self.capability:
            print(f"{item.value} a {target}")

    def get_unique_type(self):
        pass

    def get_magic_type_list(self):
        magic_list = list()
        for item in self.capability:
            magic_list = magic_list + magic_map[item]
        return magic_list
