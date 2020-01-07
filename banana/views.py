import json
from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse,JsonResponse
from .models import Post
from django.views.decorators.csrf import csrf_exempt

## Serializers
from .serializers import PostSerializer

@csrf_exempt
def hello(request):
    received_json_data = json.loads(request.body.decode("utf-8"))
    print(received_json_data)
    # utterance = received_json_data['userRequest']['utterance']
    # param_id = int(received_json_data['action']['params']['id'])
    # print(type(param_id))
    # post = Post.objects.all().get(id=param_id)
    data = {
        "version": "2.0",
        "template": {
            "outputs": [
            {
                "simpleText": {
                "text": "평소에는 아무렇지도 않던 일들이 괴롭고 귀찮게 느껴졌다."
                }
            }
            ],
            "quickReplies": [
            {
                "messageText": "극히 드물다",
                "action": "block",
                "label": "극히 드물다"
            },
            {
                "messageText": "가끔 있었다",
                "action": "block",
                "label": "가끔 있었다"
            },
            {
                "messageText": "종종 있었다",
                "action": "block",
                "label": "종종 있었다"
            },
            {
                "messageText": "대부분 그랬다",
                "action": "block",
                "label": "대부분 그랬다"
            }
            ]
        }
    }
    return JsonResponse(data)

# Create your views he`re.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

