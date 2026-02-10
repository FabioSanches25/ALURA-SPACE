from django import forms

class LoginForm(forms.Form):
    nome_login = forms.CharField(
        label='Nome de Login', 
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Digite seu nome de login'})
                   
    )
    senha = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control', 
                'placeholder': 'Digite sua senha' 
            }      
        )
    )

class CadastroForms(forms.Form):
        nome_cadastro = forms.CharField(
            label='Nome de Cadastro', 
            required=True,
            max_length=100,
            widget=forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Digite seu nome de Cadastro'})
                       
        )
        email = forms.EmailField(
            label='E-mail',
            required=True,
            max_length=70,
            widget=forms.EmailInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Digite seu e-mail' 
                }      
            )
        )
        senha = forms.CharField(
            label='Senha',
            required=True,
            max_length=70,
            widget=forms.PasswordInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Digite sua senha' 
                }      
            )
        )
        confirmar_senha = forms.CharField(
            label='Confirmar Senha',
            required=True,
            max_length=70,
            widget=forms.PasswordInput(
                attrs={
                    'class': 'form-control',    
                    'placeholder': 'Confirmar sua senha' 
                }      
            )
        )

        def clean_nome_cadastro(self):
            nome = self.cleaned_data.get('nome_cadastro')
            if nome:
                nome = nome.strip()
                if " " in nome:
                     raise forms.ValidationError("O nome de cadastro não pode conter espaços.")
                else:
                     return nome
                
        def clean_confirmar_senha(self):
            senha = self.cleaned_data.get('senha')  
            confirmar_senha = self.cleaned_data.get('confirmar_senha')
            if senha and confirmar_senha and senha != confirmar_senha:
                raise forms.ValidationError("As senhas não coincidem.")
            return confirmar_senha



  