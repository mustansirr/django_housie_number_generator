from django.shortcuts import render
import random


def home(request):
        list=[]
        for i in range(1):
          r = random.randint(1,90)
          if r not in list:
              list.append(r)
        return render(request,"generator/home.html", {'home':list})
