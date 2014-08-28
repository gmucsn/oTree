# -*- coding: utf-8 -*-
import matching_pennies.models as models
from django import forms
from matching_pennies._builtin import Form


class PennySideForm(Form):

    class Meta:
        model = models.Player
        fields = ['penny_side']
        widgets = {'penny_side': forms.RadioSelect()}

    def labels(self):
        return {'penny_side': 'Please select a side:'}
