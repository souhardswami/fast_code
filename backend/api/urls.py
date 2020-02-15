



from django.urls import path
from api import views



urlpatterns = [
    path('api/questionlist', views.QuestionList.as_view()),
    path('api/submitionlist', views.SubmitionList.as_view()),
    path('api/codeexecute', views.CodeExecute.as_view()),
]