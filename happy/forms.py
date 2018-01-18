from django import forms

class FindOutForm(forms.Form):
    newexp=forms.IntegerField()
    heat=forms.IntegerField()
    friends=forms.IntegerField()
    family=forms.IntegerField()
    career=forms.IntegerField()
    respected=forms.IntegerField()
    exercises=forms.IntegerField()
    outdoor=forms.IntegerField()

class Assess(forms.Form):
    happy=forms.IntegerField()
    dep=forms.IntegerField()
    frust=forms.IntegerField()
    anx=forms.IntegerField()
    anger=forms.IntegerField()
    stress=forms.IntegerField()
    tire=forms.IntegerField()
    trap=forms.IntegerField()
#class Goals(forms.Form):
