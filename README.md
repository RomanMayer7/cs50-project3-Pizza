# Project 3

Web Programming with Python and JavaScript

Project Name :Pizza:"Restaurant Management System"

Project Objectives
----------------------------------------------------------------------------------------

*Become more comfortable with Django.
*Gain experience with relational database design.
*Built Management System for Pizza Restaurant

Project Description
----------------------------------------------------------------------------------------

This "Restaurant Management System" is designed for Clients and Restaraunt Managers
It enables the clients to make orders,based on Restaraunt Menu.After they Place their Order:they can Track order's status.
Each client have Shopping Cart to place multiple orders.The Order can be removed from Shopping Cart if client changes his Mind later.
The new clients must create account in order to see  the Menu and make orders
The returning clients must pass authentication to log in.
The restoraunt managers which have Admin Permissions can log in their "superuser" 
Account there they have one Additional feature on Navigation Bar:"Manage Orders"
There they can see All Orders,change their status and remove them.
----------------------------------------------------------------------------------------

Project Structure
----------------------------------------------------------------------------------------
In [Project's Main Folder] there are:

*'db.sqlite3' file wich is used for Database Storage
*'manage.py' is used to Run Django Server and start our WEB Application
*'README.md' is current file where i describe my Project
*'requirements.txt' contains description
of all essential modules to be installed in order to run the App

In [mysite] subfolder there are:
'settings.py' ,'urls'.py '_init_.py','wsgi.py'
responsibal gor all global project level related info

*In 'urls'.py there  are routes for application level local
urls :path('',include('pizza.urls'))
as  well  for  admin maagement site:
path('admin/', admin.site.urls)

*'settings.py' have all properties of project
such Language Info and Codes

*A  Path for Database Connection(in our case we use a local lightweight version of SQL:"SQLite3")

*It also includes the information regarding all the applications installed in Project:
including our "PIZZA" Application 
and ADMIN SITE APP

INSTALLED_APPS = [
    'pizza.apps.PizzaConfig',
    'django.contrib.admin',
    'django.contrib.auth',
............]

[pizza] subfolder contains all application specific data

*'models.py' contains all models for data types ,used in our  Restoraunt Data Model :"Orders", food types:"Pizzas","Subs" etc...

*'views.py' contains all application  BackEnd logic written in Python
'Views' or Functions for all different routes the user can take when using the App
It prepares all the  nescessary data to represent it  inside different HTML Templates
when user chooses his route.

*'urls.py' listss all possible routes presented in Application with references to all appropriate views for each of them

*'admin.py' contains all registrations for different DB models  reserved for Admin Management Site

[templates] subfolder conatains all HTML Template files for every 'view' of application:
*'base.html' is main template from which all templates inherits
*'index.html' for Menu, 
and all the rest: 'additem.html','additem2.html','additem3.html','login.html','manageorders.html','orders.html','trackorders.html'

[static] subfolder contains all images and stylesheet files used in App

[migrations] subfolder contains all migration 'py' files  which are  corresponds  to changes preformed in App's Datatabase 

Functionalities and their Implementation
----------------------------------------------------------------------------------------

[Menu]: Our web application  supports all of the available menu items for Pinnochio’s Pizza & Subs 
(a popular pizza place in Cambridge).The models which corresponds to menu's items  are stored in pizza/models.py 
,as well the migration files placed in pizza/migrations folder 

Database  populated with menu items through the Shell Console with following command list
----------------------------------------------------------------------------------------
t=Extra(name='Pepperoni') t.save() t=Extra(name='Sausage') t.save() t=Extra(name='Mushrooms')
t.save() t=Extra(name='Onions') t.save() t=Extra(name='Ham') t.save() 
t=Extra(name='Canadian Bacon') t.save() t=Extra(name='Pineapple')
t.save() t=Extra(name='Eggplant') t.save() t=Extra(name='Tomato & Basil') t.save()
t=Extra(name='Green Peppers') t.save() t=Extra(name='Hamburger') t.save()
t=Extra(name='Spinach') t.save() t=Extra(name='Artichoke') t.save() t=Extra(name='Buffalo Chicken')
t.save() t=Extra(name='Barbecue Chicken') t.save() t=Extra(name='Anchovies') t.save()
t=Extra(name='Black Olives') t.save() t=Extra(name='Fresh Garlic') t.save()
t=Extra(name='Zucchini') t.save()

a=Addition(name='Mushrooms') a.save()
a=Addition(name='Green Peppers') a.save()
a=Addition(name='Onions') a.save()

psl=Pastasalad(name='Garden Salad',p_class='salad',price=6.25)
psl.save()
psl=Pastasalad(name='Greek Salad',p_class='salad',price=8.25)
psl.save()
psl=Pastasalad(name='Antipasto',p_class='salad',price=8.25)
psl.save()
psl=Pastasalad(name='Salad w/Tuna',p_class='salad',price=8.25)
psl.save()
psl=Pastasalad(name='Baked Ziti w/Mozzarella',p_class='pasta',price=6.50)
psl.save()
psl=Pastasalad(name='Baked Ziti w/Meatballs',p_class='pasta',price=8.75)
psl.save()
psl=Pastasalad(name='Baked Ziti w/Chicken',p_class='pasta',price=9.75)
psl.save()

d=Dinner(name='Garden Salad',s_price=35.00,l_price=60.00)
d.save()
d=Dinner(name='Greek Salad',s_price=45.00,l_price=70.00)
d.save()
d=Dinner(name='Antipasto',s_price=45.00,l_price=70.00)
d.save()
d=Dinner(name='Baked Ziti',s_price=35.00,l_price=60.00)
d.save()
d=Dinner(name='Meatball Parm',s_price=45.00,l_price=70.00)
d.save()
d=Dinner(name='Chicken Parm',s_price=45.00,l_price=80.00)
d.save()

p=Pizza(name='Cheese',p_class='Regular',num_extras=0,s_price=12.20,l_price=17.45)
p.save()
p=Pizza(name='1 topping',p_class='Regular',num_extras=1,s_price=13.20,l_price=19.45)
p.save()
p=Pizza(name='2 toppings',p_class='Regular',num_extras=2,s_price=14.70,l_price=21.45)
p.save()
p=Pizza(name='3 toppings',p_class='Regular',num_extras=3,s_price=15.70,l_price=23.45)
p.save()
p=Pizza(name='Special',p_class='Regular',num_extras=5,s_price=17.25,l_price=25.45)
p.save()
p=Pizza(name='Cheese',p_class='Sicilian',num_extras=0,s_price=23.45,l_price=37.70)
p.save()
p=Pizza(name='1 item',p_class='Sicilian',num_extras=1,s_price=25.45,l_price=39.70)
p.save()
p=Pizza(name='2 items',p_class='Sicilian',num_extras=2,s_price=27.45,l_price=41.70)
p.save()
p=Pizza(name='3 items',p_class='Sicilian',num_extras=3,s_price=28.45,l_price=43.70)
p.save()
p=Pizza(name='Special',p_class='Sicilian',num_extras=5,s_price=29.45,l_price=44.70)
p.save()


s=Sub(name='Cheese',have_addons=False,s_price=6.50,l_price=7.95)
s.save()
s=Sub(name='Italian',have_addons=False,s_price=6.50,l_price=7.95)
s.save()
s=Sub(name='Ham + Cheese',have_addons=False,s_price=6.50,l_price=7.95)
s.save()
s=Sub(name='Meatball',have_addons=False,s_price=6.50,l_price=7.95)
s.save()
s=Sub(name='Tuna',have_addons=False,s_price=6.50,l_price=7.95)
s.save()
s=Sub(name='Turkey',have_addons=False,s_price=7.50,l_price=8.50)
s.save()
s=Sub(name='Chicken Parmigiana',have_addons=False,s_price=7.50,l_price=8.50)
s.save()
s=Sub(name='Eggplant Parmigiana',have_addons=False,s_price=6.50,l_price=7.95)
s.save()
s=Sub(name='Steak',have_addons=False,s_price=6.50,l_price=7.95)
s.save()
s=Sub(name='Steak + Cheese',have_addons=True,s_price=6.95,l_price=8.50)
s.save()
s=Sub(name='Sausage, Peppers & Onions',have_addons=False,s_price=0,l_price=8.50)
s.save()
s=Sub(name='Hamburger',have_addons=False,s_price=4.60,l_price=6.95)
s.save()
s=Sub(name='Cheeseburger',have_addons=False,s_price=5.10,l_price=7.45)
s.save()
s=Sub(name='Fried Chicken',have_addons=False,s_price=6.95,l_price=8.50)
s.save()
s=Sub(name='Veggie',have_addons=False,s_price=6.95,l_price=8.50)
s.save()
----------------------------------------------------------------------------------------
[Adding Items]: Using Django Admin, site administrators (restaurant owners) able to add,update, and remove items on the menu 
through Admin UI with Admin App installed on Project via localhost\admin route

[Registration, Login, Logout]: Site users (customers) are  able to register for our web application with
 a username, password,first name, last name, and email address.
Implemented via extension of 'UserCreationForm' inside SignUpForm with addition
of apropriate fields.
Customers  are be able to log in and log out of your website.
This functionalities are implemented through
 def signup(request),'def login_view(request)' and 'def logout_view(request) '
  inside 'views.py'and rendered inside 'login.html' template

[Shopping Cart]: Once logged in, users can see a representation of the restaurant’s menu, where they can add items
 (along with toppings or extras, if appropriate) to their virtual “shopping cart.” Implemented with  different views 
 for different types of items:def addpizzaitem(request, pizza_id),def addsubitem(request, sub_id),
def addinneritem(request, din_id)  for items with different sub properties
like Size and additions AND with
def add_order(request,product_id) ,def add_order2(request,product_id)
def add_order3(request,product_id),def add_order4(request,product_id) they
are added to Cart.
This rendered through Templates: additem.html,additem2.html,additem3.html
The contents of the shopping will be saved even if a user
closes the window, or logs out and logs back in again.Implemented through saving the
added item to Database with 'preorder' status

[Placing an Order]: Once there is at least one item in a user’s Shopping Cart, they are be able to place an order,
 whereby the user is asked to confirm the items in the shopping cart, and the total  before placing an order.User can remove items from
the Shopping Card if he changes his mind.functionality is  Implemented inside:('def removeorder(request)')
can be called through AJAX HTTPRequest through JQuery function
"$(".remove").on('click', function(){.....});" in "script" snippet placed inside orders.html
 Order Placement functionality is  Implemented through 'def placeorder(request)'inside 'views.py' 


[Viewing Orders+Personal Touch]: Site administrators have access to a page where they can view any orders that have already been placed.site administrators can mark orders as complete and allowing users to see the status of their pending or completed orders.Implemented through checking if the current user is admin("superuser") of DJANGO and if so adding one additional Tab to NavBAr:"Manage Orders"
This Check occurs inside DJango page template and appropriate content is rendered
according Check's Result."Manage Orders" functionality implemented through
'def manageorders(request)'+'manageorders.html'

--------------------------------------------------------------------------
by Roman Meyerson @ 2019/Started :Feb 21, 2019-Finished:Feb 28, 2019
    
