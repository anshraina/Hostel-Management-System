from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student
from django.contrib import messages


def register(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            messages.success(request, "New entry has been recorded")
            stud_id = request.POST.get('stud_id',)
            name = request.POST.get('name', )
            year = request.POST.get('year', )
            room = request.POST.get('room', )
            contact = request.POST.get('contact', )
            email = request.POST.get('email', )
            parents_name = request.POST.get('parents_name', )
            parents_contact = request.POST.get('parents_contact', )
            parents_email = request.POST.get('parents_email', )
            stud_obj = Student(stud_id=stud_id, name=name, year=year, room=room, contact=contact, email=email,
                               parents_name=parents_name, parents_email=parents_email, parents_contact=parents_contact)

            stud_obj.save()
            return redirect('/')

    else:
        return render(request, "NewEnrty.html")

# import socket
#
# s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# s.bind(("localhost", 8758))
#
#
# # con, addr = s.accept()
# # con.getsockname()
#
# while True:
#     msg, addr = s.recvfrom(1024)
#     m2 = msg.decode()
#     print(m2)
#     if m2 == "exit":
#         break
#     msg2 = input()
#     s.sendto(msg2.encode(), addr)
#
#
# s.close()
#
#
