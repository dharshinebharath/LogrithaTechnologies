from django.urls import path
from .import views
urlpatterns=[
    path('',views.home,name='home'),
    path('students/',views.students,name='students'),
    path('registration/',views.registration,name='registration'),
    path('add_user/',views.add_user,name='add_user'),
    path('update_form/<int:id>/',views.update_form,name='update_form'),
    path('update_form_data/<int:id>/',views.update_user,name='update_form_data'),
    path('delete_user/<int:id>/',views.delete_user,name='delete_user'),
    
]