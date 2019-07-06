from django.urls import path
from . import views

urlpatterns=[
    path("",views.index,name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("signup", views.signup, name="signup"),
    path("add\<int:pizza_id>",views.addpizzaitem, name="addpizzaitem"),
    path("add2\<int:sub_id>", views.addsubitem, name="addsubitem"),
    path("add3\<int:din_id>", views.addinneritem, name="addinneritem"),
    path("add_order\<int:product_id>",views.add_order,name="add_order"),
    path("add_order2\<int:product_id>",views.add_order2,name="add_order2"),
    path("add_order3\<int:product_id>",views.add_order3,name="add_order3"),
    path("add_order4\<int:product_id>",views.add_order4,name="add_order4"),
    path("orders",views.orders,name="orders"),
    path("placeorder",views.placeorder,name="placeorder"),
    path("removeorder",views.removeorder,name="removeorder"),
    path("trackorders",views.trackorders,name="trackorders"),
    path("manageorders",views.manageorders,name="manageorders"),
    path("changestatus\<int:order_id>",views.changestatus,name="changestatus")
]