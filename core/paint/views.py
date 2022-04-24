# Create your views here.

from secrets import choice
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Files
from django.views.decorators.csrf import csrf_exempt
import json
import random
from random import shuffle

import string


@csrf_exempt
def paint(request):
    if request.method == 'GET':
        # when  GET method is called from the HTML this part of  code will run and render paint.html
        return render(request, 'paint.html')
    elif request.method == 'POST':
        # when the user press on the save butthon this part of code runs and save the canves details into db
        filename = request.POST['save_fname']
        data = request.POST['save_cdata']
        image = request.POST['save_image']
        file_data = Files(name=filename, image=data, canvas_image=image)
        file_data.save()
        return HttpResponseRedirect('/')


@csrf_exempt
def files(request):
    if request.method == 'GET':
        # when user click on the history butthon all the save paint letter are going to shown to on the files.html file
        all_data = Files.objects.all()
        return render(request, 'files.html', {'files': all_data})


@csrf_exempt
def game(request):
    if request.method == 'GET':
        """ in this part of code i have writen the login of game. """

        # first step write all ABC. A to Z
        ABC = string.ascii_uppercase

        # convert string ABC into list ABC for example ['A','B','C']
        list_of_ABC = list(ABC)

        # pick 1 rendom letter from the list of ABC list
        question_letter = random.choices(list_of_ABC, k=1)

        # pick 3 rendom letter from the list of ABC list.
        sample_list = random.choices(list_of_ABC, k=3)

        # append the question Letter into the choices list.
        sample_list.append(question_letter[0])

        # Now this part is important i have added extra string to the ABC use this pattern i can access each ABC images in HTML
        question_letter = "alphabets/{}_500x500.png".format(
            question_letter[0])
        sample_list = ["alphabets/{}_500x500.png".format(
            each_sample) for each_sample in sample_list]

        # this part shuffle the list
        shuffle(sample_list)
        sample_list = enumerate(sample_list)

        return render(request, 'game.html', {"question_letter": question_letter, "sample_list": sample_list})


@csrf_exempt
def game_2(request):
    if request.method == 'GET':

        ABC = string.ascii_uppercase
        list_of_ABC = list(ABC)

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
        # this part of code search the file in db and send it to search.HTML file
        filename = request.GET['filename']
        datafile = Files.objects.filter(name=filename)
        count = Files.objects.filter(name=filename).count()
        return render(request, 'search.html', {'data': datafile, 'filename': filename, 'count': count})
