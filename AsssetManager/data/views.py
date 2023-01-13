from django.shortcuts import redirect, render,get_object_or_404
from django.views.generic import UpdateView,ListView
from .forms import AssetForm,EmployeeForm
from .models import Asset,EmployeeAsset
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import date
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db.models import Q
import csv
# Create your views here.

@login_required
def home(request):
    good=0
    bad=0
    asset=Asset.objects.all()
    employ=EmployeeAsset.objects.all()

    for i in asset:
        if i.condition=="Good":
            good+=1
        elif i.condition=="Bad":
            bad+=1
    context={
        "asset":asset,
        "employ":"employ",
        "good":good,
        "bad":bad,

    }

    return render(request,"data/index3.html",context)


def asset(request):
    asset=Asset.objects.all()

    context={
        "asset":asset
    }

    return render(request,"data/asset.html",context)

def employee(request):
    employ=EmployeeAsset.objects.all()

    context={
        "employ":employ
    }

    return render(request,"data/employee.html",context)



def add(request):

    if request.method=="POST":
        form=AssetForm(request.POST)

        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse("asset"))
    else:
        form=AssetForm()
    
    return render(request,"data/index.html",{"form":form})


def addemployee(request):

    if request.method=="POST":
        form=EmployeeForm(request.POST)

        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse("employ"))
    else:
        form=AssetForm()
    
    return render(request,"data/index.html",{"form":form})



def note_delete(request,id):
    obj=get_object_or_404(Asset,pk=id)
    obj.delete()
    return redirect("home")

def employ_delete(request,id):
    obj=get_object_or_404(EmployeeAsset,pk=id)
    obj.delete()
    return redirect("employ")

class AssetUpdateView(UpdateView):
    model = Asset
    template_name = "data/index.html"
    form_class=AssetForm

    def get_success_url(self) -> str:
        return '/asset/data'

class EmployeeUpdateView(UpdateView):
    model = EmployeeAsset
    template_name = "data/employeeform.html"
    form_class=EmployeeForm

    def get_success_url(self) -> str:
        return '/asset/employee'
    

class SearchResultsView(ListView):
    model = Asset
    template_name = "data/search_results.html"

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Asset.objects.filter(
            Q(name__icontains=query) | Q(specifications__icontains=query)
        )
        return object_list


class EmployeeResultsView(ListView):
    model = EmployeeAsset
    template_name = "data/empsearch.html"

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = EmployeeAsset.objects.filter(
            Q(name__icontains=query) | Q(specifications__icontains=query)
        )
        return object_list



def csvexport(request):
    dats=Asset.objects.all()
    response=HttpResponse('text/csv')
    response['Content-Disposition']='attachment;filename=data_export.csv'
    writer=csv.writer(response)
    writer.writerow(['title','description','time_posted','website'])
    fake_fields=dats.values_list('name','specifications','condition','location','date_entered')
    for dat in fake_fields:
        writer.writerow(dat)
    return response
    return HttpResponseRedirect(reverse("home"))


def csvexport2(request):
    dats=EmployeeAsset.objects.all()
    response=HttpResponse('text/csv')
    response['Content-Disposition']='attachment;filename=data_export.csv'
    writer=csv.writer(response)
    writer.writerow(['title','description','time_posted','website'])
    fake_fields=dats.values_list('name','specifications','condition','location','date_entered')
    for dat in fake_fields:
        writer.writerow(dat)
    return response
    return HttpResponseRedirect(reverse("home"))