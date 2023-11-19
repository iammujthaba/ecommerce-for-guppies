from . import views
from django.urls import path

app_name = 'ecommerce_app'
urlpatterns = [
    path('',views.allProdCat,name='allProdCat'),
    # 3 - tis "product_by_category" is called by "get_url" function from Catogory metohod with a parameter as catogory link its saved "c_slug"
    # it call "allProdCat" view function with argument "c_slug" it contain catogory link (go to view.py)
    path('<slug:c_slug>/',views.allProdCat,name='product_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.proDetail,name='proDetail'),
]