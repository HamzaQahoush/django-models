from django.shortcuts import render
from django.views.generic import TemplateView , ListView , DetailView
from .models import Snack

# Create your views here.
# class HomeView (TemplateView): 
#     template_name="home.html"  


class snackView (ListView): 
    template_name="snack_list.html"  
    model = Snack


class snack_Detail_View (DetailView): 
    template_name="snacks_detail.html"  
    model = Snack


