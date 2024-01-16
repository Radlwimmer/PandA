# Index takes a list of documents (sonnets) and saves the single tokens (no duplicates!)
# with the indexes (again no duplicates!) of all the sonnets they can be found in

from CLASS_Sonnet import Sonnet
from CLASS_Query import Query


class Index(dict[str, set[int]]):
    # str = key for dictionary, in my case the token; set[int] has the IDs of the sonnets
    def __init__(self, documents: list[Sonnet]):
        super().__init__()

        self.documents = documents

        for document in documents:
            self.add(document)

    def add(self, document: Sonnet):
        tokens = document.tokenize()  # use tokenize from Document class on the document
        for token in tokens:  # go through all the tokens in the document
            if token not in self:  # create a new key if the token is new
                self[token] = set()
            self[token].add(document.id)  # add the id of the document where the token can be found in

    def search(self, query: Query) -> list[Sonnet]:
        tokens = query.tokenize()
        intersect_ids = []
        for token in tokens:
            if token not in self:  # check if token in sonnets
                print(f"-{token}- could not be found in any sonnet.")
                return []
            else:
                if not intersect_ids:  # if list empty fill with tokens
                    intersect_ids = self[token]
                else:
                    intersect_ids = set(intersect_ids).intersection(self[token])  # only save ids in both lists
        matching_sonnets = []
        for document in self.documents:
            if document.id in intersect_ids:  # select sonnets from intersection
                matching_sonnets.append(document)
        return matching_sonnets
