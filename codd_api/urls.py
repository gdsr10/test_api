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
# from rest_framework.authtoken.views import obtain_auth_token
from api.views import Login, CredentialUpdate, SidebarList, PaymentModule, ItemNumberList, FollowUp, Predictor, Clinical, MtaRecord, Layout
from api.views import KPIData, ForgotPassword, OTPVerify, ShowStatus, SentSms , ContactDetails , MBSReview, Logout


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
    
    # API to post/MtaRecordView Scheme
    path('api/mtarecord/', MtaRecord.MtaRecordView.as_view()),
    
    # API to post/MtaRecordView Scheme
    path('api/layoutdata/', Layout.LayoutView.as_view()),
    
    # API to post/KPIDataView Scheme
    path('api/kpidata/', KPIData.KPIDataView.as_view()),
    
    # API to post/ForgotPasswordView Scheme
    path('api/forgotpassword/', ForgotPassword.ForgotPasswordView.as_view()),
    
    # API to post/OTPVerifyView Scheme
    path('api/otpverify/', OTPVerify.OTPVerifyView.as_view()),
    
    # API to post/SentSmsView Scheme
    path('api/sentsms/', SentSms.SentSmsView.as_view()),
    
    # API to post/showstatus Scheme
    path('api/showstatus/', ShowStatus.ShowStatusView.as_view()),
    
    # API to post/ContactDetailsView Scheme
    path('api/contactdetails/', ContactDetails.ContactDetailsView.as_view()),
    
    # API to post/MBSReviewView Scheme
    path('api/mbsreview/', MBSReview.MBSReviewView.as_view()),
    
    # API to post/LogoutView Scheme
    path('api/logout/', Logout.LogoutView.as_view()),
    
    # path('get-token/', obtain_auth_token)
    
]
