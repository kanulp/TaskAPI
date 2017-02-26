from rest_framework import serializers
from .models import Task
class TestSerializers(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields = ('id','task_name','task_desc')