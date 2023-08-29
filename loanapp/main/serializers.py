from rest_framework import serializers

class SheetSerializer(serializers.Serializer):
    year = serializers.IntegerField()
    month = serializers.IntegerField()
    profitOrLoss = serializers.IntegerField()
    assetsValue = serializers.IntegerField()

class BusinessDetailsSerializer(serializers.Serializer):
    name = serializers.CharField()
    year = serializers.CharField()
    profitOrLoss = serializers.IntegerField()
    loan_amount = serializers.FloatField()