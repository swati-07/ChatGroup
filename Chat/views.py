from django.shortcuts import render

# Create your views here.
def indexview(request):
	return render(request,'index.html',{})

def roomview(request,room_name):
	
	return render(request,'chatroom.html',{'room_name':room_name})