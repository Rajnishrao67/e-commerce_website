from django.urls import path
from  .import views
urlpatterns = [
   	path("",views.index, name="shop home"),
   	path('about/', views.about, name="AboutUS"),
   	path('contact/', views.contact, name="ContactUs"),
   	path('tracker/', views.tracker, name="TrackingStatus"),
   	path('search/', views.search, name="Search"),
   	path('products/<int:myid>', views.productview, name="ProductView"),
   	path('checkout/', views.checkout, name="CheckOut")
  

]
