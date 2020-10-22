from rest_framework import serializers
from .models import *


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee_details
        fields = '__all__'