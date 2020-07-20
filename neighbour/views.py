from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


@login_required(login_url='/accounts/login/')
def index(request):
    title = "Neighbourhood"
    
    business = Business.objects.all()
    context = {
        "title": title,
        "business": business
    }
    return render(request, 'index.html', context)

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/login')
    else:
        form = RegisterForm()
    return render(request, 'registration/registration_form.html', {"form": form}))
    
@login_required(login_url='/login')
def profile(request):
    user = request.user
    context = {
        "user": user,
    }
    return render(request, 'profile.html', context)

