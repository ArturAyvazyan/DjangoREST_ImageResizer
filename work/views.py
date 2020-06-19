from django.shortcuts import render, redirect
from rest_framework import generics
from work.serializers import ImageDetailSerializer, ImageListSerializer
from work.models import Image
from django.template import RequestContext



#HTML
def home(request):
    return render(request, 'dom.html')


def resize(request, pk):
    imagas = Image.objects.get(pk=pk)
    return render(request, 'shaba.html',{
        'imagas':imagas,
    })



#REST API
class ImageCreateView(generics.CreateAPIView):
    serializer_class = ImageDetailSerializer

class ImageListView(generics.ListAPIView):
    serializer_class = ImageListSerializer
    queryset = Image.objects.all()
    
class ImageDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ImageDetailSerializer
    queryset = Image.objects.all()
    