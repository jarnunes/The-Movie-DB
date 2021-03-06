from django.shortcuts import render, HttpResponse
from django.http import HttpResponseBadRequest, JsonResponse
from movie.python import themovie_api, utils
import json


def init(request):
    return render(request=request, template_name=('movie/index.html'))


def popular(request):
    movies = themovie_api.popular()
    context = {'movies': movies}

    if utils.is_ajax(request):
        if request.method == 'GET':
            context = themovie_api.search(request.body)
            return JsonResponse({'status': 200, 'message': 'Insert here your message', 'context': context})
        else:
            return HttpResponseBadRequest('Invalid request')

    return render(request=request, template_name='movie/index.html', context=context)


def search(request):
    if utils.is_ajax(request):
        if request.method == "POST":
            search_str = json.loads(request.body).get("searchText")
            search_result = themovie_api.search(search_str)
            return JsonResponse({"data": search_result})


def new_movies(request):
    ...


def get_movie_info(request, _id):
    if utils.is_ajax(request):
        if request.method == 'GET':
            movie_info = themovie_api.get_movie(_id)
            print(movie_info)
            return JsonResponse({"data": movie_info})
    return HttpResponseBadRequest("<h2>Página não encontrada</h2>")
