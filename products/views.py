from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import Product
from django.utils import timezone



def home(request):
    return render(request, "home.html")


@login_required(login_url='/accounts')
def create(request):
    # print(request.POST)
    # print(request.FILES)
    if request.method == 'POST':
        if request.POST['title'] + request.POST['url'] + request.POST['body'] :
            product = Product()
            product.title = request.POST['title']
            product.body = request.POST['body']
            product.url = request.POST['url']
            product.icon = request.FILES['icon']
            product.image = request.FILES['image']
            product.pub_date = timezone.datetime.now()
            product.hunter = request.user
            product.save()
            return redirect('products')
        else:
            return render(request, "create.html", {'error': 'Please provide all the fields in the form'})

    return render(request, "create.html")


def products(request):
    return render(request, "products.html")