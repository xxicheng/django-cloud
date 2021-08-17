from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('project_status', 'project_country', 'year', 'month','project_name', 'project_number', 'company', 'sector',
                  'bank', 'url', 'loan_amount', 'currency', 'loan_amount_in_usd')

