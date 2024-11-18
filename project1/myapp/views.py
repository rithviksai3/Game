from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Detail
import random
# Create your views here.
def index(request):
    if request.method=='POST':
            Choice=request.POST['Choice']
            player_choice=Choice
            options=["rock","paper","scissors"]
            computer_choice=random.choice(options)
            choices={"Computer_choice":computer_choice}
            messages.error(request,choices)
            if player_choice=="rock" and computer_choice=="scissors":
                messages.error(request,'YOU WON')
            elif player_choice=="scissors" and computer_choice=="paper":
                 messages.error(request,'YOU WON')
            elif player_choice=="paper" and computer_choice=="rock":
                 messages.error(request,'YOU WON')
            elif player_choice==computer_choice:
                 messages.error(request,"DRAW")
            else:
                messages.error(request,'YOU LOST')
    return render(request,'index.html')
