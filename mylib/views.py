from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from . import models

# Create your views here.
class MainView(View):
    def get(self,request):
        return render(request,"LandingPage.html")


class MoviesView(View):
    def get(self,request):
        return render(request,"Movies.html")


class TVShowsView(View):
    def get(self,request):
        return render(request,"TVShows.html")


class CrewView(View):
    def get(self,request):
        return render(request,"CastAndCrew.html")

class Comunity(View):
    def get(self,request):
        return render(request,"Community.html")

class AboutPage(View):
    def get(self,request):
        return render(request,"About.html")


def MovieDetail(request,id):
    movie = models.Movie.objects.get(id=id)

    context = {
        "movie":movie
    }
    return render(request,"Movie.html",context)


def register(request):
    if request.method == 'POST':
        full_name = request.POST['fname']
        email = request.POST['femail']
        password = request.POST['fpass']
        re_password = request.POST['frepass']

        if password != re_password:
            return render(request, 'register.html', {'error': 'Passwords do not match'})

        user = models.User.objects.create_user(username=email, email=email, password=password, first_name=full_name)
        login(request, user)
        return redirect('main')

    return render(request, 'register.html')
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('femail')
        password = request.POST.get('fpass')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('main')  #
        else:
            return render(request, 'SignIn.html', {'error': 'Invalid credentials'})
    return render(request, 'SignIn.html')

class MoviesbyCountry(View):
    def get(self,request):
        countries = models.Country.objects.all()
        context = {
            'countries':countries
        }

        return render(request,"MoviesByCountry.html",context)