from django.shortcuts import render
from django.forms import model_to_dict
from rest_framework import generics
from .models import Mens
from .serializers import MensSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class MensAPIView(APIView):
    def get(self, request):
        lst = Mens.objects.all()
        return Response({'posts': MensSerializer(lst, many=True).data})
    
    def post(self, request):
        serializers = MensSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        
        return Response({'post': serializers.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})
        
        try:
            instance = Mens.objects.get(pk=pk)
        except:
            return Response({"error": "Method PUT not allowed"})
        
        serializers = MensSerializer(data=request.data, instance=instance)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response({"post": serializers.data})
        

# class MensAPIView(generics.ListAPIView):
#     queryset = Mens.objects.all()
#     serializer_class = MensSerializer