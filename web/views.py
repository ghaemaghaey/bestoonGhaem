from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def dakhl(request):
    return JsonResponse({'status':'ok'})
def kharg(request):
    
    return JsonResponse({str(request.POST):'ok'})