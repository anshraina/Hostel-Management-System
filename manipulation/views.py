from bokeh.embed import components
from django.shortcuts import render, redirect
from NewEntry.models import Student
from enterleave.models import inout
from django.contrib import messages

from bokeh.plotting import figure


# Create your views here.


def search(request):
    my_id = 0
    if request.method == "POST":
        name = request.POST['name']
        if Student.objects.filter(name=name).exists():
            stud_list = Student.objects.filter(name=name)

            return render(request, "manipulationv2.html", {'stud_list': stud_list})

        else:
            messages.info(request, 'name does not exist')
            return redirect('/manipulation/search')

    else:
        stud_list = Student.objects.all()
        return render(request, "manipulationv2.html", {'stud_list': stud_list})


students_ids = []
counts = []


def visualize(request):
    global students_ids, counts
    if request.method == "post":
        return redirect('/')
    else:
        for p in Student.objects.raw('SELECT id, stud_id FROM NewEntry_student'):
            students_ids.append(p.stud_id)
            c = inout.objects.filter(stud_id=p.stud_id).count()
            counts.append(c)

        plot = figure(title='Bar Graph', x_axis_label='students ids', y_axis_label='frequency', plot_width=1250,
                      plot_height=700)
        plot.vbar(x=students_ids, top=counts, width=0.9)
        plot.y_range.start = 0
        plot.yaxis.axis_label_text_font_size = "25pt"
        plot.xaxis.axis_label_text_font_size = "25pt"
        script, div = components(plot)
        students_ids = []
        counts = []

        return render(request, "data_vis.html", {'script': script, 'div': div})
