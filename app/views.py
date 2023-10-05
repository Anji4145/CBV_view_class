from django.shortcuts import render
from django.views.generic import View,TemplateView
from django.http import HttpResponse
from app.forms import *
# Create your views here.

#function_Based_view by using view class,string response

def fbv(request):
    return HttpResponse('fbv string response')


#class_Based_view by using view class,string response
class Cbv(View):
    def get(self,request):
        return HttpResponse('Cbv string response')
    

#function_Based_view by using view class,html response
def fbv_page(request):
    return render(request,'fbv_page.html')

#class_Based_view by using view class,html response
class Cbv_Page(View):
    def get(self,request):
        return render(request,'Cbv_Page.html')

#function_Based_view by using view class,inserttion of data 
def insert_by_fbv(request):
    SFO=StudentForm()
    d={'SFO':SFO}
    if request.method=='POST':
        SFDO=StudentForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('Data Is Inserted')
    return render(request,'insert_by_fbv.html',d)


#Insert_by_cbv
class Insert_by_cbv(View):
    def get(self,request):
        SFO=StudentForm()
        d={'SFO':SFO}
        return render(request,'Insert_by_cbv.html',d)
    
    def post(self,request):
        SFDO=StudentForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('Data Is Inserted')
        

# Render Html page by using TemplateView

class CBV_Temp(TemplateView):
    template_name='CBV_Temp.html'