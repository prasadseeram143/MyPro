from django.http import HttpResponse,HttpResponseRedirect
from details.models import detail
from django.shortcuts import render,render_to_response
from django.core.context_processors import csrf
from django.template import RequestContext
from django.views.generic.base import TemplateView
from details.forms import *

class Adds(TemplateView):
    def vn(customer_name):
        if customer_name.isalpha():
            pass
        else:
            raise ValidationError('please enter alphabetics')
    template_view='adds.html'
    def get(self,request):
         form=TestForm()
         return render_to_response('adds.html',locals(),context_instance=RequestContext(request))
    def post(self, request):
        form=TestForm(request.POST)
        if form.is_valid():
             customer = form.cleaned_data['customer_name']
             customer_mobile = form.cleaned_data['customer_mnum']
             cprblm=form.cleaned_data['complaint_problem']
             cnum=form.cleaned_data['complaint_num']
             detail.objects.create(customer_name=customer,customer_mnum=customer_mobile,complaint_problem=cprblm,complaint_num=cnum)
             HttpResponseRedirect('/')
        else:
             #return HttpResponse('validationError')
             return HttpResponseRedirect('/errors/')
        return HttpResponseRedirect('/')
class Details(TemplateView):
    template_view='details.html'
    def get(self, request):
        s=detail.objects.all()
        return render_to_response('details.html',locals(),context_instance=RequestContext(request))
class Shows(TemplateView):
    template_view='shows.html'
    def get(self,request,id):
        s=detail.objects.get(id=id)
        return render_to_response('shows.html',locals(),context_instance=RequestContext(request))
class Deletes(TemplateView):
    def get(self,request,id):
        d=detail.objects.get(id=id)
        d.delete()
        return render(request,'details.html')
class Errors(TemplateView):
    def get(self,request):
        return render(request,'errors.html')
