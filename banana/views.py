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
    utterance = received_json_data['userRequest']['utterance']
    param_id = int(received_json_data['action']['params']['id'])
    # print(type(param_id))
    post = Post.objects.all().get(id=param_id)
    return JsonResponse({
"version": "2.0",
  "template": {
    "outputs": [
      {
        "simpleText": {
          "text": "토트넘 선수 리스트입니다."
        }
      }
    ],
    "quickReplies": [
      {
        "messageText": "손흥민",
        "action": "message",
        "label": "손흥민"
      },
      {
        "messageText": "헤리케인",
        "action": "message",
        "label": "헤리케인"
      },
      {
        "messageText": "에릭센",
        "action": "message",
        "label": "에릭센"
      },
      {
        "messageText": "요리스",
        "action": "message",
        "label": "요리스"
      }
    ]
  }
})

# Create your views he`re.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

