from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from . models import Allcourses,Details

# Create your views here.
def courses(request):
    courses = Allcourses.objects.all()
    template_name ="technicalcourses/index.html"
    context ={'courses':courses}
    return render(request,template_name,context)

def details(request,course_id):
    course = get_object_or_404(Details,pk=course_id)
    template_name =   "technicalcourses/details.html"
    context ={'course':course}
    return render(request,template_name,context)

