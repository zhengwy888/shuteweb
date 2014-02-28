# Create your views here.
from revenue.models import Transaction
from revenue.forms import AddTransForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django import forms
import datetime
from dateutil.relativedelta import relativedelta

def index(request):
    return view_transactions(request)

def aggregateTrans(trans_list):
    currentMonth = {}

    for trans in trans_list:
        if ( trans.type not in currentMonth ) :
            currentMonth[trans.type]={}
            currentMonth[trans.type]['revenue']=0
            currentMonth[trans.type]['cost']=0
            currentMonth[trans.type]['margin']=0
        if trans.amount > 0:
            currentMonth[trans.type]['revenue'] += trans.amount
        else:
            currentMonth[trans.type]['cost'] -= trans.amount

    for type in currentMonth:
        if currentMonth[type]['revenue'] > 0 :
            currentMonth[type]['margin'] = format(1 - (currentMonth[type]['cost']/currentMonth[type]['revenue']), '.2%')
        else:
            currentMonth[type]['margin'] = 'N/A'

    return currentMonth

def view_transactions(request):
    timenow = datetime.date.today()

    monthbegin = datetime.date(year=timenow.year, month=timenow.month, day=1)
    prevmonth = monthbegin+relativedelta(months=-1)
    trans_list = Transaction.objects.filter(date__gte=monthbegin)
    prev_trans_list = Transaction.objects.filter(date__lt=monthbegin, date__gte=prevmonth)

    currentMonth = aggregateTrans(trans_list)
    prevMonth = aggregateTrans(prev_trans_list)

    newForm = AddTransForm(initial={'date':datetime.date.today(), 'type':'cn_med'})

    return render_to_response("revenue/transaction.html", locals(), context_instance=RequestContext(request))

def add_transactions(request):
    if request.POST:
        form = AddTransForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Added")
                return redirect('revenue.views.index')
            except:
                messages.error(request, "Bad Request")
                return HttpResponseRedirect(request.path)
        else:
            return HttpResponse('form is not valid')
    return HttpResponse('not POST')

def del_transactions(request, trans_id):
    p = get_object_or_404(Transaction, pk=trans_id)
    p.delete()
    return redirect('revenue.views.index')
