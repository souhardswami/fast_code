from api.models import Question
from rest_framework import serializers



class QuestionSerializer(serializers.ModelSerializer):


    class Meta:
        model = Question
        fields = ['id','title', 'code','statement','test_input']

