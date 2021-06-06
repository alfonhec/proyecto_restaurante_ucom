from catalogos.forms import ClientesForm
from django.shortcuts import render, redirect
from .models import Cliente, Producto, Pedidos

# Create your views here.
def index(request):
    form=Producto.objects.all()
    return render(request,
                    'catalogos/menu.html', 
                    {
                        'Producto':form
                    })


def cliente(request):
    form=Cliente.objects.all()
    return render(request,
                    'catalogos/clientes.html',
                    {
                        'Cliente':form
                    })

def formCliente(request):
    if request.method == 'POST':
        form = ClientesForm(request.POST)

        if form.is_valid:
            form.save()
            redirect('catalogos/clientes/')
    else:
        form = ClientesForm()
        
    return render(request,
            'catalogos/formCliente.html',
            {
                'form': form
            })

def pedidos(request):
    form=Pedidos.objects.all()
    return render(request,
                    'catalogos/pedidos.html', 
                    {
                        'Pedidos':form
                    })

