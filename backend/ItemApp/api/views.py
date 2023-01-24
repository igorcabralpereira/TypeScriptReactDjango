from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from ItemApp.models import Items
from .serializers import ItemSerializer
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token',
        '/api/token/refresh',
    ]

    return Response(routes)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
@csrf_exempt
def itemApi(request):
    if request.method == 'GET':
        items = Items.objects.all().filter(user_id=request.user.id).order_by('date')
        # print(items)
        items_serializer = ItemSerializer(items, many=True)
        return Response(items_serializer.data)

    elif request.method == 'POST':
        item_data = JSONParser().parse(request)
        items_serializer = ItemSerializer(data=item_data)
        if items_serializer.is_valid():
            items_serializer.save()
            return JsonResponse("Criado com Sucesso", safe=False)
        return JsonResponse("Falha ao criar o registro", safe=False)

    elif request.method == 'PUT':
        item_data = JSONParser().parse(request)
        item = Items.objects.get(id=item_data['id'])
        items_serializer = ItemSerializer(item, data=item_data)
        if items_serializer.is_valid():
            items_serializer.save()
            return JsonResponse("Atualizado com sucesso", safe=False)
        return JsonResponse("Falha ao atualizar o registro", safe=False)

    elif request.method == 'DELETE':
        item_data = JSONParser().parse(request)
        item = Items.objects.get(id=item_data['id'])
        item.delete()
        return JsonResponse("Deletado com sucesso", safe=False)
    return JsonResponse("Falha ao deletar o registro", safe=False)
