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


@login_required(login_url='/login')
def post_business(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostBusinessForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.owner = current_user
            image.save()
        return redirect('/')
    else:
        form = PostBusinessForm(auto_id=False)
    return render(request, 'add_business.html', {"form": form})  

@login_required(login_url='/login')
def notices(request):
    user = Profile.objects.get(user=request.user.id)
    alerts = Notices.objects.all().filter(hood=user.hood)
    current_user = request.user
    if request.method == 'POST':
        hood = Hood.objects.get(name=user.hood)
        form = PostNotice(request.POST, request.FILES)
        if form.is_valid():
            title = form.save(commit=False)
            title.author = current_user
            title.hood = hood
            title.save()
            return redirect('/notices/')
    else:
        form = PostNotice(auto_id=False)
    return render(request, 'notices.html', {"notices": alerts, "form": form})

@login_required(login_url='/login')
def establishment(request):
    user = Profile.objects.get(user=request.user.id)
    neccesities = Establishment.objects.all().filter(hood=user.hood)
    current_user = request.user
    if request.method == 'POST':
        hood = Hood.objects.get(name=user.hood)
        form = AddEstablishment(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.author = current_user
            image.hood = hood
            image.save()
            return redirect('/establishment/')
    else:
        form = AddEstablishment(auto_id=False)
    return render(request, 'establishment.html', {"establishment": neccesities, "form": form})        