from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',include('studapp.urls')),
    path('api-auth/',include('rest_framework.urls')),#URl's for Rest framework
    url(r'swagger/',schema_view) #Url's for Swagger
]