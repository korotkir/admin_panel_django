from django.shortcuts import render
from django.shortcuts import redirect
from django.conf import settings
from django.http import HttpResponse



def main(request):
	if request.user.is_authenticated:
		return render(request, 'main/index.html')
	else:
		return redirect('/accounts/login/')
