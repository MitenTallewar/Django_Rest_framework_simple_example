from rest_framework.routers import SimpleRouter
from studapp.views import StudentOperations


srouter =SimpleRouter()
srouter.register('api/v1',StudentOperations)
urlpatterns=srouter.urls