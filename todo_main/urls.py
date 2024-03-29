from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

from . import views

app_name = 'todo_main'

router = routers.DefaultRouter()
router.register(r'todos',views.Todo_index)
router.register(r'comment', views.Comment_index)

urlpatterns = [
    url('api-auth/', include('rest_framework.urls')),
    url(r'^', include(router.urls)), #index
    url(r'^todos/$', views.Todo_main.as_view(), name='todo_list'), #list
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)