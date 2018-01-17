from django.http import HttpResponse, Http404
#from django.template import loader
from django.http import HttpResponseRedirect
import json
from django.views.decorators.csrf import csrf_exempt
from .forms import UserForm
from django.shortcuts import render,get_object_or_404
from . models import Product,ID,ShopManager,Salesperson,Receiptionist,InventoryManager,Manager_notification
import datetime
from django.http import JsonResponse

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserForm()

    return render(request, 'ok/login.html', {'form': form})


def index(request):
    all_products=Product.objects.all()
   # template = loader.get_template('ok/showproducts.html')

    context = {
        'all_product': all_products,
    }
    return render(request, 'ok/table.html', context)
@csrf_exempt
def sort(request):

    sorttype = request.POST['sort']
    print(sorttype)
    if sorttype == 'name':
        all_products = Product.objects.order_by('pro_name')
    elif sorttype == 'quantity':
        all_products = Product.objects.order_by('qty')
    elif sorttype == 'id':
        all_products = Product.objects.all()
    context = {
        'all_product': all_products,
    }
    return render(request, 'ok/sort.html', context)

def search(request,produ):
    product=Product.objects.get(pk=produ)
    print(produ)
    return render(request, 'ok/search.html', {'product': product})

    #return HttpResponse("<h1>"+ product.pro_name + "</h1>"+)


def detail(request,product_id):
    product=get_object_or_404(Product,pk=product_id)
    return render(request, 'ok/detail.html', {'product': product})

    #return HttpResponse("<h1>"+ product.pro_name + "</h1>"+)

def loginpage(request):
    return render(request, 'ok/login.html')

@csrf_exempt
def login_next(request):
    if(request.method=='POST'):

        x = json.loads(request.body)
        print("hello")
       # hello = 'Hello world\n'
        #print(hello)
        prod = get_object_or_404(Product, pk=int(x[0]['pro']))
        abc = float(x[1]['qty']) * float(prod.price)
        context = {
             'id': prod.id,
             'name': prod.pro_name,
             'qnty': x[1]['qty'],
             'price': prod.price,
             'total': abc
             }
        print(x[0]['pro'])
        print(x[1]['qty'])
        print(abc)
        json_object= {'key':json.dumps(context)}
        return JsonResponse(json_object)
       # return render(request, 'ok/login__next.html')
    return render(request, 'ok/login__next.html')


def addRow(request):
    prod = get_object_or_404(Product, pk=int(request.POST['Product Id']))
    qty = int(request.POST['Quantity'])
    context = {
        'pro': prod.price,
        'qty' : qty,
    }
    abc = int(prod.qty) - qty
    prod.qty = str(abc)
    prod.save()
    return render(request, 'ok/a.html', context)


def home(request):
    try:
        user = ID.objects.get(username=request.POST['username'])
    except(KeyError,ID.DoesNotExist):
        return HttpResponse("ID does not exist.")

    if user.password != request.POST['password']:
        return HttpResponse("Incorrect password.")

    else:
        context = {
            'name': request.POST['username'],
        }

        usertype=request.POST['option']

        if user.type != usertype:
            return HttpResponse("Employee type mismatch.")

        if usertype=='InventoryManager':
            return render(request, 'ok/InventoryManager_Home.html', context)
        elif usertype=='ShopManager':
            return render(request, 'ok/ShopManager_Home.html', context)
        elif usertype =='Salesperson':
            return render(request, 'ok/Salesperson_Home.html', context)
        else:
            return render(request, 'ok/Receiptionist_Home.html', context)