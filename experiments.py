import sys
import inspect
import numpy as np
import matplotlib.pyplot as plt

from game_mechanics import Token

class SimulateOneRound():
    """
    Simulate one round of quacks (possibly multiple times)
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

    def process_results(self,):

        # Create a figure
        fig, ax = plt.subplots(1, 1)

        # Plot the score distribution
        score = np.array(self.datahandler.data['score'])

        n_bins = len(np.unique(score))
        ax.hist(score, bins=n_bins)
        ax.set_xlabel('Score')
        ax.set_ylabel('Count')
        fig.savefig('n_orange.png')

    def reset(self):
        self.bag.reset()


class SweepOrange():
    """
    Simulate a single round multiple times, add one orange, repeat
    """
    def __init__(self,
                 policy,
                 bag,
                 datahandler,
                 num_samples=1,
                 num_orange_max=10,
                 *args, **kwargs):

        self.policy = policy
        self.bag = bag

        self.setup_datahandler(num_samples, num_orange_max)

        self.num_samples = num_samples
        self.num_orange = 1
        self.num_orange_max = 10

    def run(self):
        for i in range(1, self.num_orange_max+1):
            for j in range(self.num_samples):
                # Use the policy to play a round
                outcome = self.policy.play(self.bag)

                # Process the results of the round
                # self.datahandler.process_round(**outcome)
                self.process_round(sample_index=j,
                                   orange_index=i-1,
                                   **outcome)

                # Reset the experiment
                self.reset()

            # Add an orange token to the bag
            self.bag.add_token(token=Token(color='orange', value=1))
            self.num_orange += 1
            # Reset the experiment
            self.reset()

    def setup_datahandler(self, num_samples, num_orange_max):

        z = np.zeros((num_samples, num_orange_max))
        self.data = {'score': z.copy(),
                     'exploded': z.copy(),
                     'num_black': z.copy(),
                     }

    def process_round(self,
                      orange_index,
                      sample_index,
                      rollout,
                      score,
                      exploded,
                      *args,
                      **kwargs):

        self.data['score'][sample_index, orange_index] = score
        self.data['exploded'][sample_index, orange_index] = exploded

        # Record the number of black tokens played
        num_black = rollout.count(Token(value=1, color='black'))
        self.data['num_black'][sample_index, orange_index] = num_black

    def process_result(self,):

        # Create a figure
        fig, ax = plt.subplots(1, 1)

        # Plot the score distribution
        # score = np.mean(self.data['score'], axis=0)

#        ax.boxplot(self.data['score'],
#                   showmeans=True)
        ax.violinplot(self.data['score'],
                   showmeans=True)

        ax.set_xlabel('# orange tokens')
        ax.set_ylabel('Score')
        fig.savefig('orange_sweep.png')

        ax.cla()

        num_black = np.mean(self.data['num_black'], axis=0)
        num_orange = np.arange(1, 11)
        ax.scatter(num_orange, num_black, color='k')
        ax.set_ylim(0.0, 3.0)
        ax.set_xlabel('# orange tokens')
        ax.set_ylabel('Expected no. black token played')
        fig.savefig('orange_sweep_black_open_prob_2.png')

    def reset(self):
        self.bag.reset()


class TestPolicy():
    """
    Test policy (or something else) by simulating a single round of quacks
    (once)
    """
    def __init__(self,
                 policy,
                 bag,
                 datahandler,
                 *args, **kwargs):

        self.policy = policy
        self.bag = bag

    def run(self):

        # Use the policy to play a round
        outcome = self.policy.play(self.bag)

        print(outcome)

        print("Board")
        for token in outcome['rollout']:
            print(token)

        print("Bag")
        print(self.bag)

    def reset(self):
        self.bag.reset()

    def process_results(self):
        pass


clsmembers_pairs = inspect.getmembers(sys.modules[__name__], inspect.isclass)
EXPERIMENTS = {k: v for (k, v) in clsmembers_pairs}
