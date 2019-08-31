from fairy import Fairy, FairyType


class MermaidFairy(Fairy):
    def __init__(self):
        super(MermaidFairy, self).__init__()
        self.unique_type = FairyType.MERMAID_TYPE
        self.capability.append(self.unique_type)

    def get_unique_type(self):
        return self.unique_type
