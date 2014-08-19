import otree.test
from otree.common import Money, money_range
import bargaining.views as views
from bargaining._builtin import Bot


class PlayerBot(Bot):

    def play(self):

        # start
        self.submit(views.Introduction)

        # request
        self.submit(views.Request, {"request_amount": 0.45})  # figure out how to randomize this amount

        # results
        self.submit(views.Results)