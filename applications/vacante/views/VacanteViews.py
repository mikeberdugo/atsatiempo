from django.shortcuts import render, redirect, get_object_or_404
from applications.cliente.models import Cli051Cliente
from applications.vacante.forms.VacanteForms import VacanteForm
from applications.vacante.models import Cli052Vacante, Cli055ProfesionEstudio, Cli053SoftSkill, Cli054HardSkill, Cli052VacanteHardSkillsId054, Cli052VacanteSoftSkillsId053, Cli056AplicacionVacante
from applications.usuarios.models import Permiso
from applications.common.models import Cat001Estado, Cat004Ciudad
from applications.candidato.models import Can101Candidato
from django.contrib import messages
from django.http import JsonResponse
import json
from django.contrib.auth.decorators import login_required
from applications.usuarios.decorators  import validar_permisos

# vacante por cliente sin loqin 
def vacante_cliente_mostrar(request, pk=None):
    #datos clientes
    cliente = get_object_or_404(Cli051Cliente, pk=pk)
    #estado_general_vacante
    estado = Cat001Estado.objects.get(id=1)
    #listado vacantes activas
    vacantes = Cli052Vacante.objects.filter(cliente_id_051=cliente.id, estado_id_001=1).order_by('-id')

    form_errors = False

    # Formulario Vacantes
    if request.method == 'POST': 
        form = VacanteForm(request.POST)
        
        if form.is_valid():
            #datos formulario

            titulo = form.cleaned_data['titulo']
            numero_posiciones = form.cleaned_data['numero_posiciones']
            profesion_estudio_id_055 = form.cleaned_data['profesion_estudio_id_055']
            experiencia_requerida = form.cleaned_data['experiencia_requerida']
            soft_skills_id_053 = form.cleaned_data['soft_skills_id_053']
            hard_skills_id_054 = form.cleaned_data['hard_skills_id_054']
            funciones_responsabilidades = form.cleaned_data['funciones_responsabilidades']
            salario = form.cleaned_data['salario']

            estado_id = Cat001Estado.objects.get(id=1)
            ciudad_id = Cat004Ciudad.objects.get(id=form.cleaned_data['ciudad'])

            
            # Intentar obtener el objeto profesion estudio
            profesion_estudio_dato, created = Cli055ProfesionEstudio.objects.get_or_create(
                nombre = profesion_estudio_id_055,
                defaults={'estado_id_001': estado}
            )

            #crea la vacante
            vacante_creada = Cli052Vacante.objects.create(
                titulo = titulo,
                numero_posiciones = numero_posiciones,
                experiencia_requerida = experiencia_requerida,
                funciones_responsabilidades = funciones_responsabilidades,
                salario = salario,
                estado_vacante = 1,
                ciudad_id = ciudad_id.id,
                cliente_id_051_id = cliente.id,
                estado_id_001_id = estado_id.id,
                profesion_estudio_id_055_id = profesion_estudio_dato.id,
            )



            # Convertir el string JSON en un objeto Python (lista de diccionarios)
            skills = json.loads(soft_skills_id_053)
            
            # Ahora puedes iterar sobre la lista de diccionarios
            for skill in skills:
                # Intentar obtener el objeto soft_skills
                soft_skills, created = Cli053SoftSkill.objects.get_or_create(
                    nombre = skill['value'],
                    defaults={'estado_id_001': estado}
                )

                Cli052VacanteSoftSkillsId053.objects.create(
                    cli052vacante=vacante_creada,
                    cli053softskill=soft_skills
                )


            # Convertir el string JSON en un objeto Python (lista de diccionarios)
            skills = json.loads(hard_skills_id_054)
            
            # Ahora puedes iterar sobre la lista de diccionarios
            for skill in skills:
                # Intentar obtener el objeto hard_skills
                hard_skills, created = Cli054HardSkill.objects.get_or_create(
                    nombre = skill['value'],
                    defaults={'estado_id_001': estado}
                )

                Cli052VacanteHardSkillsId054.objects.create(
                    cli052vacante=vacante_creada,
                    cli054hardskill=hard_skills
                )

            messages.success(request, 'El registro de la vacante ha sido creado con éxito.')
            return redirect('vacantes:vacantes_cliente', pk=cliente.id)
        else:
            form_errors = True
            messages.error(request, form.errors)
    else:
        form = VacanteForm()
        vacantes = Cli052Vacante.objects.filter(cliente_id_051=cliente.id, estado_id_001=1).order_by('-id')

    return render(request, 'vacante/listado_vacantes_cliente.html',
        { 
            'form': form,
            'vacantes': vacantes,
            'cliente': cliente,
            'form_errors': form_errors,
        })    

