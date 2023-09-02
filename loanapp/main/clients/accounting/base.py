from abc import ABC, abstractmethod

class BaseAccountingClient(ABC):
    """ Basic functions every accounting client must implement to work within the application """
    def __init__(self, accessToken):
        self.accessToken = accessToken
    
    @abstractmethod
    def fetch_balance_sheet(self):
        """ Function that returns the balance sheet of the given organization """ 
        ...