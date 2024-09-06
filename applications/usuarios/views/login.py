from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from applications.usuarios.forms.loginform import LoginForm
from applications.usuarios.forms.UserForms import SignupForm
from applications.usuarios.models import UsuarioBase 
from applications.cliente.models import Cli051Cliente
import random
from django.utils.text import capfirst
from applications.common.models import Cat004Ciudad, Cat001Estado

## login 

## login 

frases_falla_login = [
    "¡Parece que el nombre de usuario o la contraseña están jugando a las escondidas! Revisa y vuelve a intentarlo.",
    "¡Oh no! El nombre de usuario o la contraseña decidieron tomar un día libre. ¡Verifica los datos y vuelve a intentarlo!",
    "¡Ups! El nombre de usuario o la contraseña están en modo de vacaciones. Asegúrate de ingresar la información correcta.",
    "¡Ay caramba! El nombre de usuario o la contraseña se escaparon. Revisa tus datos e intenta de nuevo.",
    "¡Vaya, vaya! El nombre de usuario o la contraseña están en huelga. Verifica tus credenciales y vuelve a intentarlo.",
    "¡Oh no! Parece que el nombre de usuario o la contraseña están de parranda. Asegúrate de que todo esté en orden y prueba de nuevo.",
    "¡Menuda sorpresa! El nombre de usuario o la contraseña decidieron hacer una siesta. Verifica la información e inténtalo otra vez.",
    "¡Atención! El nombre de usuario o la contraseña están haciendo travesuras. Asegúrate de que sean correctos y vuelve a intentarlo.",
    "¡Ups! Parece que el nombre de usuario o la contraseña se perdieron. Verifica los datos e intenta nuevamente.",
    "¡Oh! El nombre de usuario o la contraseña están de fiesta. Revisa tus credenciales y prueba de nuevo."
]


frases_creacion_cuenta = [
    "¿Aún no tienes cuenta? ¡No te preocupes! Crear una es tan rápido que podrías hacerlo antes de que termine el video viral que estás viendo.",
    "¿Todavía no tienes cuenta? ¡No hay problema! Crear una es tan rápido que podrías hacerlo antes de que tu serie favorita lance el siguiente episodio.",
    "¿Aún sin cuenta? ¡No te preocupes! Crear una es tan rápido que podrías hacerlo antes de que tu videojuego cargue el siguiente nivel.",
    "¿Aún no tienes cuenta? ¡No te preocupes! Crear una es tan rápido que podrías hacerlo antes de que tu perro decida dejar de buscar su juguete.",
    "¿No tienes cuenta aún? ¡No hay problema! Crear una es tan rápido que podrías hacerlo antes de que tu planta decida crecer una hoja nueva.",
    "¿Todavía sin cuenta? ¡No te preocupes! Crear una es tan rápido que podrías hacerlo antes de que tu meme favorito se vuelva obsoleto.",
    "¿Aún sin cuenta? ¡No hay lío! Crear una es tan rápido que podrías hacerlo antes de que tu música de fondo cambie de canción.",
    "¿Aún no tienes cuenta? ¡No te preocupes! Crear una es tan rápido que podrías hacerlo antes de que tu tarta de cumpleaños se derrita.",
    "¿Todavía sin cuenta? ¡No hay problema! Crear una es tan rápido que podrías hacerlo antes de que tu gato decida dejar de ignorarte.",
    "¿Aún no tienes cuenta? ¡No te preocupes! Crear una es tan rápido que podrías hacerlo antes de que tu nuevo libro llegue al final de la primera página."
]

frases_restablecimiento = [
    "Te enviaremos un correo electrónico con instrucciones para restablecer tu contraseña. ¡Es tan fácil que podrías hacerlo mientras terminas de leer un artículo interesante!",
    "Recibirás un correo electrónico con instrucciones para restablecer tu contraseña. ¡Es tan rápido que podrías hacerlo antes de que tu serie favorita termine el primer episodio!",
    "Un correo electrónico con instrucciones para restablecer tu contraseña está en camino. ¡Es tan sencillo que podrías hacerlo mientras esperas que se cocine la pasta!",
    "Te enviaremos un correo con las instrucciones para restablecer tu contraseña. ¡Es tan fácil que podrías hacerlo mientras decides qué ver en tu plataforma de streaming!",
    "Pronto recibirás un correo con instrucciones para restablecer tu contraseña. ¡Es tan rápido que podrías hacerlo mientras tomas un breve descanso del trabajo!",
    "Te llegará un correo con las instrucciones para restablecer tu contraseña. ¡Es tan sencillo que podrías hacerlo mientras tu café se enfría!",
    "Un correo con las instrucciones para restablecer tu contraseña está en camino. ¡Es tan fácil que podrías hacerlo mientras esperas que se cargue una aplicación!",
    "Recibirás un correo con las instrucciones para restablecer tu contraseña. ¡Es tan rápido que podrías hacerlo mientras eliges tu próxima canción!",
    "Te enviaremos un correo con instrucciones para restablecer tu contraseña. ¡Es tan sencillo que podrías hacerlo mientras tu máquina de café hace su magia!",
    "Un correo con las instrucciones para restablecer tu contraseña llegará pronto. ¡Es tan fácil que podrías hacerlo mientras le das un vistazo a tus redes sociales!"
]

