from django.urls import path
from .import views
app_name = 'shopapp'

urlpatterns = [
    path('',views.allcat,name='allcat'),
    path('<slug:c_slug>/',views.allcat,name='allpro'),
    path('<slug:c_slug>/<slug:pro_slug>/',views.prodetails,name='pdetails')
]
