from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # URLs da sua aplicação 'paginas'
    path('', include('paginas.urls')),
]