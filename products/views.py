from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import Product
from django.utils import timezone


def home(request):
    a = Product.objects.all()
    return render(request, "home.html", {'allProducts': a})


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


@login_required(login_url='/accounts')
def products(request):
    a = Product.objects.filter(hunter=request.user)
    return render(request, "products.html", {'myProducts': a})


def detail(request, product_id):
    # a = Product.objects.filter(hunter=request.user)
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'productDetail.html', {'product': product})