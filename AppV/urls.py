from django.urls import path
from AppV import views
from AppV import views_vistas
from django.contrib.auth.views import LogoutView

#para las imagenes
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
path('about/', views.about, name="about"),
path('', views_vistas.login_request, name="login"),
path('singup/', views.register, name='register'),
path('logout/', LogoutView.as_view(template_name='appv/logout.html'), name='logout'),
path('edit/', views.editar_perfil, name="editar"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urls_vista_clases=[
    path('pages', views_vistas.EntradasListView.as_view(), name='list'),
    path('detail/<int:pk>', views_vistas.EntradaDetalle.as_view(), name='detail'),
    path('edit/<int:pk>', views_vistas.EntradaEditar.as_view(), name='edit'),
    path('delete/<int:pk>', views_vistas.EntradaEliminar.as_view(), name='delete'),
    path('new/', views_vistas.EntradaCrear.as_view(), name='create'),
]



urlpatterns += urls_vista_clases

