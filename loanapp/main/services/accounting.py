class AccountingService:
    """ A Service Layer for linking client layer to db layer """
    def __init__(self, client):
        self.client = client
    
    def fetch_balance_sheet(self) -> list[dict[str, str]]:
        return self.client.fetch_balance_sheet()