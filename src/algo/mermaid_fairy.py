from algo.fairy import Fairy, FairyType


class MermaidFairy(Fairy):
    def __init__(self):
        super(MermaidFairy, self).__init__()

        self.capability.append(FairyType.MERMAID_TYPE)
