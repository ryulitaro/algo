from enum import Enum


class FairyType(Enum):
    COMMON = 'turns into'
    LEAF_TYPE = 'controls plants:'
    MERMAID_TYPE = 'controls sea plants:'


class Fairy:
    def __init__(self):
        self.capability = [FairyType.COMMON]

    def do_magic(self, target):
        for item in self.capability:
            print(f'{item.value} {target}')
