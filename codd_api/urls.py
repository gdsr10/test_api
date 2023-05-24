"""codd_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api.views import Login, CredentialUpdate, SidebarList, PaymentModule, ItemNumberList, FollowUp, Predictor, Clinical


urlpatterns = [
    path('admin/', admin.site.urls),
    
    # API to post/Login Scheme
    path('api/login/', Login.LoginView.as_view()),
    
    # API to post/credentialupdate Scheme
    path('api/credentialupdate/', CredentialUpdate.CredentialUpdateView.as_view()),
    
    # API to post/SidebarListView Scheme
    path('api/sidebarlist/', SidebarList.SidebarListView.as_view()),
    
    # API to post/PaymentModuleView Scheme
    path('api/paymentmodule/', PaymentModule.PaymentModuleView.as_view()),
    
    # API to post/ItemNumberListView Scheme
    path('api/itemnumberlist/', ItemNumberList.ItemNumberListView.as_view()),
    
    # API to post/FollowUpView Scheme
    path('api/followup/', FollowUp.FollowUpView.as_view()),
    
    # API to post/PredictorView Scheme
    path('api/predictor/', Predictor.PredictorView.as_view()),
    
    # API to post/PredictorView Scheme
    path('api/clinicaldata/', Clinical.ClinicalView.as_view()),
    
]
