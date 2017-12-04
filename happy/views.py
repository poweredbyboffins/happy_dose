from django.template import RequestContext
from django.shortcuts import render_to_response
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib import messages
from django.db import connection
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import *
from .models import *
import datetime as d
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import components
from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral6
from bokeh.plotting import figure
from django.contrib.auth import logout

@login_required
def simple_chart(request):
    fruits = ['Dopamine', 'Oxytocin', 'Serotonin', 'Endorphine']
    counts = [9, 2, 3, 6]

    source = ColumnDataSource(data=dict(fruits=fruits, counts=counts, color=Spectral6))

    plot=figure(x_range=fruits, y_range=(0,9), plot_height=350, title="Neurotransmitter Analysis",
           toolbar_location=None, tools="")

    plot.vbar(x='fruits', top='counts', width=0.9, color='color', legend="fruits", source=source)

    plot.xgrid.grid_line_color = None
    plot.legend.orientation = "horizontal"
    plot.legend.location = "top_center"
    script, div = components(plot, CDN)

    return render(request, "happy/sc.html", {"the_script": script, "the_div": div})

@login_required
def stateofplay(request):
    """ get data """
    #select count(*)
    findcnt=Findout.objects.filter(userid=request.user.id).count()
    goalcnt=Goals.objects.filter(userid=request.user.id).count()
    #rescnt=Findout.objects.filter(userid=request.user.id).count()
    rescnt=1
    dict={"findcnt":findcnt,"goalcnt":goalcnt,"rescnt":rescnt}
    return render(request, "happy/sop.html", {'data':dict})

def index(request):
    return render(request, "happy/index.html", )
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('happy/findout.html')
    else:
        form = UserCreationForm()
    return render(request, 'happy/signup.html', {'form': form})

@login_required
def findout(request):
    return render(request, 'happy/findout.html')
@login_required
def happy(request):
    return render(request, 'happy/happiness.html')
@login_required
def assess(request):
    form = Assess(request.POST)
    uid=request.user.id
    print(uid)
    formdata = {}
    if form.is_valid():
       happy = form.cleaned_data.get('happy')
       dep = form.cleaned_data.get('dep')
       frust = form.cleaned_data.get('frust')
       anx = form.cleaned_data.get('anx')
       anger = form.cleaned_data.get('anger')
       stress = form.cleaned_data.get('stress')
       tire = form.cleaned_data.get('tire')
       trap = form.cleaned_data.get('trap')
       formdata = {"happy":happy,"dep":dep,"frust":frust
                  ,"anx":anx,"anger":anger,"stress":stress
                  ,"tire":tire,"trap":trap} 
       save(formdata,uid) 
    return render(request, 'happy/joy.html')
@login_required
def proc(request):
    form = FindOutForm(request.POST)
    uid=request.user.id
    formdata = {}
    if form.is_valid():
       #form.save()
       newexp = form.cleaned_data.get('newexp')
       heat = form.cleaned_data.get('heat')
       friends = form.cleaned_data.get('friends')
       family = form.cleaned_data.get('family')
       respected = form.cleaned_data.get('career')
       exercises = form.cleaned_data.get('exercises')
       outdoor = form.cleaned_data.get('outdoor')
       formdata = {"newexp":newexp,"heat":heat,"friends":friends
                  ,"family":family,"respected":respected,"exercises":exercises
                  ,"outdoor":outdoor} 
       save(formdata,uid) 
    return render(request, 'happy/happiness.html')

def save(formdata,uid):
    findout = Findout()
    for key,value in formdata.items():
        findout.userid=uid
        findout.facttype=key
        findout.value=value
        findout.save()

def logout_view(request):
    logout(request)
    return render(request, 'happy/logout.html')
