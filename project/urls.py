
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todolist.urls'))
]
handler404 = "todolist.views.page_not_found_view"