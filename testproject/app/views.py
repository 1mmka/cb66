from typing import Any
from django.db import models
from django.shortcuts import render
from django.forms import ModelForm, ValidationError, modelform_factory,NumberInput,TextInput
from app.models import Human
from django.views.generic import CreateView
from django.urls import reverse_lazy


# Create your views here.
class CustomModelForm(ModelForm):
    class Meta:
        model = Human
        fields = ('name','age','city')
        labels = {
            'name':'Имя', 'age':'Возраст','city':'Город'
        }
        widgets = {
            'age':NumberInput(attrs={'required':'required'})
        }

    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 0:
            raise ValidationError('age can not be negative number')
        return age

customForm = modelform_factory(Human,CustomModelForm)

class CreateHumanView(CreateView):
    template_name = 'create.html'
    form_class = customForm
    success_url = reverse_lazy('create')
    
    def form_valid(self,form):
        if form.is_valid():
            return super().form_valid(form)
        else:
            return self.form_invalid(form)