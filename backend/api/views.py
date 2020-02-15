from django.shortcuts import render

# Create your views here.


from api.models import Question
from api.serializers import QuestionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class QuestionList(APIView):
    
    

    
    def get(self, request, format=None):
        question = Question.objects.all()
        serializer = QuestionSerializer(question, many=True)
        return Response(serializer.data)
    

class SubmitionList(APIView):
    
    
 
    
    def post(self,request,format=None):
        
        answer=request.data['answer']
        number=request.data['number']
        
        value=Question.objects.filter(id=number)
        correct_output=value[0].test_output
        
        if(answer==correct_output):
            return Response(data="Accepted",status=status.HTTP_200_OK) 
        else:
            return Response(data="wrong",status=status.HTTP_200_OK) 

        # return 
    

class CodeExecute(APIView):

    
    def post(self,request,format=None):
        
        from .codexecution import execute
        
        code=request.data['code']
        language=request.data['language']
        stdin=request.data['stdin']
        


        obj=execute(code,language,stdin)
        result=obj.run()

        return Response(data=result)


