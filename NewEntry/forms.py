from django import forms


class StudentForm(forms.Form):
    stud_id = forms.IntegerField()
    name = forms.CharField(max_length=100)
    year = forms.CharField(max_length=10)
    contact = forms.BigIntegerField()
    email = forms.EmailField(max_length=50)
    room = forms.PositiveSmallIntegerField()
    parents_name = forms.CharField(max_length=100)
    parents_contact = forms.BigIntegerField()
    parents_email = forms.EmailField(max_length=50)