## Create cuenta

frases_bienvenida = [
    "¡Hola, aventurero! Espero que disfrutes más que un niño en una tienda de golosinas.",
    "¡Bienvenido al club! Espero que te diviertas tanto como un perro en una fiesta de disfraces.",
    "¡Saludos! Espero que te guste tanto como a un gato encontrar un rayo de sol en un día nublado.",
    "¡Qué alegría verte por aquí! Espero que te diviertas más que un niño con una caja de LEGO.",
    "¡Ey, bienvenido! Espero que disfrutes tanto como una abeja en un jardín lleno de flores.",
    "¡Hola, nuevo amigo! Espero que te guste tanto como un ratón encontrar un pedazo de queso.",
    "¡Hola, explorador! Espero que disfrutes más que un niño con una pala en la playa.",
    "¡Bienvenido! Espero que te diviertas tanto como un perro con una nueva pelota.",
    "¡Hey, qué tal! Espero que te guste tanto como un niño descubre un nuevo parque de diversiones.",
    "¡Saludos, compañero! Espero que disfrutes más que un chef con una receta ganadora.",
    "¡Hola, nuevo usuario! Espero que te diviertas tanto como un pájaro al vuelo libre.",
    "¡Bienvenido a bordo! Espero que disfrutes más que un pez en un estanque nuevo.",
    "¡Ey, qué pasa! Espero que te guste tanto como un niño con un nuevo juguete.",
    "¡Hola, amigo! Espero que disfrutes más que un gato con una caja nueva.",
    "¡Bienvenido a la fiesta! Espero que te diviertas tanto como una tortuga en un mar tranquilo.",
    "¡Hola, nuevo miembro! Espero que te guste tanto como a un niño le gusta encontrar caramelos escondidos.",
    "¡Qué bueno verte! Espero que disfrutes más que un caballo galopando libremente en el campo.",
    "¡Hola! Espero que te diviertas tanto como un mago descubriendo un nuevo truco.",
    "¡Bienvenido! Espero que disfrutes más que un niño en un rincón de juegos lleno de sorpresas.",
    "¡Hey, qué onda! Espero que te guste tanto como un gato jugando con una pelota de lana."
]


frases_error_contrasena = [
    "¡Oops! Las contraseñas están jugando al escondite. Asegúrate de que coincidan y prueba de nuevo.",
    "¡Vaya! Parece que las contraseñas están en una pelea. Revisa que ambas sean iguales y vuelve a intentarlo.",
    "¡Oh no! Las contraseñas no se están poniendo de acuerdo. Verifica que coincidan y prueba otra vez.",
    "¡Menuda confusión! Las contraseñas no están sincronizadas. Asegúrate de que sean idénticas y vuelve a intentarlo.",
    "¡Ay caramba! Las contraseñas están haciendo travesuras. Asegúrate de que sean las mismas y prueba de nuevo.",
    "¡Oops! Las contraseñas están en desacuerdo. Revisa que sean iguales y vuelve a intentarlo.",
    "¡Oh! Las contraseñas están haciendo su propia fiesta. Asegúrate de que coincidan y vuelve a intentarlo.",
    "¡Ups! Las contraseñas no están en sintonía. Verifica que sean iguales y vuelve a intentarlo.",
    "¡Vaya! Las contraseñas parecen tener opiniones diferentes. Asegúrate de que sean iguales y vuelve a intentarlo.",
    "¡Oh no! Las contraseñas están en una pelea de egos. Asegúrate de que sean idénticas y vuelve a intentarlo."
]

frases_error_usuario = [
    "¡Oh no! Este nombre de usuario ya está en uso. ¿Te atreves a encontrar uno tan genial como este?",
    "¡Vaya! Alguien más se adelantó y ya usó este nombre de usuario. Intenta ser más original y prueba con otro.",
    "¡Ups! Este nombre de usuario ya está registrado. Parece que el universo te está pidiendo que seas más creativo.",
    "¡Menuda coincidencia! Alguien más ya pensó en este nombre de usuario. Intenta con uno diferente antes de que todos se acaben.",
    "¡Oh! Este nombre de usuario ya está ocupado. Parece que alguien más también tiene buen gusto. Elige otro y sigue adelante.",
    "¡Oops! Este nombre de usuario ya está en la lista. ¿Qué tal probar con algo más único antes de que todos los buenos se acaben?",
    "¡Oh no! Este nombre de usuario ya está tomado. ¿Te animas a buscar un nombre tan épico como este?",
    "¡Vaya! Alguien más ya se adelantó y usó este nombre. ¿Qué tal ser el primero en elegir otro igualmente genial?",
    "¡Ay caramba! Este nombre de usuario ya está en uso. ¡Parece que te toca encontrar uno aún más increíble!",
    "¡Oh! Este nombre de usuario ya está ocupado. ¡Asegúrate de que tu nuevo nombre sea tan memorable como el primero!"
]


