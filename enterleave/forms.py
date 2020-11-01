from django import forms


class EntryExitForm(forms.Form):
    stud_id = forms.IntegerField()
    choice = forms.CharField(max_length=10)


