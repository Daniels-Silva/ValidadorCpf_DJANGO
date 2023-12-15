
from django.contrib import admin
from django.urls import path, include

from brutus.views import validar_cpf
from brutus.views import remove_caracteres_especiaiss


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('brutus.urls'))
    
]
