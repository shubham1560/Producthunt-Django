from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import Product, ProductAttribute
from django.utils import timezone
import random
import string


def home(request):
    a = Product.objects.filter(active=True)
    return render(request, "home.html", {'allProducts': a})


@login_required(login_url='/accounts')
def create(request):
    print(request.POST)
    print(request.FILES)
    if request.method == 'POST':
        if request.POST['title'] + request.POST['url'] + request.POST['body'] :
            product = Product()
            ran = int(''.join([random.choice(string.digits) for n in range(16)]))
            product.title = request.POST['title']
            product.body = request.POST['body']
            product.url = request.POST['url']
            product.icon = request.FILES['icon']
            product.image = request.FILES['image']
            product.pub_date = timezone.datetime.now()
            product.hunter = request.user
            product.id = ran
            product.save()
            return redirect('products')
        else:
            return render(request, "create.html", {'error': 'Please provide all the fields in the form'})

    return render(request, "create.html")


@login_required(login_url='/accounts')
def products(request):
    a = Product.objects.filter(hunter=request.user, active=True)
    return render(request, "products.html", {'myProducts': a})


def detail(request, product_id):
    # a = Product.objects.filter(hunter=request.user)
    product = get_object_or_404(Product, pk=product_id)
    a = ProductAttribute.objects.filter(voter=request.user)
    if a:
        voted = True
    else:
        voted = False
    result = {'product': product, 'voted': voted}
    return render(request, 'productDetail.html', result)


@login_required(login_url='/accounts')
def vote(request, product_id):
    a = ProductAttribute.objects.filter(voter=request.user)
    if a:
        print("Already Given vote")
    else:
        print("Giving your vote")
        # print("Well Inside Function")
        if request.method == 'POST':
            # print("Inside POST")
            product = get_object_or_404(Product, pk=product_id)
            # print(product)
            votes = ProductAttribute()
            votes.id = int(''.join([random.choice(string.digits) for n in range(16)]))
            votes.vote = True
            votes.product = product
            votes.voter = request.user
            votes.voting_time = timezone.datetime.now()
            votes.save()
            # print(votes)
            return detail(request, product_id)
    return detail(request, product_id)