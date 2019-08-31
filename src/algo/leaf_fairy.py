from algo.fairy import Fairy, FairyType


class LeafFairy(Fairy):
    def __init__(self):
        super(LeafFairy, self).__init__()
        self.unique_type = FairyType.LEAF_TYPE
        self.capability.append(FairyType.LEAF_TYPE)

    def get_unique_type(self):
        return FairyType.LEAF_TYPE
