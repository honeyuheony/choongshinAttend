from django.shortcuts import render, redirect, get_object_or_404
from .models import Child
from .models import Attend
from django.db.models import Q
from django.utils import timezone
from django.contrib import messages

from datetime import date
from datetime import timedelta
from datetime import datetime
import json

today = date.today()
diff = (today.weekday() - 6) % 7
last_sun = today - timedelta(days=diff)

# Create your views here.


def main(request):
    year = str(last_sun)
    return render(request, 'main.html', {'year': year})


def nextSunday(request, year):
    previous = request.POST["previous"]
    year = datetime.strptime(year, '%Y-%m-%d') - timedelta(7)
    return redirect(previous, str(year))


def prevSunday(request, year):
    previous = request.POST["previous"]
    year = datetime.strptime(year, '%Y-%m-%d') + timedelta(7)
    return redirect(previous, str(year))


def one(request):
    if request.method == "POST":
        year = str(request.POST.get("attend_date"))
    else:
        year = str(last_sun)

    child = Child.objects.filter(Q(classname="베드로반") | Q(classname="안드레반"))
    attendList = []
    for c in child:
        try:
            attendList.append(Attend.objects.get(child_id=c, att_date=year))
        except Attend.DoesNotExist:
            attend = Attend()
            attend.child_id = c
            attendList.append(attend)
    return render(request, 'attend1.html', {'attendList': attendList, 'year': year})
# def one(request):
#     year = last_sun
#     child = Child.objects.filter(Q(classname="베드로반") | Q(classname="안드레반"))
#     attendList = []
#     for c in child:
#         try:
#             attendList.append(Attend.objects.get(
#                 child_id=c, att_date=year))
#         except Attend.DoesNotExist:
#             attendList.append(Attend())
#     return render(request, 'attend1.html', {'attendList': attendList})


def two(request):
    child = Child.objects.filter(Q(classname="야고보반") | Q(classname="다대오반"))
    return render(request, 'attend2.html', {'child': child})


def three(request):
    child = Child.objects.filter(Q(classname="바돌로매반") | Q(classname="디모데반"))
    return render(request, 'attend3.html', {'child': child})


def four(request):
    child = Child.objects.filter(Q(classname="요한반") | Q(classname="빌립반"))
    return render(request, 'attend4.html', {'child': child})


def five(request):
    child = Child.objects.filter(Q(classname="마태반") | Q(classname="시몬반"))
    return render(request, 'attend5.html', {'child': child})


def six(request):
    child = Child.objects.filter(Q(classname="바울반") | Q(classname="누가반"))
    return render(request, 'attend6.html', {'child': child})


def attend(request):
    child = ''
    attend_date = request.POST["attend_date"]
    previous = request.POST["previous"]
    previous_page = ''
    if previous[11:12] == '1':
        child = Child.objects.filter(Q(classname="베드로반") | Q(classname="안드레반"))
        previous_page = one
    if previous[11:12] == '2':
        child = Child.objects.filter(Q(classname="야고보반") | Q(classname="다대오반"))
        previous_page = two
    if previous[11:12] == '3':
        child = Child.objects.filter(
            Q(classname="바돌로매반") | Q(classname="디모데반"))
        previous_page = three
    if previous[11:12] == '4':
        child = Child.objects.filter(Q(classname="요한반") | Q(classname="빌립반"))
        previous_page = four
    if previous[11:12] == '5':
        child = Child.objects.filter(Q(classname="마태반") | Q(classname="시몬반"))
        previous_page = five
    if previous[11:12] == '6':
        child = Child.objects.filter(Q(classname="바울반") | Q(classname="누가반"))
        previous_page = six
    worship = request.POST.getlist('worship[]', '')
    zoom = request.POST.getlist('zoom[]', '')
    note = request.POST.getlist('note[]', '')
    for i, c in enumerate(child):
        try:
            attend = Attend.objects.get(child_id=c, att_date=attend_date)
        except Attend.DoesNotExist:
            attend = Attend()
            attend.child_id = c
        # attend.child_name = c.name
        if str(attend.child_id) in worship:
            attend.att_worship = True
        else:
            attend.att_worship = False
        if str(attend.child_id) in zoom:
            attend.att_zoom = True
        else:
            attend.att_zoom = False
        attend.att_memo = note[i]
        attend.recode_date = timezone.now()
        attend.att_date = attend_date
        attend.save()
        messages.info(request, zoom)
    return redirect(previous_page)
