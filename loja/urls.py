from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                        
    path('produtos/', views.produtos, name='produtos'),        
    path('sobre/', views.sobre, name='sobre'),                
    path('contato/', views.contato, name='contato'),          
    path('carrinho/', views.carrinho, name='carrinho'),       
    path('adicionar/<int:produto_id>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),  
    path('remover/<int:produto_id>/', views.remover_do_carrinho, name='remover_do_carrinho'),        
    path('finalizar/', views.finalizar_compra, name='finalizar_compra'),                               
]
