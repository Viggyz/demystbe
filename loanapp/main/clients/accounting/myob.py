from .base import BaseAccountingClient

class MYOBClient(BaseAccountingClient):
    """ Client that implements a MYOB SDK to communicate with API """
    
    def fetch_balance_sheet(self):
        ...
        