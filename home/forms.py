from django import forms
from .models import *




class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome', 'ordem']
        widgets = {
            'nome':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
            'ordem':forms.NumberInput(attrs={'class': 'inteiro form-control', 'placeholder': ''}),
        }
    def clean_nome(self):
            nome = self.cleaned_data.get('nome')
            if len(nome) < 3:
                raise forms.ValidationError("O nome deve ter pelo menos 3 caracteres.")
            return nome  
        
    def clean_ordem(self):
        ordem = self.cleaned_data.get('ordem')
        if ordem <= 0:
            raise forms.ValidationError("O campo ordem deve ser maior que zero.")
        return ordem    
       
    def clean(self):
         cleaned_data = super().clean()
         senha = cleaned_data.get("senha")
         confirmar_senha = cleaned_data.get("confirmar_senha")

         if senha != confirmar_senha:
              raise forms.ValidationError("As senhas não correspondem")
         
    def validar_nome(valor):
         if len(valor)< 3:
              raise forms.ValidationError("O nome deve ter pelo menos 3 caracteres.")
         


    





