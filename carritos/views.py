from django.shortcuts import redirect, get_object_or_404,render
from .models import Carrito, CarritoProducto
from productos.models import Producto

def agregar_producto_a_carrito(request):
    if request.method == 'POST':
        # Verifica que el usuario esté autenticado
        if not request.user.is_authenticated:
            return redirect('login')

        producto_id = request.POST.get('producto_id')
        cantidad = int(request.POST.get('cantidad', 1))

        # Asegúrate de que aquí estás usando 'id_producto' como el nombre del campo del modelo
        producto = get_object_or_404(Producto, id_producto=producto_id)

        # Obtén o crea el carrito para el cliente
        carrito, created = Carrito.objects.get_or_create(cliente=request.user.cliente)

        # Agregar el producto al carrito
        carrito_producto, created = CarritoProducto.objects.get_or_create(
            carrito=carrito,
            producto=producto,
            defaults={'cantidad': 0}
        )
        carrito_producto.cantidad += cantidad
        carrito_producto.save()

        return redirect('carrito')  # Redirige al carrito después de agregar el producto

def carrito_view(request):
    # Asegúrate de que el usuario esté autenticado
    if not request.user.is_authenticated:
        return redirect('login')

    # Obtén o crea un carrito para el cliente
    carrito, created = Carrito.objects.get_or_create(cliente=request.user.cliente)

    # Manejar la adición de productos al carrito
    if request.method == 'POST':
        producto_id = request.POST.get('producto_id')
        cantidad = int(request.POST.get('cantidad', 1))
        producto = get_object_or_404(Producto, id=producto_id)

        # Agregar el producto al carrito
        carrito_producto, created = CarritoProducto.objects.get_or_create(
            carrito=carrito,
            producto=producto,
            defaults={'cantidad': 0}
        )
        carrito_producto.cantidad += cantidad
        carrito_producto.save()

        return redirect('carrito')

    # Obtener los productos del carrito
    productos_en_carrito = carrito.productos.all()

    # Obtener todos los productos disponibles
    productos = Producto.objects.all()

    # Calcular el total de cada producto
    for item in productos_en_carrito:
        item.total = item.cantidad * item.producto.precio

    context = {
        'carrito': carrito,
        'productos_en_carrito': productos_en_carrito,
        'productos': productos,  # Asegúrate de pasar la lista de productos
    }
    return render(request, 'carrito.html', context)
