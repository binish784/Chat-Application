from django.shortcuts import render,get_object_or_404

from django.contrib.auth.models import User
from django.http import JsonResponse

from .forms import ChatForm

from .models import chat
from accounts.models import friendRequest,Profile

# Create your views here.


def showMessage(request,id):
	messages=''
	to_user=get_object_or_404(User,id=id)
	form=ChatForm()
	if(to_user==request.user):
		message="Chatting with yourself huh !!"
	else:
		to_user_profile=get_object_or_404(Profile,user=to_user)
		request_user_profile=Profile.objects.get(user=request.user)
		if(request_user_profile.friends.filter(user=to_user).first()):
			status=True
			message="Connected to " + to_user.username
			messages = chat.objects.filter(message_to=request.user,message_from=to_user) | chat.objects.filter(message_to=to_user,message_from=request.user)
			messages.order_by('pk')
		else:
			status=False
			message="Connection terminated , You are not friends with " + to_user.username
	context={
		'messages':messages,
		'reciever_id':id,
		'status':status,
		'message': message,
		'form':form,
	}
	return render(request,'chat/message.html',context)

def sendMessage(request,id):
	message=request.GET.get('message',None)
	reciever=User.objects.get(id=id)
	if message:
		message=chat(message_from=request.user,message_to=reciever,message=message);
		message.save()
		data={
			'message':'Message Has been sent',
		}
	else:
		data={
			'message':'Error in sending message',
		}
	return JsonResponse(data)

def getMessage(request,id):
	user2=get_object_or_404(User,id=id);
	messages = chat.objects.filter(message_to=request.user,message_from=user2) | chat.objects.filter(message_to=user2,message_from=request.user)
	messages.order_by('pk')
	data_set=[]
	for msg in messages:
		message=msg.message
		message_to=msg.message_to.username
		message_from=msg.message_from.username
		if message_to==request.user.username:
			status=1
		else:
			status=0
		data_pack={
			'message':message,
			'message_to':message_to,
			'message_from':message_from,
			'status':status
		}
		data_set.append(data_pack)
	data={
		'messages':data_set,
	}
	return JsonResponse(data)	