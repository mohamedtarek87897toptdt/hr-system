from django.shortcuts import render
#from django.http import HttpResponse
from .models import branches

# Create your views here. 
def Branches(request):
    b = branches.objects.all()
    return render(request,'branches.html',{'branches':b})
    

def BranchesDetails(request,branche_id):
   b = branches.objects.get(pk=branche_id)
   departments = b.departmentsBranche.all()
   #print(departments)
   return render(request,'brancheDetails.html',{'branche':b,'departments':departments}) 
