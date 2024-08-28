from django.urls import path
from . import views


urlpatterns = [
    path('register/',views.register_view, name='register'), #for url's to get icluded we first define url present in app
    path('login/',views.login_view, name='login'),  #then we define what that url does from views 
    path('logout/',views.logout_view, name='logout'),#to use it in templates without implcitly writing the whole thing
    path('index/', views.index_view, name='index'),
    path('lawyers/', views.lawyers_view, name='lawyers'),
    path('info/', views.info_view, name='info'),
    path('profile/', views.profile_view, name='profile'),
    path('contact/', views.contact_view, name='contact'),
    path('enquiry/', views.enquiry_view, name='enquiry'),
    path('create_info/', views.create_info, name='create_info'),
    path('info_list/', views.info_list, name='info_list'),
    path('info_detail/<int:pk>/', views.info_detail, name='info_detail'),
    path('chatbot/', views.chatbot_response, name='chatbot_response'),
     path('search/', views.search_view, name='search'),

]

