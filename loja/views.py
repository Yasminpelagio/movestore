from django.shortcuts import render, redirect
import random


produtos_lista = [
    {'id': 1, 'nome': 'Sofá Moderno Cinza', 'preco': 1250, 'imagem': 'https://images.unsplash.com/photo-1759722668385-90006d9c7aa7?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OHx8c29mYSUyMG1vZGVybm8lMjBjaW56YXxlbnwwfHwwfHx8MA%3D%3D'},
    {'id': 2, 'nome': 'Poltrona Elegante Bege', 'preco': 700, 'imagem': 'https://images.unsplash.com/photo-1619992677751-cb736bd47e2e?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjR8fHBvbHRyb25hfGVufDB8fDB8fHww'},
    {'id': 3, 'nome': 'Mesa de Jantar de Madeira', 'preco': 980, 'imagem': 'https://images.unsplash.com/photo-1636138388621-258a72ecb07e?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTZ8fG1lc2ElMjBkZSUyMGphbnRhcnxlbnwwfHwwfHx8MA%3D%3D'},
    {'id': 4, 'nome': 'Cadeira Estofada Azul', 'preco': 350, 'imagem': 'https://plus.unsplash.com/premium_photo-1723874468810-3147a74bb3a7?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8Y2FkZWlyYSUyMGF6dWx8ZW58MHx8MHx8fDA%3D'},
    {'id': 5, 'nome': 'Rack para TV ', 'preco': 480, 'imagem': 'https://plus.unsplash.com/premium_photo-1683133212932-7dd8bd0b2c67?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1yZWxhdGVkfDV8fHxlbnwwfHx8fHw%3D'},
    {'id': 6, 'nome': 'Estante de Livros Moderna', 'preco': 650, 'imagem': 'https://images.unsplash.com/photo-1708161885729-63faff807840?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NTV8fGVzdGFudGUlMjBkZSUyMGxpdnJvc3xlbnwwfHwwfHx8MA%3D%3D'},
    {'id': 7, 'nome': 'Mesa de Centro Redonda', 'preco': 390, 'imagem': 'https://plus.unsplash.com/premium_photo-1722843459670-cc2560c22b36?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTd8fG1lc2ElMjBkZSUyMGNlbnRyb3xlbnwwfHwwfHx8MA%3D%3D'},
    {'id': 8, 'nome': 'Conjunto de Pufes Coloridos', 'preco': 280, 'imagem': 'https://media.istockphoto.com/id/1443833087/pt/foto/different-poufs-on-white-background-home-design.webp?a=1&b=1&s=612x612&w=0&k=20&c=CBQgkShTrKh-FrQcZf1589Z-N3o_uh-76z17toia_rY='},
    {'id': 9, 'nome': 'Cama Queen com Cabeceira', 'preco': 1550, 'imagem': 'https://images.unsplash.com/photo-1613977257441-dd57bd5aaf70?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NDN8fGNhbWF8ZW58MHx8MHx8fDA%3D'},
    {'id': 10, 'nome': 'Mesa lateral', 'preco': 240, 'imagem': 'https://plus.unsplash.com/premium_photo-1674773521319-a67d6e0f2de5?q=80&w=679&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'},
]


carrinho_produtos = []


def home(request):
    produtos_destaque = random.sample(produtos_lista, 4)
    return render(request, 'home.html', {'produtos_destaque': produtos_destaque})

def produtos(request):
    return render(request, 'produtos.html', {'produtos': produtos_lista})

def carrinho(request):
    total_geral = sum(item['total'] for item in carrinho_produtos)
    return render(request, 'carrinho.html', {'carrinho': carrinho_produtos, 'total_geral': total_geral})

def adicionar_ao_carrinho(request, produto_id):
    produto = next((p for p in produtos_lista if p['id'] == produto_id), None)
    if produto:
        item_existente = next((i for i in carrinho_produtos if i['id'] == produto_id), None)
        if item_existente:
            item_existente['quantidade'] += 1
            item_existente['total'] = item_existente['preco'] * item_existente['quantidade']
        else:
            carrinho_produtos.append({
                'id': produto['id'],
                'nome': produto['nome'],
                'preco': produto['preco'],
                'quantidade': 1,
                'total': produto['preco'],
                'imagem': produto['imagem']
            })
    return redirect('produtos')

def remover_do_carrinho(request, produto_id):
    global carrinho_produtos
    carrinho_produtos = [item for item in carrinho_produtos if item['id'] != produto_id]
    return redirect('carrinho')

def finalizar_compra(request):
    global carrinho_produtos
    carrinho_produtos = []
    return render(request, 'finalizar.html')

def sobre(request):
    return render(request, 'sobre.html')

def contato(request):
    return render(request, 'contato.html')
