from django.shortcuts import render, redirect, get_object_or_404
from .models import Child
from .models import Attend
from django.db.models import Q
from django.utils import timezone
from django.contrib import messages

# Create your views here.


def main(request):
    return render(request, 'main.html')


def one(request):
    child = Child.objects.filter(Q(classname="베드로반") | Q(classname="안드레반"))
    return render(request, 'attend1.html', {'child': child})


def two(request):
    child = Child.objects.filter(Q(classname="야고보반") | Q(classname="다대오반"))
    return render(request, 'attend2.html')


def three(request):
    child = Child.objects.filter(Q(classname="바돌로매반") | Q(classname="디모데반"))
    return render(request, 'attend3.html')


def four(request):
    child = Child.objects.filter(Q(classname="요한반") | Q(classname="빌립반"))
    return render(request, 'attend4.html')


def five(request):
    child = Child.objects.filter(Q(classname="마태반") | Q(classname="시몬반"))
    return render(request, 'attend5.html')


def six(request):
    child = Child.objects.filter(Q(classname="바울반") | Q(classname="누가반"))
    return render(request, 'attend6.html')


def attend(request):
    child = ''
    previous = request.POST["previous"]
    if previous[11:12] == '1':
        child = Child.objects.filter(Q(classname="베드로반") | Q(classname="안드레반"))
    if previous[11:12] == '2':
        child = Child.objects.filter(Q(classname="야고보반") | Q(classname="다대오반"))
    if previous[11:12] == '3':
        child = Child.objects.filter(
            Q(classname="바돌로매반") | Q(classname="디모데반"))
    if previous[11:12] == '4':
        child = Child.objects.filter(Q(classname="요한반") | Q(classname="빌립반"))
    if previous[11:12] == '5':
        child = Child.objects.filter(Q(classname="마태반") | Q(classname="시몬반"))
    if previous[11:12] == '6':
        child = Child.objects.filter(Q(classname="바울반") | Q(classname="누가반"))
    worship = request.POST.getlist('worship[]', "")
    zoom = request.POST.getlist('zoom[]', "")
    note = request.POST.getlist('note[]', '')
    for i, c in enumerate(child):
        attend = Attend()
        attend.child_id = c
        # attend.child_name = c.name
        if str(i+1) in worship:
            attend.att_worship = True
        else:
            attend.att_worship = False
        if str(i+1) in zoom:
            attend.att_zoom = True
        else:
            attend.att_zoom = False
        attend.att_memo = note[i]
        attend.recode_date = timezone.now()
        attend.att_date = timezone.now()
        attend.save()
        messages.info(request, zoom)
    return redirect(previous)
