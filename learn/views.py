#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse(u'欢迎光临 我的世界!')

def home(request):
	info_dict={'site':u'赤炼群青','content':'people mountain'}
	return render(request,'home.html',{'info_dict':info_dict})