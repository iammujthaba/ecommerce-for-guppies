from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from . models import Category, Product
from django.core.paginator import Paginator,EmptyPage,InvalidPage

# Create your views here.

# def index(request):
#     return render(request,'index.html')

def allProdCat(request, c_slug = None):
    c_page = None
    offer = None
    products_list = None
    # 4 - tis "if" condition work when "product_by_category" path is call "allProdCat" function [its hpappaning]
    # and "c_slug" change its valure from "None" to catogory url (go to "get_object_or_404")
    if c_slug != None:
        # 5 - tis "get_object_or_404" function return catogory url corresponding Catogory method name (go to 6)
        c_page = get_object_or_404(Category, slug = c_slug)
        # 6 - tis line of code take all product listed under, user cliked catogory (done.)
        products_list = Product.objects.all().filter(category = c_page, available = True)
    else:
        products_list = Product.objects.all().filter(available = True)


    paginator = Paginator(products_list,6)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1

    try:
        products = paginator.page(page)
    except (InvalidPage,EmptyPage):
        products = paginator.page(paginator.num_pages)
        
    offer = Product.objects.filter(old_price__gt=0)

    return render(request,'category.html',{'category':c_page, 'products':products, 'offer':offer})


def proDetail(request, c_slug, product_slug):
    try:
        product = Product.objects.get(category__slug = c_slug, slug = product_slug)
    except Exception as e:
        raise e
    
    

    if c_slug:
        c_page = get_object_or_404(Category, slug = c_slug)
        products_list = Product.objects.all().filter(category = c_page, available = True)

    paginator = Paginator(products_list,5)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1

    try:
        products = paginator.page(page)
    except (InvalidPage,EmptyPage):
        products = paginator.page(paginator.num_pages)


    return render(request, 'product.html',{'product':product,'products':products})



def allProductListing(request):
    products_list = Product.objects.all().filter(available = True)

    paginator = Paginator(products_list,14)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1

    try:
        products = paginator.page(page)
    except (InvalidPage,EmptyPage):
        products = paginator.page(paginator.num_pages)
        
    return render(request,'shop.html',{'products':products})

def offerProductListing(request):
    products_list = Product.objects.filter(old_price__gt=0)

    paginator = Paginator(products_list,14)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1

    try:
        products = paginator.page(page)
    except (InvalidPage,EmptyPage):
        products = paginator.page(paginator.num_pages)
        
    return render(request,'shop.html',{'products':products})