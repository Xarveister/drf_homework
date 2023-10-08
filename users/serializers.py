from rest_framework import serializers

from main.models import Payment
from main.serializers import PaymentForOwnerSerializer
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    payments = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = '__all__'

    def get_payments(self, owner):
        if self.context['request'].user != owner:
            return None
        return PaymentForOwnerSerializer(Payment.objects.filter(owner=owner), many=True).data


class PublicUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'role']
