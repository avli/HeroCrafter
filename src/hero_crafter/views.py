from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import fields
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from . import models


class HomeView(LoginRequiredMixin, ListView):
    model = models.Character
    template_name = 'home.html'
    context_object_name = 'characters'

    def get_queryset(self):
        return models.Character.objects.filter(user=self.request.user)


class CharacterForm(forms.ModelForm):
    portrait_url = forms.URLField(widget=forms.HiddenInput(), initial='')

    class Meta:
        model = models.Character
        fields = [
            'name', 'race', 'gender', 'strength', 'dexterity', 'constitution', 'intelligence', 'wisdom',
            'hit_points', 'charisma', 'character_class', 'alignment', 'biography', 'portrait_url']


class CharacterView(LoginRequiredMixin, DetailView):
    model = models.Character
    template_name = 'character.html'
    context_object_name = 'character'


class CreateCharacterView(LoginRequiredMixin, CreateView):
    form_class = CharacterForm
    template_name = "create_character.html"
    success_url = reverse_lazy('home')

    def get_form(self, form_class=None):
        form = super(CreateCharacterView, self).get_form(form_class)
        for field in form.fields.values():
            if isinstance(field, fields.TypedChoiceField):
                field.choices = list(field.choices)[1:]
        return form

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user_id = self.request.user.id
        res = super().form_valid(form)
        return res
