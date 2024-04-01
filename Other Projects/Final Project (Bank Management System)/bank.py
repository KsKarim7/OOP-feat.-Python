from abc import ABC, abstractmethod
import math

class Bank(ABC):
    balance = 1000000000000000000000000000
    loans = 0
    if_loan = True
    def __init__(self,name,email,address) -> None:
        self.name = name
        self.email = email
        self.address = address