from django.urls import path
from owner import views
urlpatterns=[
    path("mobiles/add",views.mobile_create,name="addmobiles"),
    path("home",views.home,name="home"),
    path("brand/add",views.add_brand,name="addbrand"),
    path("brand/list", views.list_brand, name="listbrand"),
    path("brand/<int:id>", views.view_brand, name="viewbrand"),
    path("brand/remove<int:id>", views.remove_brand, name="remove"),
    path("brand/change<int:id>",views.update_brand,name="change"),
    path("mobiles",views.mobile_list,name="listmobiles"),
    path("mobiles/change/<int:id>",views.mobile_update,name="mobileedit"),
    path("mobiles/<int:id>",views.mobile_detail,name="mobiledetail"),
    path("mobiles/remove/<int:id>",views.remove_mobile,name="removemobile")

]