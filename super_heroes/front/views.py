from django.shortcuts import render, redirect
from .models import SuperHeroe, SuperPoder
from .forms import HeroeForm, PoderForm

# Create your views here.
def home(request):  
    return render(request,"home.html")  


def heroeList(request):  
    heroes = SuperHeroe.objects.all()  
    return render(request,"heroe-list.html",{'heroes':heroes})  

def heroeCreate(request):  
    if request.method == "POST":  
        form = HeroeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('heroe-list')  
            except:  
                pass  
    else:  
        form = HeroeForm()  
    return render(request,'heroe-create.html',{'form':form})  

def heroeUpdate(request, id):  
    heroe = SuperHeroe.objects.get(id=id)
    form = HeroeForm(
        initial={
            'nombre': heroe.nombre, 
            'alias': heroe.alias, 
            'edad': heroe.edad, 
            'sexo': heroe.sexo,
            'poder': heroe.poder.nombre
        })
    if request.method == "POST":  
        form = HeroeForm(request.POST, instance=heroe)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('/heroe-list')  
            except Exception as e: 
                pass    
    return render(request,'heroe-update.html',{'form':form})  

def heroeDelete(request, id):
    heroe = SuperHeroe.objects.get(id=id)
    try:
        heroe.delete()
    except:
        pass
    return redirect('heroe-list')

# Create your views here.
def poderList(request):  
    poders = SuperPoder.objects.all()  
    return render(request,"poder-list.html",{'poders':poders})  

def poderCreate(request):  
    if request.method == "POST":  
        form = PoderForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('poder-list')  
            except:  
                pass  
    else:  
        form = PoderForm()  
    return render(request,'poder-create.html',{'form':form})  

def poderUpdate(request, id):  
    poder = SuperPoder.objects.get(id=id)
    form = PoderForm(
        initial={
            'nombre': poder.nombre, 
            'descripcion': poder.descripcion
        })
    if request.method == "POST":  
        form = PoderForm(request.POST, instance=poder)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('/poder-list')  
            except Exception as e: 
                pass    
    return render(request,'poder-update.html',{'form':form})  

def poderDelete(request, id):
    poder = SuperPoder.objects.get(id=id)
    try:
        poder.delete()
    except:
        pass
    return redirect('poder-list')