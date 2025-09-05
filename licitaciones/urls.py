from django.urls import path
from .views import LicitacionListView, LicitacionCreateView, LicitacionUpdateView, LicitacionDeleteView

urlpatterns = [
    path("", LicitacionListView.as_view(), name="lista"),
    path("nuevo/", LicitacionCreateView.as_view(), name="nuevo"),
    path("editar/<int:pk>/", LicitacionUpdateView.as_view(), name="editar"),
    path("borrar/<int:pk>/", LicitacionDeleteView.as_view(), name="borrar"),
]
