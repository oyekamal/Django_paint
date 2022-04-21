# Create your views here.

from secrets import choice
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Files
from django.views.decorators.csrf import csrf_exempt
import json
import random

import string


@csrf_exempt
def paint(request):
    if request.method == 'GET':
        return render(request, 'paint.html')
    elif request.method == 'POST':
        filename = request.POST['save_fname']
        data = request.POST['save_cdata']
        image = request.POST['save_image']
        file_data = Files(name=filename, image=data, canvas_image=image)
        file_data.save()
        return HttpResponseRedirect('/')


@csrf_exempt
def files(request):
    if request.method == 'GET':
        all_data = Files.objects.all()
        return render(request, 'files.html', {'files': all_data})


@csrf_exempt
def game(request):
    if request.method == 'GET':
        # all_data = Files.objects.all()

        ABC = string.ascii_uppercase
        list_of_ABC = list(ABC)

        # sampling with replacement
        # k = number of items to select
        question_letter = random.choices(list_of_ABC, k=1)
        sample_list = random.choices(list_of_ABC, k=3)
        sample_list.append(question_letter[0])
        print(question_letter)
        print(sample_list)
        question_letter = "alphabets/{}_500x500.png".format(
            question_letter[0])
        sample_list = ["alphabets/{}_500x500.png".format(
            each_sample) for each_sample in sample_list]
        sample_list = enumerate(sample_list)

        print(question_letter)
        print(sample_list)
        return render(request, 'game.html', {"question_letter": question_letter, "sample_list": sample_list})

@csrf_exempt
def game_2(request):
    if request.method == 'GET':
        # all_data = Files.objects.all()

        ABC = string.ascii_uppercase
        list_of_ABC = list(ABC)

        # sampling with replacement
        # k = number of items to select
        question_letter = random.choices(list_of_ABC, k=1)
        sample_list = random.choices(list_of_ABC, k=3)
        sample_list.append(question_letter[0])
        print(question_letter)
        print(sample_list)
        question_letter = "alphabets/{}_500x500.png".format(
            question_letter[0])
        sample_list = ["alphabets/{}_500x500.png".format(
            each_sample) for each_sample in sample_list]
        sample_list = enumerate(sample_list)

        print(question_letter)
        print(sample_list)
        return render(request, 'game_2.html', {"question_letter": question_letter, "sample_list": sample_list})


def search(request):
    if 'filename' in request.GET:
        filename = request.GET['filename']
        datafile = Files.objects.filter(name=filename)
        count = Files.objects.filter(name=filename).count()
        # print(datafile.values_list())
        return render(request, 'search.html', {'data': datafile, 'filename': filename, 'count': count})
