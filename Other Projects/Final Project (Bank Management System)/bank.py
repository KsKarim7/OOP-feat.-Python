from abc import ABC, abstractmethod
import math

class Bank(ABC):
    balance = math.inf
    loans = 0
    if_loan = True
    def __init__(self,name,email,address) -> None:
        self.name = name
        self.email = email
        self.address = address