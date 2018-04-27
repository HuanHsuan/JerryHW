from django.shortcuts import render_to_response
# Create your views here.
from .models import Profile, Introduction, Hobby

def index(request):
	profilee = Profile.objects.all()
	return render_to_response('huan/intro.html',locals())