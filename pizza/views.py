from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse

from django.views.decorators.csrf import csrf_exempt
from .models import Pizza,Extra,Order,Sub,Addition,Pastasalad,Dinner

from django.shortcuts import redirect

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
 first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
 last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
 email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
 class Meta:
    model = User
    fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        form = SignUpForm()
        return render(request, "pizza/login.html", {"form":form,"message": None})
    context = {
        "user": request.user,
        "regular_pizzas": Pizza.objects.filter(p_class="Regular"),
        "sicilian_pizzas": Pizza.objects.filter(p_class="Sicilian"),
        "toppings":Extra.objects.all(),
        "subs": Sub.objects.all(),
        "dinners":Dinner.objects.all(),
        "pastas":Pastasalad.objects.filter(p_class="pasta"),
        "salads":Pastasalad.objects.filter(p_class="salad")
    }
    return render(request, "pizza/index.html", context)

def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        form = SignUpForm()
        return render(request, "pizza/login.html",{"form":form,"message": "Invalid credentials."})

def logout_view(request):
    logout(request)
    form = SignUpForm()
    return render(request, "pizza/login.html",{"form":form,"message": "Invalid credentials."})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
     form = SignUpForm()
     return render(request, "pizza/login.html",{"form":form,"message": "Invalid Sign UP Attempt."})



def addpizzaitem(request, pizza_id):
    product=Pizza.objects.filter(id=pizza_id)
    print(product[0].num_extras) 
    context = {
          "user": request.user,
          "product":product[0],
          "small":product[0].s_price,
          "large":product[0].l_price,
          "extras":Extra.objects.all(),
          "extras_num": range(0, product[0].num_extras)  
    }
    return render(request, "pizza/additem.html", context)

def addsubitem(request, sub_id):
    product=Sub.objects.filter(id=sub_id) 
    context = {
          "user": request.user,
          "product":product[0],
          "small":product[0].s_price,
          "large":product[0].l_price,
          "additions":Addition.objects.all(),
          "have_adds":product[0].have_addons, 
    }
    return render(request, "pizza/additem2.html", context)

def addinneritem(request, din_id):
    product=Dinner.objects.filter(id=din_id) 
    context = {
          "user": request.user,
          "product":product[0],
          "small":product[0].s_price,
          "large":product[0].l_price,     
    }
    return render(request, "pizza/additem3.html", context)

#defining function to add order of type Pizza to Orders
def add_order(request,product_id):
    #Getting user info
    user=request.user
    order_owner=""+user.first_name+" "+user.last_name

    #determining order's  item size by comparing the prices for small and large item
    p_price = float(request.POST["size"])
    product=Pizza.objects.filter(id=product_id)
    if(p_price<product[0].l_price):
        p_size="Small"
    else:
        p_size="Large"    
    #building order's name for Pizza item,composed from pizza name and pizza class
    pizza_name=product_name=product[0].name
    pizza_class=product[0].p_class
    product_name=""+pizza_class+" "+pizza_name+" Pizza"
    #searching for all "toppings" from POST request and appending them to array
    topping_list=[]
    for extr in request.POST:
       if extr.startswith("topping"):
        ex=str(request.POST[extr])
        topping_list.append(ex)

    #Add order to 'Orders' Table with status="preorder" 
    o=Order(name=product_name,size=p_size,extras=topping_list,price=p_price,owner=order_owner,status="preorder")
    o.save()
    #Redirect to this user Orders Page   
    return HttpResponseRedirect(reverse("index"))

#defining function to add order of type Sub to Orders
def add_order2(request,product_id):
    #Getting user info
    user=request.user
    order_owner=""+user.first_name+" "+user.last_name

    #determining order's  item size by comparing the prices for small and large item
    p_price = float(request.POST["size"])
    product=Sub.objects.filter(id=product_id)
    if(p_price<product[0].l_price):
        p_size="Small"
    else:
        p_size="Large"
    #building order's name for Sub item
    sub_name=product_name=product[0].name
    product_name=""+sub_name+" Sub"
    #searching for all "additions" from POST request and appending them to array
    addition_list=[]
    addition_counter=0
    for extr in request.POST:
       if extr.startswith("addition"):
        addition_list.append(request.POST[extr])
        addition_counter=addition_counter+1#counting additions
       elif extr.startswith("extra_cheese"):
        addition_list.append(request.POST[extr])
        addition_counter=addition_counter+1#counting additions

    #Computing hte ultimate price for the Order
    p_price=p_price+addition_counter*0.50
    #Add order to 'Orders' Table with status="preorder"
    o=Order(name=product_name,size=p_size,extras=addition_list,price=p_price,owner=order_owner,status="preorder")
    o.save()
    #Redirect to this user Orders Page   
    return HttpResponseRedirect(reverse("index"))

#defining function to add order of type Dinner to Orders
def add_order3(request,product_id):
    #Getting user info
    user=request.user
    order_owner=""+user.first_name+" "+user.last_name

     #determining order's  item size by comparing the prices for small and large item
    p_price = float(request.POST["size"])
    product=Dinner.objects.filter(id=product_id)
    if(p_price<product[0].l_price):
        p_size="Small"
    else:
        p_size="Large"
    #building order's name for Sub item
    dnr_name=product[0].name
    product_name=""+dnr_name+" Dinner Platter"
    #Add order to 'Orders' Table with status="preorder"
    o=Order(name=product_name,size=p_size,extras="",price=p_price,owner=order_owner,status="preorder")
    o.save()
    #Redirect to this user Orders Page   
    return HttpResponseRedirect(reverse("index"))

