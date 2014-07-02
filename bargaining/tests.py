import ptree.test
import bargaining.views as views
from bargaining.utilities import ParticipantMixin, ExperimenterMixin


class ParticipantBot(ParticipantMixin, ptree.test.ParticipantBot):

    def play(self):
        pass


class ExperimenterBot(ExperimenterMixin, ptree.test.ExperimenterBot):

    def play(self):
        pass