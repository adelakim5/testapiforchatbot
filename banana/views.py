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
    utterance = received_json_data['userRequest']['utterance']
    param_id = int(received_json_data['action']['params']['id'])
    # print(type(param_id))
    post = Post.objects.all().get(id=param_id)
    return JsonResponse({
        "version": "2.0",
        "template": {
            "outputs": [{
            "simpleText": {
                "text":"id : {} , title : {} , content : {}".format(param_id, post.title, post.content)
            }
            }]
        }
    })

# Create your views he`re.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

