from rest_framework import serializers

class ProviderSerializer(serializers.Serializer):
    provider = serializers.CharField()
    accessToken = serializers.CharField()

class SheetSerializer(serializers.Serializer):
    year = serializers.IntegerField()
    month = serializers.IntegerField()
    profitOrLoss = serializers.IntegerField()
    assetsValue = serializers.IntegerField()

class BusinessDetailsSerializer(serializers.Serializer):
    name = serializers.CharField()
    year = serializers.CharField()
    balance_sheet = SheetSerializer(many=True)
    loan_amount = serializers.FloatField()