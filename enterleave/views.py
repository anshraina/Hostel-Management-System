from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .forms import EntryExitForm
from .models import inout
from NewEntry.models import Student
import datetime
from django.contrib import messages

# Create your views here.


@csrf_exempt
def entry_exit(request):
    if request.method == 'POST':
        global flag
        flag = 0
        obj = request.body.decode("utf-8")
        print("data from user", obj)
        form = EntryExitForm(request.POST)
        if form.is_valid():
            stud_id = request.POST.get('stud_id', )
            choice = request.POST.get('choice', )
            ch = choice.lower()
            if Student.objects.filter(stud_id=stud_id).exists():
                if ch == "in":
                    if inout.objects.filter(stud_id=stud_id).exists():
                        now = datetime.datetime.now()
                        print("in")
                        out_obj = inout(stud_id=stud_id, IN=now)
                        oobj = inout.objects.filter(stud_id=stud_id).order_by('-id')[:1]
                        if len(oobj) > 0:
                            if oobj[0].IN is None:
                                flag = 1
                                print("run hot")
                                for x in oobj:
                                    x.IN = now
                                    x.save()
                                messages.info(request, 'Student is in the hostel')
                            else:
                                messages.info(request, "Student is already IN")
                                flag = 1

                        if flag == 0:
                            out_obj.save()

                            messages.info(request, 'Student is in the hostel')
                            flag = 0

                        return render(request, "inout.html", {'stud_list': oobj})
                    else:
                        messages.error(request, "Invalid Operation!!!"
                                                "The student should be out first before "
                                                "getting in")

                elif ch == "out":
                    print("out")
                    now = datetime.datetime.now()
                    out_obj = inout(stud_id=stud_id, OUT=now)
                    oobj = inout.objects.filter(stud_id=stud_id).order_by('-id')[:1]
                    if len(oobj) > 0:
                        if oobj[0].IN is None:
                            messages.info(request, "Student is already out")
                            flag = 1
                            print("abc")

                    if flag == 0:
                        out_obj.save()
                        messages.success(request, 'Student in now out')
                        flag = 0

                    return render(request, "inout.html", {'stud_list': oobj})
            else:
                messages.error(request, "There is no student with this id")
                return redirect('/inout/entry_exit')
        else:
            print("wrong form")
            return redirect('/inout/entry_exit')
    else:
        return render(request, "inout.html")
