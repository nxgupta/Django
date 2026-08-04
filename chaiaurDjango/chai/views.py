from django.shortcuts import render
from .models import ChaiVariety
from django.shortcuts import get_object_or_404

# Create your views here.
def all_chai(Request):
    chais = ChaiVariety.objects.all()
    return render(Request, 'chai/all_chai.html', {'chais':chais})

def chai_detail(Request, chai_id):
    chai = get_object_or_404(ChaiVariety, pk=chai_id)
    return render(Request, 'chai/chai_detail.html', {"chai":chai})