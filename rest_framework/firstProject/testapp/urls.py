from django.urls import path, include

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('api/', include('testapp.apis.urls')),
]
