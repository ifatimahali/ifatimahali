from django.contrib import admin
from django.urls import include, path

app_name = 'blog'

urlpatterns = [
    path('blog/', include('blog.urls', namespace='blog')),
    path('admin/', admin.site.urls),
]