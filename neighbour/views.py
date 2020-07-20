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



@login_required(login_url='/login')
def create_profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,
                                   request.FILES, instance=request.user.profile)
        if user_form.is_valid() and p_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('/profile/')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,
                                   request.FILES, instance=request.user.profile)
    return render(request, 'create_profile.html', {"user_form": user_form, "profile_form": profile_form, })

def search_results(request):
    if 'businesses' in request.GET and request.GET["businesses"]:
        search_term = request.GET.get('businesses')
        searched_businesses = Business.search_by_name(search_term)
        message = f'{search_term}'

        context = {
            "message": message,
            "businesses": searched_businesses,
        }
        return render(request, 'search.html', context)
    else:
        message = "Search for a business by its name"
        return render(request, 'search.html', {"message": message})