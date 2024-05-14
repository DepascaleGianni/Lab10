from dataclasses import dataclass
from model.country import Country


@dataclass
class Connection:
    dyad : int
    state1no : int
    state1ab : str
    state2no : int
    state2ab : str
    year : int
    conttype : int
    version : float

    #relazioni
    state1 : Country = None
    state2 : Country = None

    def __hash__(self):
        return hash(self.state1no,self.state2no)

    def __str__(self):
        return f'contiguity between {self.state1ab} and {self.state2ab}'
