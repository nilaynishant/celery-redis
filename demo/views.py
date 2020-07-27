from django.shortcuts import render
from django.http import HttpResponse
from demo.tasks import add


class image:
    def __init__(self, a):
        ## private varibale or property in Python
        self.__a = a

    ## getter method to get the properties using an object
    def get_a(self):
        return self.__a

    ## setter method to change the value 'a' using an object
    def set_a(self, a):
        self.__a = a


# Create your views here.
def index(request):
    result = add.delay(7, 8)
    print(result.get(timeout=1))
    return HttpResponse("Hello, world. You're at the polls index.")
