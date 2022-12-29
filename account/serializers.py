from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from .models import Account


class AccountSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Account
        fields = "__all__"
