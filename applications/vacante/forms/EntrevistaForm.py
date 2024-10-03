from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Fieldset
from applications.vacante.models import Cli057AsignacionEntrevista
from applications.usuarios.models import UsuarioBase
from django.utils import timezone
from datetime import datetime, time


class EntrevistaCrearForm(forms.Form):
    # Campos del usuario
    fecha_entrevista = forms.DateField(
        label='Fecha de Entrevista',
        required=True,
        widget=forms.DateInput(attrs={
            'class': 'form-control form-control-solid mb-3 mb-lg-0',
            'type': 'date',
        })
    )

    hora_entrevista = forms.TimeField(
        label='Hora de Entrevista',
        required=True,
        widget=forms.TimeInput(attrs={
            'class': 'form-control form-control-solid mb-3 mb-lg-0',
            'type': 'time',
        })
    )

    tipo_entrevista = forms.ChoiceField(
        choices=Cli057AsignacionEntrevista.TIPO_ENTREVISTA,
        label='Tipo de Entrevista',
        required=True,
        widget=forms.Select(attrs={
            'class': 'form-select form-select-solid',
            'data-control': 'select2',
        })
    )

    lugar_enlace = forms.CharField(
        label='Lugar o Enlace',
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-solid mb-3 mb-lg-0',
            'placeholder': 'Ingrese el lugar o enlace de la entrevista',
        })
    )

    # entrevistador = forms.ModelChoiceField(
    #     queryset=UsuarioBase.objects.none(),  # Inicialmente vacío, se actualizará en __init__
    #     label='Cliente',
    #     required=False,
    #     widget=forms.Select(attrs={
    #         'class': 'form-select form-select-solid',
    #         'data-control': 'select2',
    #     })
    # )

    def __init__(self, *args, **kwargs):
        grupo_id = kwargs.pop('grupo_id', None)
        cliente_id = kwargs.pop('cliente_id', None)
        super().__init__(*args, **kwargs)

        # Configuración de Crispy Forms
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_id = 'form_crear_entrevista'
        self.helper.form_class = 'w-200'

        

        usuarios =  UsuarioBase.objects.filter(group=grupo_id, cliente_id_051=cliente_id, is_active=True).order_by('primer_apellido')
        usuario_choices = [('', '----------')] + [(usuario.id, f" {usuario.primer_apellido} {usuario.primer_nombre}") for usuario in usuarios]
        
        # Añadir el campo city al formulario con las opciones obtenidas
        self.fields['entrevistador'] = forms.ChoiceField(
            choices=usuario_choices,
            label='Entrevistador',
            widget=forms.Select(attrs={
                'class': 'form-select form-select-solid',
                'data-control': 'select2',
            })
        )
        
        self.helper.layout = Layout(
                Row(
                    Column('fecha_entrevista', css_class='form-group mb-0'),
                    Column('hora_entrevista', css_class='form-group mb-0'),
                ),
                Row(
                    Column('entrevistador', css_class='form-group mb-0'),
                    css_class='fw-semibold fs-6 mb-2'
                ),
                Row(
                    Column('tipo_entrevista', css_class='form-group mb-0'),
                    css_class='fw-semibold fs-6 mb-2'
                ),
                Row(
                    Column('lugar_enlace', css_class='form-group mb-0'),
                    css_class='fw-semibold fs-6 mb-2'
                ),
            )

    def clean(self):
        cleaned_data = super().clean()

        fecha_entrevista = cleaned_data.get('fecha_entrevista')
        hora_entrevista = cleaned_data.get('hora_entrevista')

        # valida fecha
        if fecha_entrevista:
            fecha_actual = timezone.now().date()
            if fecha_entrevista < fecha_actual:
                self.add_error('fecha_entrevista', 'La fecha de la entrevista no puede ser anterior a la fecha actual.')

        return cleaned_data