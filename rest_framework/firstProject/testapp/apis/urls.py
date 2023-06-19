from django.urls import path, include
from .views import test
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('api/', include('testapp.apis.urls')),
    path('',test)
]
