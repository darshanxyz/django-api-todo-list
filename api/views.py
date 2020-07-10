from django.shortcuts import render
from django.http import HttpResponse


def get_all_todos(request):
    return HttpResponse("API to get all the todo items")
