from django.shortcuts import render
from django.http import JsonResponse
from .models import Bank,Branch
# Create your views here.

def bank_list(request):
    banks = Bank.objects.all().values('id','name')
    return JsonResponse(list(banks),safe=False)

def branch_detail(request,ifsc):
    try:
        branch = Branch.objects.select_related('bank').get(ifsc=ifsc)
        data = {
            'bank': {
                'id': branch.bank.id,
                'name': branch.bank.name
            },
            'ifsc': branch.ifsc,
            'branch': branch.branch,
            'address': branch.address,
            'city': branch.city,
            'district': branch.district,
            'state': branch.state
        }
        return JsonResponse(data)
    except:
        return JsonResponse({'error':'Branch not found'},status = 404)