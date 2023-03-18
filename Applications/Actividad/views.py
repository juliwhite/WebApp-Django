from django.shortcuts import render, redirect
from .models import Activity

# Create your views here.
def home(request):
    activityList = Activity.objects.all()
    return render(request, "arrangeActivity.html", {"activity":activityList})

def registerActivity(request):
    group=request.POST['txtGroup']
    activities=request.POST['txtActivities']
    date=request.POST['begin']

    activity = Activity.objects.create(group=group, activities=activities, date=date)
    return redirect('/')

def deleteActivity(request, activities):
    activity = Activity.objects.get(activities=activities)
    activity.delete()

    return redirect('/')
