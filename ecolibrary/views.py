from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from .models import NationalPark, NaturalMonument, STATES


class Home(TemplateView):
    template_name = "ecolibrary/home.html"

class NationalParkListView(ListView):
    model = NationalPark
    template_name = "ecolibrary/ecolist.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["states"] = STATES
        return context
    
    def get_queryset(self):
        national_parks = NationalPark.objects.all()
        try:
            text_search = self.request.GET['text_search']
            national_parks = national_parks.filter(name__contains=text_search)
        except Exception as e: 
            # print(e)
            pass

        try:
            state_search = self.request.GET['state_search']
            national_parks = national_parks.filter(state=int(state_search))
        except Exception as e: 
            #print(e)     
            pass

        return national_parks

class NaturalMonumentListView(ListView):
    model = NaturalMonument
    template_name = "ecolibrary/ecolist.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["states"] = STATES
        return context
    
    def get_queryset(self):
        natural_monuments = NaturalMonument.objects.all()
        try:
            text_search = self.request.GET['text_search']
            natural_monuments = natural_monuments.filter(name__contains=text_search)
        except Exception as e: 
            # print(e)
            pass

        try:
            state_search = self.request.GET['state_search']
            natural_monuments = natural_monuments.filter(state=int(state_search))
        except Exception as e: 
            # print(e)     
            pass

        return natural_monuments

class NationalParkDetailView(DetailView):
    model = NationalPark
    template_name = "ecolibrary/ecosite.html"

class NaturalMonumentDetailView(DetailView):
    model = NaturalMonument
    template_name = "ecolibrary/ecosite.html"

