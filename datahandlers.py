"""
Datahandlers are use to collect data from simulated runs
"""

import sys
import inspect


class RepeatSingleRound():
    def __init__(self):
        self.data = {}
        self.data['score'] = []
        self.data['num_blacks'] = []
        self.data['exploded'] = []

    def process_round(self, rollout, score, exploded, *args, **kwargs):
        # Record the score
        self.data['score'].append(score)

        # Log if we exploded or not
        self.data['exploded'].append(exploded)

        # Record the number of black tokens played
        num_blacks = rollout.count('b1')
        self.data['num_blacks'].append(num_blacks)

    def post_process(self,):
        pass


clsmembers_pairs = inspect.getmembers(sys.modules[__name__], inspect.isclass)
DATAHANDLERS = {k: v for (k, v) in clsmembers_pairs}
