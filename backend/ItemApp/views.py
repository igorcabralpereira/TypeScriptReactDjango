from django.shortcuts import render
#
#from django.views.decorators.csrf import csrf_exempt
#from rest_framework.parsers import JSONParser
#from django.http.response import JsonResponse
#
#from ItemApp.models import Items
#from ItemApp.serializers import ItemSerializer
#
#
# @csrf_exempt
# def itemApi(request, id=0):
#    if request.method == 'GET':
#        items = Items.objects.all().filter(user_id=request.user.id).order_by('date')
#        print(items)
#        items_serializer = ItemSerializer(items, many=True)
#        return JsonResponse(items_serializer.data, safe=False)
#
#    elif request.method == 'POST':
#        item_data = JSONParser().parse(request)
#        items_serializer = ItemSerializer(data=item_data)
#        if items_serializer.is_valid():
#            items_serializer.save()
#            return JsonResponse("Criado com Sucesso", safe=False)
#        return JsonResponse("Falha ao criar o registro", safe=False)
#
#    elif request.method == 'PUT':
#        item_data = JSONParser().parse(request)
#        item = Items.objects.get(id=item_data['id'])
#        items_serializer = ItemSerializer(item, data=item_data)
#        if items_serializer.is_valid():
#            items_serializer.save()
#            return JsonResponse("Atualizado com sucesso", safe=False)
#        return JsonResponse("Falha ao atualizar o registro", safe=False)
#
#    elif request.method == 'DELETE':
#        item = Items.objects.get(id=id)
#        item.delete()
#        return JsonResponse("Deletado com sucesso", safe=False)
#    return JsonResponse("Falha ao deletar o registro", safe=False)
