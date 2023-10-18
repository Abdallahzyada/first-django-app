from django.shortcuts import render
from django.http.response import HttpResponse,HttpResponseRedirect
from .models import Trainee
from django.views import View
from .forms import *
from tracks.models import *

# Create your views here.


def traineeList(request):
    context = {}
    trainees = Trainee.objects.all()
    search_query = request.GET.get('search')
    if search_query:
        trainees = trainees.filter(name__icontains=search_query)

    context['trainees'] = trainees
    return render(request, 'trainee/list.html', context)


class TraineeAdd(View):
    def get(self,req):
        context = {}
        context['tracks'] = Track.objects.all()
        context['form']=addtraineeform()
        return render(req, 'trainee/studentAdd.html', context)

    def post(self,req):
        form=addtraineeform(req.POST)
        if(form.is_valid()):
            name = req.POST['name']
            trackid = req.POST['tracks']

            Trainee.objects.create(name=name, track=Track.objects.get(id=trackid))
            return HttpResponseRedirect('/Trainee/list')
        else:
            context={
                'form': form,'MSG':form.errors}
            return render(req, 'trainee/studentAdd.html', context)


class TraineeUpdate(View):
    def get(self, request,id):
        trainee = Trainee.objects.get(id=id)
        form = addtraineeform(initial={'name': trainee.name, 'tracks': trainee.track.id})
        context = {
            'form': form,
            'trainee': trainee,
            'tracks': Track.objects.all()
        }
        return render(request, 'trainee/update.html', context)

    def post(self, request, id):
        trainee = Trainee.objects.get(id=id)
        form = addtraineeform(request.POST)
        if form.is_valid():
            trainee.name = form.cleaned_data['name']
            trainee.track = Track.objects.get(id=form.cleaned_data['tracks'])
            trainee.save()
            return HttpResponseRedirect('/Trainee/list')
        context = {
            'form': form,
            'trainee': trainee,
            'tracks': Track.objects.all()
        }
        return render(request, 'trainee/update.html', context)


def traineeDelete(request,id):
    Trainee.objects.filter(id=id).delete()
    return  HttpResponseRedirect('/Trainee/list')
