from django.shortcuts import render,redirect
from Testapp.form import MovieForm
from Testapp.models import Movie

# Create your views here.

def index_views(request):
    return render(request,'html/Index.html')
def add_movie_views(request):
    form=MovieForm()
    if request.method=='POST':
        form=MovieForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return index_views(request)
    return render(request,'html/Addmovie.html',{'form':form})


def list_movie_views(request):
    movie_list=Movie.objects.all()
    return render(request,'html/Listmovie.html',{'list':movie_list})


def update_views(request,id):
    movie=Movie.objects.get(id=id)
    if request.method=='POST':
        form=MovieForm(request.POST,instance=movie)
        if form.is_valid():
            form.save(commit=True)
        return redirect('/listmovies')
    return render(request,'html/edit.html',{'movie':movie})



def delete_views(request,id):
    movie=Movie.objects.get(id=id)
    movie.delete()
    return redirect('/listmovies')
