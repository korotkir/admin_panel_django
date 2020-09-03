from django.shortcuts import render
from django.shortcuts import redirect
from django.conf import settings
from django.http import HttpResponse

def billing(request):
	if request.user.is_authenticated:
		return render(request, 'billing/Billing-1.html')
	else:
		return redirect('/accounts/login/')
