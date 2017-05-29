from django.shortcuts import render
from django.http import JsonResponse
from json import JSONEncoder
# vase inke barname csrf nakhad
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from .models import Expense, Income , Token , User , EventType
from datetime import datetime
from django.shortcuts import render

#TODO: behine sazi codeha, baresi moshkelate admin,...
@csrf_exempt
#    return render(request, "index.html")
def Submit_Expense(request):
    this__token = request.POST.get('token')
    this__user = User.objects.get(token__Token = this__token)
    now = datetime.now()
    Expense.objects.create(text = request.POST.get('text'), amount=request.POST.get('amount'), date=now, user=this__user)
    return JsonResponse({
    'status' : 'ok'
    }, encoder = JSONEncoder)
@csrf_exempt
def Submit_Income(request):
    this__token = request.POST.get('token')
    this__user = User.objects.get(token__Token = this__token)
    now = datetime.now()
    Income.objects.create(text = request.POST.get('text'), amount=request.POST.get('amount'), date=now, user=this__user)
    return JsonResponse({
    'status' : 'ok'
    }, encoder = JSONEncoder)
def Event_Type(request):
    etypes= EventType.objects.all()
    return render(request,'index.html',{'eventtypes' : etypes})
    
