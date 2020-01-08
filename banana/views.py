import json
from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse
from .models import Post
from django.views.decorators.csrf import csrf_exempt
from .mango.transformdata import transformData
from .mango.responseData import responseData
from .mango.shared import BLOCK_ID

## Serializers
from .serializers import PostSerializer

ANSWER = ["극히 드물다","가끔 있었다","종종 있었다","대부분 그랬다","우울증 자가진단 시작하기"]

@csrf_exempt
def hello(request):
    rData = responseData(request)
    block_id = rData.getBlockId()
    print(block_id)
    utterance = rData.getUtterance()
    print(utterance)
    block_name = rData.getBlockName()
    print(block_name)
    if(ANSWER.__contains__(utterance)):
        if(utterance==ANSWER[0]):
            answer01 = 0
        elif(utterance==ANSWER[1]):
            answer01 = 1
        elif(utterance==ANSWER[2]):
            answer01 = 2
        elif(utterance==ANSWER[3]):
            answer01 = 3
        answer_1 = Post(q01=answer01)
        answer_1.save()
        data = transformData(block_id).getJsonData()
    else:
        data = transformData(block_id).getJsonDump()
    return data
    

# Create your views he`re.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

