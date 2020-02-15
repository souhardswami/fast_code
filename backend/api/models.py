
from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=20, blank=True, default='')
    code = models.CharField(max_length=10, blank=True, default='')
    test_input = models.CharField(max_length=20, blank=True, default='')
    test_output = models.CharField(max_length=20, blank=True, default='')
    statement=models.TextField()
    
    


    

    