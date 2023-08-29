from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .clients.accounting.xero import XeroClient as Xero
from .clients.decision_engine import DecisionEngineClient

from .services.accounting import AccountingService
from .services.decision_engine import DecisionEngine

from .serializers import SheetSerializer, BusinessDetailsSerializer

@api_view(["GET"])
def balance_sheet(request):
    """Fetches balance sheet for request"""
    accounting_client = Xero()
    service = AccountingService(client=accounting_client)
    try:
        sheet = service.fetch_balance_sheet()
    except Exception as exp: # Would be a kind of api error
        return Response(exp, status=status.HTTP_503_SERVICE_UNAVAILABLE)
    else:
        serializer = SheetSerializer(sheet)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    

@api_view(["POST"])
def get_outcome(request):
    """ Returns the outcome of whether a loan was approved """ 
    serializer = BusinessDetailsSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    client = DecisionEngineClient()
    service = DecisionEngine(client=client)
    try:
        service.submit_for_decision(serializer.validated_data)
    except Exception as exp: # Normally will be a specific error or multiple errors
        return Response(exp, status=status.HTTP_503_SERVICE_UNAVAILABLE)
    return Response(status=status.HTTP_201_CREATED)
