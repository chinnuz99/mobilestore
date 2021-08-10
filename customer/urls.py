from django.urls import path
from customer import views

urlpatterns=[
    path("accounts/signin",views.SignInView.as_view(),name="signin"),
    path("accounts/signup",views.RegistrationView.as_view(),name="signup"),
    # path("accounts/signout",)
    path("home",views.CustomerHomeView.as_view(),name="customerhome")

]