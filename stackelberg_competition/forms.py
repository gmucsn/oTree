# -*- coding: utf-8 -*-
import stackelberg_competition.models as models
from stackelberg_competition.utilities import ParticipantMixIn, MatchMixIn
import ptree.forms


class QuantityForm(ParticipantMixIn, ptree.forms.Form):

    class Meta:
        model = models.Participant
        fields = ['quantity']

    def labels(self):
        return {'quantity': 'Enter the quantity of goods to produce?'}

    def quantity_error_message(self, value):
        if (value < 1) or (value > (self.treatment.total_capacity)/2):
            return 'Quantity should be between {} and {} units'.format(1, (self.treatment.total_capacity)/2)
