from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_vies
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_vies.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_vies.LogoutView.as_view(), name='logout'),
    path('course/', include('courses.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
