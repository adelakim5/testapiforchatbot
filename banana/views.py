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
    print(received_json_data['userRequest']['utterance'])
    return JsonResponse({
  "version": "2.0",
  "template": {
    "outputs": [{
      "simpleText": {
        "text": "hello I'm Ryan"
      }
    }]
  }
})

# Create your views he`re.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

