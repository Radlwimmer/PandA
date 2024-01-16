from CLASS_Document import Document


class Query(Document):
    def __init__(self, query: str):
        super().__init__([query])
