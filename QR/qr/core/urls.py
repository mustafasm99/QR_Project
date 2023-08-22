from django.urls import path
from .views import *
urlpatterns = [
    path("ip" , ip , name="ip"),
    path("" , create_qr , name="home"),
    path("scan/<str:name>" , scand , name="scan"),
    path("allQR" , desplay , name="allqr"),
    path("analyze" , anal ,name="anal"),
]