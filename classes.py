from typing import List,Dict,Any

class Response_Recipe:
    def __init__(self) -> None:
        self.Recipe: List[Dict[str,str]] = []
        self.Grocery: Dict[str,Any] = []