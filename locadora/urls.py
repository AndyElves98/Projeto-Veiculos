from django.urls import path
from . import views #arquivo views que ainda não utilizamos

urlpatterns = [
    path('', views.listar_locacoes, name='listar_locacoes'),
    path('listar_clientes', views.listar_clientes, name='listar_clientes'), #nova url
    path('listar_veiculos', views.listar_veiculos, name='listar_veiculos'), #nova url
    path('locacao/<int:id>/', views.detalhar_locacao, name='detalhar_locacao'), #nova url
    path('locacao/new/', views.cadastrar_locacao, name='cadastrar_locacao'), #nova url
    path('locacao/editar/<int:id>/', views.editar_locacao, name='editar_locacao'),#nova url
	path('cliente/editar/<int:id>/', views.editar_cliente, name='editar_cliente'),#nova url
    path('veiculo/editar/<int:id>/', views.editar_veiculo, name='editar_veiculo'),#nova url
    path('buscar_locacao', views.buscar_locacao, name='buscar_locacao'),#nova url
    path('buscar_veiculo', views.buscar_veiculo, name='buscar_veiculo'),#nova url
    path('locacao/deletar/<int:id>/', views.delete_locacao, name='delete_locacao'),
    path('veiculo/deletar/<int:id>/', views.delete_veiculo, name='delete_veiculo'),
    path('cliente/deletar/<int:id>/', views.delete_cliente, name='delete_cliente'),

     #rotas do login e logout
    path('page_login', views.page_login, name='page_login'),
    path('autenticar_usuario', views.autenticar_usuario, name='autenticar_usuario'),
    path('logout_usuario', views.logout_usuario, name='logout_usuario'),
]

