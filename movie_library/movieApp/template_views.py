from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from movieApp.serializers import CodeForm
from TwoFAUserApp.models import TwoFAUser
from .utils import send_sms
from movieApp.models import Code
import random


def landing_page(request):
    return render(request, 'LandingPage.html', {})


def movies(request):
    return render(request, 'Movies.html')


def movie_detail(request, movie_id):
    return render(request, 'Movie.html', {'movie_id': movie_id})


def tv_shows(request):
    return render(request, 'TVShows.html')


def about(request):
    return render(request, 'About.html')


def community(request):
    return render(request, 'Community.html')


def movies_by_country(request):
    return render(request, 'MoviesByCountry.html')


def country_movies(request):
    return render(request, 'Country_movies.html')


def register(request):
    if request.method == 'POST':
        # Your existing registration logic here
        # After successful registration:
        return redirect('landing_page')
    # Your existing GET logic here
    return render(request, 'Register.html')


def sign_in(request):
    return render(request, 'SignIn.html')


def cast_and_crew(request):
    return render(request, 'CastAndCrew.html')

# 2FA


@login_required
def home_view(request):
    return render(request, 'home.html', {})


def auth_view(request):
    form = AuthenticationForm()
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            request.session['pk'] = user.pk
            return redirect('verify_view')
    return render(request, 'auth.html', {'form': form})


def verify_view(request):
    form = CodeForm(request.POST or None)
    pk = request.session.get('pk')

    if not pk:
        return redirect('auth_view')

    try:
        user = TwoFAUser.objects.get(pk=pk)
    except TwoFAUser.DoesNotExist:
        return redirect('auth_view')

    if request.method == "GET" and not request.POST:
        code, created = Code.objects.get_or_create(user=user)

        number_list = [x for x in range(10)]
        code_items = []
        for i in range(5):
            num = random.choice(number_list)
            code_items.append(num)

        code_string = "".join(str(item) for item in code_items)
        code.codenumber = code_string
        code.save()

        code_user = f"{user.username}: {code.codenumber}"
        send_sms(code_user, user.phone_number)

    if request.method == "POST" and form.is_valid():
        num = form.cleaned_data.get('codenumber')
        code = Code.objects.get(user=user)
        if str(code.codenumber) == str(num):
            login(request, user)
            return redirect('home_view')
        else:
            form.add_error('codenumber', 'Invalid code. Please try again.')

    return render(request, 'verify.html', {'form': form})