frases_error_email = [
    "¡Oops! Este correo electrónico ya está registrado. ¿Quizás quieras probar con otro antes de que todos se acaben?",
    "¡Oh no! Este correo electrónico ya está en uso. Parece que alguien más también le gusta el mismo dominio.",
    "¡Menuda coincidencia! Este correo electrónico ya está registrado. ¡Es como si todos estuvieran compitiendo por el mismo!",
    "¡Vaya! Este correo electrónico ya ha sido tomado. ¿Qué tal si encuentras uno aún más sorprendente para tu cuenta?",
    "¡Oh! Este correo electrónico ya está ocupado. ¡No te preocupes, hay muchos más por descubrir!",
    "¡Oops! Este correo electrónico ya está en uso. Parece que estás compitiendo con un montón de gente por el mismo. Prueba otro.",
    "¡Oh no! Este correo electrónico ya está registrado. ¿Qué tal si pruebas con otro para destacar entre la multitud?",
    "¡Ay caramba! Este correo electrónico ya ha sido tomado. ¡Elige otro antes de que todos los buenos se acaben!",
    "¡Vaya! Este correo electrónico ya está en uso. ¡No te preocupes, seguro que hay un montón de opciones interesantes!",
    "¡Oh! Este correo electrónico ya está en la lista. ¡Asegúrate de que el próximo sea tan atractivo como este!"
]

frases_inicio_sesion = [
    "¿Ya tienes una cuenta? ¡Perfecto! Entonces, deja de perder el tiempo y entra para empezar la diversión.",
    "¿Ya eres parte de la familia? ¡Genial! Solo falta iniciar sesión y empezar la acción.",
    "¡Ya tienes cuenta, aventurero! ¿Qué esperas? Inicia sesión y lánzate a la aventura.",
    "¿Cuentas con una cuenta? ¡Eso está bien! Solo falta hacer login y empezar a explorar.",
    "¿Ya eres usuario? ¡Perfecto! Solo inicia sesión y comienza a disfrutar.",
    "¡Ya tienes cuenta! Entonces, no pierdas más tiempo aquí. Inicia sesión y lánzate al meollo del asunto.",
    "¿Ya registraste tu cuenta? ¡Inicia sesión ya y empieza a disfrutar del contenido!",
    "¿Ya tienes acceso? ¡Genial! Solo falta iniciar sesión y comenzar la fiesta.",
    "¡Eres un usuario experimentado! Entonces, ¿por qué estás aquí? Inicia sesión y vamos a lo importante.",
    "¿Ya tienes una cuenta? ¡Entonces inicia sesión y deja de perder el tiempo aquí!"
]




def login_view(request):
    if request.user.is_authenticated:
        return redirect('candidatos:inicio')
    else:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    # request.session['company'] = user.company.id
                    
                    return redirect('candidatos:inicio')  
                else:
                    frase_aleatoria = random.choice(frases_falla_login)
                    messages.error(request, frase_aleatoria)
                    return redirect('accesses:login')  
        else:
            form = LoginForm()

    return render(request, './authentication/login.html',{
        'form':form,
        })
    
    

def logout_view(request):
    logout(request)
    return redirect('accesses:login')    # Redirigir a la página de inicio de sesión después de cerrar sesión

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            name = form.cleaned_data['name']
            last_name = form.cleaned_data['last_name']
            
            if password1 == password2:
                if UsuarioBase.objects.filter(username=email).exists():
                    messages.error(request, '¡Oops! Parece que alguien más ya se adelantó y tomó ese correo. Prueba con otro, o tal vez es el momento de reconciliarte con tu contraseña olvidada.')
                else:
                    
                    city =  Cat004Ciudad.objects.get(id = form.cleaned_data['city'] )
                    print(type(form.cleaned_data['nit']))
                    new_company = Cli051Cliente (
                        estado_id_001 = Cat001Estado.objects.get(id=1),
                        razon_social= form.cleaned_data['companyname'] ,
                        nit= form.cleaned_data['nit'],                        
                        ciudad_id_004= city ,
                        email= form.cleaned_data['companyemail'],
                        contacto= form.cleaned_data['companycontact'],
                        
                    )
                    
                    new_company.save()
                    
                    user = UsuarioBase.objects.create_user(
                        username= email, 
                        email= email, 
                        password=password1,
                        cliente_id_051 = new_company ,
                        primer_nombre = name.capitalize() ,
                        primer_apellido = last_name.capitalize(),
                        
                    )
            
                    login(request, user)
                    frase_aleatoria = random.choice(frases_bienvenida)
                    messages.success(request, frase_aleatoria)
                    return redirect('candidatos:inicio')  
            else:
                frase_aleatoria = random.choice(frases_error_contrasena)
                messages.error(request, frase_aleatoria)
    else:
        form = SignupForm()
    login_f = random.choice(frases_inicio_sesion)
    return render(request, './authentication/signup.html', 
                    {'form': form,
                    'login_f':login_f,
                    })
    