#vacante por cliente login
@login_required
@validar_permisos(*Permiso.obtener_nombres())
def vacante_cliente(request):
    # Verificar si el cliente_id está en la sesión
    cliente_id = request.session.get('cliente_id')
    primer_nombre = request.session.get('primer_nombre')
    
    
    # Obtener el cliente usando el id de la sesión
    cliente = get_object_or_404(Cli051Cliente, pk=cliente_id)
    #estado_general_vacante
    estado = Cat001Estado.objects.get(id=1)
    #listado vacantes activas
    vacantes = Cli052Vacante.objects.filter(cliente_id_051=cliente.id, estado_id_001=1).order_by('-id')

    form_errors = False

    # Formulario Vacantes
    if request.method == 'POST': 
        form = VacanteForm(request.POST)
        
        if form.is_valid():
            #datos formulario

            titulo = form.cleaned_data['titulo']
            numero_posiciones = form.cleaned_data['numero_posiciones']
            profesion_estudio_id_055 = form.cleaned_data['profesion_estudio_id_055']
            experiencia_requerida = form.cleaned_data['experiencia_requerida']
            soft_skills_id_053 = form.cleaned_data['soft_skills_id_053']
            hard_skills_id_054 = form.cleaned_data['hard_skills_id_054']
            funciones_responsabilidades = form.cleaned_data['funciones_responsabilidades']
            salario = form.cleaned_data['salario']

            estado_id = Cat001Estado.objects.get(id=1)
            ciudad_id = Cat004Ciudad.objects.get(id=form.cleaned_data['ciudad'])

            # Intentar obtener el objeto profesion estudio
            profesion_estudio_dato, created = Cli055ProfesionEstudio.objects.get_or_create(
                nombre = profesion_estudio_id_055,
                defaults={'estado_id_001': estado}
            )

            #crea la vacante
            vacante_creada = Cli052Vacante.objects.create(
                titulo = titulo,
                numero_posiciones = numero_posiciones,
                experiencia_requerida = experiencia_requerida,
                funciones_responsabilidades = funciones_responsabilidades,
                salario = salario,
                estado_vacante = 1,
                ciudad_id = ciudad_id.id,
                cliente_id_051_id = cliente.id,
                estado_id_001_id = estado_id.id,
                profesion_estudio_id_055_id = profesion_estudio_dato.id,
            )



            # Convertir el string JSON en un objeto Python (lista de diccionarios)
            skills = json.loads(soft_skills_id_053)
            
            # Ahora puedes iterar sobre la lista de diccionarios
            for skill in skills:
                # Intentar obtener el objeto soft_skills
                soft_skills, created = Cli053SoftSkill.objects.get_or_create(
                    nombre = skill['value'],
                    defaults={'estado_id_001': estado}
                )

                Cli052VacanteSoftSkillsId053.objects.create(
                    cli052vacante=vacante_creada,
                    cli053softskill=soft_skills
                )


            # Convertir el string JSON en un objeto Python (lista de diccionarios)
            skills = json.loads(hard_skills_id_054)
            
            # Ahora puedes iterar sobre la lista de diccionarios
            for skill in skills:
                # Intentar obtener el objeto hard_skills
                hard_skills, created = Cli054HardSkill.objects.get_or_create(
                    nombre = skill['value'],
                    defaults={'estado_id_001': estado}
                )

                Cli052VacanteHardSkillsId054.objects.create(
                    cli052vacante=vacante_creada,
                    cli054hardskill=hard_skills
                )

            messages.success(request, 'El registro de la vacante ha sido creado con éxito.')
            return redirect('vacantes:vacantes')
        else:
            form_errors = True
            messages.error(request, form.errors)
    else:
        form = VacanteForm()
        vacantes = Cli052Vacante.objects.filter(cliente_id_051=cliente.id, estado_id_001=1).order_by('-id')

    return render(request, 'vacante/listado_vacantes_cliente.html',
        { 
            'form': form,
            'vacantes': vacantes,
            'cliente': cliente,
            'form_errors': form_errors,
            'primer_nombre': primer_nombre,
        })

