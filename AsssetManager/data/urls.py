from django.contrib import admin
from django.urls import path
from .views import home,add,note_delete,AssetUpdateView,EmployeeUpdateView,asset,employee,addemployee,employ_delete,SearchResultsView, EmployeeResultsView,csvexport,csvexport2

urlpatterns = [
    path("dashboard/",home,name="home"),
    path("data/",asset,name="asset"),
    path("employee/",employee,name="employ"),
    path("add/",add,name="add"),
    path("add/employee/",addemployee,name="addemployee"),
    path("delete/<id>",note_delete,name="delete"),
    path("emplyee/delete/<id>",employ_delete,name="employeedelete"),
    path("update/<pk>",AssetUpdateView.as_view(),name="update"),
    path("employee/update/<pk>",EmployeeUpdateView.as_view(),name="employeeupdate"),
    path("search/",SearchResultsView.as_view(template_name="data/search_result.html"),name="search"),
    path("search/emp",EmployeeResultsView.as_view(template_name="data/empsearch.html"),name="empsearch"),
    path("data/csv/",csvexport,name="csv"),
    path("data/cs/",csvexport2,name="csv2")
]
