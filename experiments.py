import sys
import inspect
import numpy as np
import matplotlib.pyplot as plt


class SimulateOneRound():
    """
    Simulate one round of quacks (posiible multiple times)
    """
    def __init__(self,
                 policy,
                 bag,
                 datahandler,
                 num_samples=1,
                 *args, **kwargs):

        self.policy = policy
        self.bag = bag
        self.datahandler = datahandler

        self.num_samples = num_samples

    def run(self):
        for _ in range(self.num_samples):
            # Use the policy to play a round
            outcome = self.policy.play(self.bag)

            # Process the results of the round
            self.datahandler.process_round(**outcome)

            # Reset the experiment
            self.reset()

    def process_result(self,):

        # Create a figure
        fig, ax = plt.subplots(1, 1)

        # Plot the score distribution
        score = np.array(self.datahandler.data['score'])

        print(score)
        n_bins = len(np.unique(score))
        ax.hist(score, bins=n_bins)
        ax.set_xlabel('Score')
        ax.set_ylabel('Count')
        fig.savefig('n_orange.png')

    def reset(self):
        self.bag.reset()


clsmembers_pairs = inspect.getmembers(sys.modules[__name__], inspect.isclass)
EXPERIMENTS = {k: v for (k, v) in clsmembers_pairs}
