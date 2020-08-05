from django.shortcuts import render, redirect, get_object_or_404
from .models import Designer

# Create your views here.
def home(request):
    designers = Designer.objects.all()
    return render(request, 'home.html', {'designers' : designers})

def introduce(request):
    return render(request, 'introduce.html')

def detail(request, designer_id):
    designer = get_object_or_404(Designer, pk=designer_id)
    return render(request, 'detail.html', {'designer' : designer})

def new(request):
    return render(request, 'new.html')

def create(request):
    if request.method == 'POST':
        post = Designer()
        if 'image' in request.FILES:
            post.image = request.FILES['image']
            post.name = request.POST['name']
            post.adress = request.POST['adress']
            post.description = request.POST['description']
        
        post.save()

        return redirect('detail', post.id) # 같은 의미 ('profile/'+str(pst.id))