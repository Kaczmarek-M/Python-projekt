from django.urls import path
from KI.views import test_response, nowa_ksiazka, edytuj_ksiazke, usun_ksiazke

urlpatterns = [
    path('test/', test_response, name="test_response"),
    path('nowa/', nowa_ksiazka, name="nowa_ksiazka"),
    path('edytuj/<int:id>/', edytuj_ksiazke, name="edytuj_ksiazke"),
    path('usun/<int:id>/', usun_ksiazke, name="usun_ksiazke"),

]