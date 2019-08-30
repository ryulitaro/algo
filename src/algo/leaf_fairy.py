from algo.fairy import Fairy, FairyType


class LeafFairy(Fairy):
    def __init__(self):
        super(LeafFairy, self).__init__()

        self.capability.append(FairyType.LEAF_TYPE)