#ver todas las vacantes


@login_required
@validar_permisos(*Permiso.obtener_nombres())
def vacante_cliente_todas(request):
    
    vacantes = Cli052Vacante.objects.filter(estado_id_001=1).order_by('-id')

    return render(request, 'vacante/listado_vacantes_todos.html',
        { 
            'vacantes': vacantes,
        })

@login_required
@validar_permisos(*Permiso.obtener_nombres())
def vacante_detalle(request, pk):
    vacante = get_object_or_404(Cli052Vacante, pk=pk)
    cliente = get_object_or_404(Cli051Cliente, id=vacante.cliente_id_051.id)

    user_id = request.session.get('_auth_user_id')
    print(user_id)

    contexto = {
        'vacante': vacante,
        'cliente': cliente,
    }
    return render(request, 'vacante/detalle_vacante.html', contexto)

@login_required
@validar_permisos(*Permiso.obtener_nombres())
def vacante_aplicada(request, pk):
    error_vacante = False

    candidato_id = request.session.get('candidato_id')
    vacante = get_object_or_404(Cli052Vacante, id=pk)
    candidato = get_object_or_404(Can101Candidato, id=candidato_id)
    # Verifica si ya existe una aplicación para esta vacante y este candidato
    aplicacion_existente = Cli056AplicacionVacante.objects.filter(
        candidato_101=candidato,
        vacante_id_052=vacante
    ).exists()


    if aplicacion_existente:
        messages.warning(request, 'Ya has aplicado a esta vacante anteriormente.')
        error_vacante = True
    else:
        Cli056AplicacionVacante.objects.create(
                candidato_101=candidato,
                vacante_id_052=vacante
            )
        messages.success(request, 'Has aplicado a la vacante con éxito.')

    return render(request, 'vacante/aplicar_vacante.html',
        { 
            'vacantes': vacante,
            'error_vacante': error_vacante,
        })

@login_required
@validar_permisos(*Permiso.obtener_nombres())
def vacante_candidato(request):
    candidato_id = request.session.get('candidato_id')
    candidato = get_object_or_404(Can101Candidato, id=candidato_id)
    vacante_aplicada = Cli056AplicacionVacante.objects.filter(candidato_101=candidato.id)
    # vacante = get_object_or_404(Cli052Vacante, id=vacante_aplicada.vacante_id_052)

    contexto = {
        # 'vacante': vacante,
        'vacante_aplicada' : vacante_aplicada,

    }

    return render(request, 'vacante/vacante_candidato.html', contexto)

@login_required
@validar_permisos(*Permiso.obtener_nombres())
def vacante_gestion(request, pk):
    vacante = get_object_or_404(Cli052Vacante, pk=pk)
    cliente = get_object_or_404(Cli051Cliente, id=vacante.cliente_id_051.id)
    vacante_aplicada = Cli056AplicacionVacante.objects.filter(vacante_id_052=vacante.id)

    user_id = request.session.get('_auth_user_id')
    print(user_id)

    contexto = {
        'vacante': vacante,
        'cliente': cliente,
        'vacante_aplicada': vacante_aplicada,
    }
    return render(request, 'vacante/gestion_vacante.html', contexto)


