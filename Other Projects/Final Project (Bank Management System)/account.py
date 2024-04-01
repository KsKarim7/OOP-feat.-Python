from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self,name,email,address) -> None:
        self.name = name
        self.email = email
        self.address = address