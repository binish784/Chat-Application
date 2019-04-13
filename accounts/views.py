from django.shortcuts import render,get_object_or_404
from django.conf import settings

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


from django.http import HttpResponseRedirect
from django.db.models import Q

# Create your views here.

from .models import Profile,friendRequest


@login_required
def HomeView(request):
	user_profile=Profile.objects.get(user=request.user)
	connected=user_profile.friends.all()
	context={
		'friends':connected
	}
	return render(request,'accounts/home.html',context)

def users_list(request):
	user_profile=Profile.objects.get(user=request.user)
	users=Profile.objects.filter().exclude(profile=user_profile).exclude(user=request.user)
	context={
		'all_users':users,
	}
	return render(request,'accounts/all_users.html',context)

def show_send_requests(request):
	requests=friendRequest.objects.filter(from_user=request.user)
	context={
		'requests':requests,
	}
	return render(request,'accounts/sentRequest.html',context)

def send_friend_request(request,id):
	to_user=get_object_or_404(User,id=id)
	from_user=request.user
	frequest,created=friendRequest.objects.get_or_create(
		from_user=from_user,
		to_user=to_user
		)
	return HttpResponseRedirect('/')

def cancel_friend_request(request,id):
	to_user=get_object_or_404(User,id=id)
	frequest=friendRequest.objects.get(
		to_user=to_user,
		from_user=request.user
		)
	frequest.delete()
	return HttpResponseRedirect('/')

def accept_friend_request(request,id):
	to_user=get_object_or_404(User,id=id)
	frequest=friendRequest.objects.filter(to_user=to_user,from_user=request.user).first()
	user1=to_user
	user2=request.user
	user1.Profile.friends.add(user2.Profile)
	user2.Profile.friends.add(user1.Profile)
	frequest.delete()
	return HttpResponseRedirect('')