#defining function to add order of type Pasta or Salad to Orders
def add_order4(request,product_id):
    #Getting user info
    user=request.user
    order_owner=""+user.first_name+" "+user.last_name

    #building order's name for Pasta or Salad item
    product=Pastasalad.objects.filter(id=product_id)
    psl_name=product[0].name
    product_name=""+psl_name
    #product price
    p_price=psl_name=product[0].price
    #Add order to 'Orders' Table with status="preorder"
    o=Order(name=product_name,size="Standart",extras="",price=p_price,owner=order_owner,status="preorder")
    o.save()
    #Redirect to this user Orders Page   
    return HttpResponseRedirect(reverse("index"))

def orders(request):
     #Show all orders for specific user ,with status='preorder'
     user=request.user
     order_owner=""+user.first_name+" "+user.last_name
     your_orders=Order.objects.filter(owner=order_owner,status="preorder")
     print(your_orders)
     if your_orders.exists():
      #print("EXISSSST")
      extras_lists=[]
      total=0#Total price of all orders for a user
      for x in your_orders:
       total=total+x.price
       print(x)
       extrs=x.extras # recieveing extras list from table row as string :"['topping1', 'topping2',...]"
       print(extrs)
       substr=extrs[1:-1] #remove first and last chars from the string:"'topping1', 'topping2',..."
       print(substr)
       extr_array=substr.split(",")#break string into tokens by "," delimiter and store into array 
       print(extr_array)
       extras_lists.append(extr_array)

      mylist = zip(your_orders, extras_lists)
      context = {"my_list":mylist,"order_total":total,"orders_owner":order_owner}
     else :
      context = {"my_list":[],"order_total":0,"orders_owner":order_owner}
     #send data to render them inside orders.html
     return render(request, "pizza/orders.html",context)

def placeorder(request):
    #Change status of all user's entries from table Orders to "Order Placed"
    user=request.user
    order_owner=""+user.first_name+" "+user.last_name
    your_orders=Order.objects.filter(owner=order_owner,status="preorder")
    for o in your_orders:
       print(o)
       o.status="Order Placed"
       o.save()

    return HttpResponseRedirect(reverse("index"))

@csrf_exempt
def removeorder(request):
   order_id = int(request.POST["order_number"])
   print("Number of Order to be  removed:")
   print(order_id)
   order=Order.objects.filter(id=order_id)
   order[0].delete()
   return HttpResponse(status=204)

def trackorders(request):
     #Show all orders for specific user ,with status='preorder'
     user=request.user
     order_owner=""+user.first_name+" "+user.last_name
     your_orders = Order.objects.filter(owner=order_owner,status="Order Placed") |Order.objects.filter (owner=order_owner,status="Cooking")|Order.objects.filter (owner=order_owner,status="Preparing")|Order.objects.filter (owner=order_owner,status="Ready")
     if your_orders.exists():
      #your_orders=Order.objects.filter(owner=order_owner,status="preorder")
      extras_lists=[]
      total=0#Total price of all orders for a user
      for x in your_orders:
       total=total+x.price
       print(x)
       extrs=x.extras # recieveing extras list from table row as string :"['topping1', 'topping2',...]"
       print(extrs)
       substr=extrs[1:-1] #remove first and last chars from the string:"'topping1', 'topping2',..."
       print(substr)
       extr_array=substr.split(",")#break string into tokens by "," delimiter and store into array 
       print(extr_array)
       extras_lists.append(extr_array)
      mylist = zip(your_orders, extras_lists)
      #send data to render them inside orders.html
      context = {"my_list":mylist,"order_total":total,"orders_owner":order_owner}
     else:
      context = {"my_list":[],"order_total":0} 
     return render(request, "pizza/trackorders.html",context)

def manageorders(request):
     #all_orders=Order.objects.all()
     all_orders=Order.objects.exclude(status="preorder")
     if all_orders.exists():
      extras_lists=[]
      total=0#Total price of all orders for a user
      for x in all_orders:
       total=total+x.price
       print(x)
       extrs=x.extras # recieveing extras list from table row as string :"['topping1', 'topping2',...]"
       print(extrs)
       substr=extrs[1:-1] #remove first and last chars from the string:"'topping1', 'topping2',..."
       print(substr)
       extr_array=substr.split(",")#break string into tokens by "," delimiter and store into array 
       print(extr_array)
       extras_lists.append(extr_array)
      mylist = zip(all_orders, extras_lists)
      context = {"my_list":mylist,"order_total":total}
     else :
      context = {"my_list":[],"order_total":0}
     #send data to render them inside orders.html
     return render(request, "pizza/manageorders.html",context)

def changestatus(request,order_id):
   status = str(request.POST["status"])
   print(status)
   order=Order.objects.filter(id=order_id)
   o=order[0]
   o.status=status
   o.save()
   return HttpResponseRedirect(reverse("manageorders"))
