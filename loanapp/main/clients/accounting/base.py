from collections.abc import abstractmethod

class BaseAccountingClient:
    """ Basic functions every accounting client must implement to work within the application """
    @abstractmethod
    def fetch_balance_sheet(self):
        """ Function that returns the balance sheet of the given organization """ 
        ...