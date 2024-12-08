from django.shortcuts import render

def landing_page(request):
    return render(request, 'LandingPage.html')

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
    return render(request, 'Register.html')

def sign_in(request):
    return render(request, 'SignIn.html') 

def cast_and_crew(request):
    return render(request, 'CastAndCrew.html')

def movies_by_country(request):
    return render(request, 'MoviesByCountry.html')

def country_movies(request):
    return render(request, 'Country_movies.html')