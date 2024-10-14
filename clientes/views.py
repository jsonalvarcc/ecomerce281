from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Cliente, Vendedor
#registar usuario como cliente o vendedor


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        tipo_usuario = request.POST.get('tipo_usuario')  # 'cliente' o 'vendedor'

        # Crear el usuario
        user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)

        # Crear el cliente o vendedor basado en la selección
        if tipo_usuario == 'cliente':
            Cliente.objects.create(user=user, telefono=telefono)
            messages.success(request, 'Cliente registrado correctamente.')
        elif tipo_usuario == 'vendedor':
            Vendedor.objects.create(user=user, telefono=telefono)
            messages.success(request, 'Vendedor registrado correctamente.')

        return redirect('login')  # Redirige al inicio de sesión o a donde desees

    return render(request, 'registration/register.html')



# Vista para cerrar sesión
def logout_view(request):
    logout(request)
    return redirect('index')  # Redirige a la página de inicio después de cerrar sesión

# Vista para la página principal (Home)
def home_view(request):
    return render(request, 'home.html')  # Renderiza la plantilla 'home.html'

# Vista para la página de inicio (Index)
def index_view(request):
    return render(request, 'index.html')  # Renderiza la plantilla 'index.html'

# Vista para iniciar sesión
def login_view(request):
    if request.method == 'POST':
        # Obtener el usuario y contraseña desde el formulario POST
        username = request.POST['username']
        password = request.POST['password']
        
        # Autenticar usuario
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # Inicia sesión al usuario
            return redirect('home')  # Redirige a la página de inicio (Home)
        else:
            # Si la autenticación falla, muestra un mensaje de error
            messages.error(request, 'Usuario o contraseña incorrectos.')
    
    return render(request, 'login.html')  # Renderiza la plantilla 'login.html'


