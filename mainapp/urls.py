from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

request_router = DefaultRouter()
request_router.register(r'api/v1/request', views.RequestFetchAPI)

urlpatterns = [
                  path('', views.HomePageView.as_view(), name='home'),
                  path('request/', views.CreateRequest.as_view(), name='requestview'),
                  # path('volunteer/', views.Maintenance.as_view(), name='registerview'),
                  path('volunteer/', views.RegisterVolunteer.as_view(), name='registerview'),
                  path('requests/', views.request_list, name='requestlistview'),
                  path('contactus/', views.districtmanager_list, name='contactus'),
                  path('reg_success/', views.RegSuccess.as_view(), name='reg_successview'),
                  path('req_sucess/', views.ReqSuccess.as_view(), name='req_sucessview'),
                  path('district_needs/', views.DistNeeds.as_view(), name='distneedsview'),
                  path('reg_contrib/', views.RegisterContributor.as_view(), name='reg_contribview'),
                  path('contrib_success/', views.ContribSuccess.as_view(), name='contribsucessview'),
                  path('disclaimer/', views.DisclaimerPage.as_view(), name='disclaimer'),
                  path('ieee/', views.AboutIEEE.as_view(), name='aboutieee'),
              ] + request_router.urls
