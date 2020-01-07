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

ANSWER = ["극히 드물다","가끔 있었다","종종 있었다","대부분 그랬다","우울증 자가진단"]

@csrf_exempt
def hello(request):
    rData = responseData(request)
    block_id = rData.getBlockId()
    print(block_id)
    utterance = rData.getUtterance()
    print(utterance)
    block_name = rData.getBlockName()
    print(block_name)
    data = transformData(block_id).getJsonDump()   
    if(ANSWER.__contains__(utterance)):
        data = transformData(block_id).getJsonData()
    return data
    

# Create your views he`re.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

