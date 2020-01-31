from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
import json
# Create your views here.

def index(request):
    return render(request, 'demo_page.html')


def demo_call(request):
    return render(request, 'index.html')


def success_call(request):
    current_user = request.user
    context = {
        'fname' : current_user.first_name,
        'lname' : current_user.last_name,
        'email' : current_user.email,
    }
    print(context)
    return render(request, 'success.html',context)

def save_pword(request):
    return render(request,'reset_password.html')

def reset_password(request):
    try:
        if request.method == 'POST':
            password = request.POST.get('password2')
            id = request.user.id
            user = User.objects.get(id = id)
            email = request.user.email
            user.password = password
            user.is_staff = True
            user.save()
            print('---------------details saved successfully-------------')
    except Exception as e:
        print(e)
        data = {}
    return HttpResponse(json.dumps(data), content_type='application/json')