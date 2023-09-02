class DecisionEngine:
    """ Service layer to link operation between db and clients """
    def __init__(self, client):
        self.client = client
    
    def _preprocess_before_submit(self, data):
        """ Handle any additional rules """
        preAssesment = 30
        if data["balance_sheet"][-1]["profitOrLoss"] > 0:
            preAssesment = 60
        if data["balance_sheet"][-1]["assetsValue"] > data["loan_amount"]:
            preAssesment = 100
        data.update({
            "preAssessment": preAssesment
        })
        return data
    
    def submit_for_decision(self, data):
        data = self._preprocess_before_submit(data)
        self.client.submit_application(data)
