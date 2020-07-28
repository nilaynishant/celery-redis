from django.shortcuts import render
from django.http import HttpResponse
from demo.tasks import add
from PIL import Image

# class image:
#     def __init__(self, a):
#         ## private varibale or property in Python
#         self.__a = a

#     ## getter method to get the properties using an object
#     def get_a(self):
#         return self.__a

#     ## setter method to change the value 'a' using an object
#     def set_a(self, a):
#         self.__a = a


# Create your views here.
def index(request,z, x, y):
    result = add.delay(7, 8)
    print(result.get(timeout=1))
    # image = Image.fromarray(result.get(timeout=1))
    # response = image.save('img/png')
    img = Image.fromarray(result.get(timeout=1)).resize((256, 256), Image.NEAREST)
    # serialize to HTTP response
    response = HttpResponse(content_type="image/png")
    img.save(response, "PNG")
    return response
