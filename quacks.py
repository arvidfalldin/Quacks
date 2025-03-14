import numpy as np
import matplotlib.pyplot as plt

from game_mechanics import Bag
from policies import POLICYS
from experiments import EXPERIMENTS
from datahandlers import DATAHANDLERS
from parse_utils import create_parser, load_settings

if __name__ == "__main__":

    parser = create_parser()
    args, __ = parser.parse_known_args()
    settings = load_settings(args.settings_file)

    # Load the policy specified by the settings file
    PolicyClass = POLICYS[settings['policy']]
    policy = PolicyClass(**settings['policy_settings'])

    # Initialize a bag
    bag = Bag(**settings['bag_settings'])

    # Initialize a datahandler
    DataHandlerClass = DATAHANDLERS[settings['datahandler']]
    datahandler = DataHandlerClass()

    # Init the experiment
    ExperimentClass = EXPERIMENTS[settings['experiment']]
    experiment = ExperimentClass(
        policy=policy,
        bag=bag,
        datahandler=datahandler,
        **settings['experiment_settings'])

    # Run the experiment
    experiment.run()

    # Process the outcome of the experiment(s)
    experiment.process_results()


    # scores = np.zeros((N, M))
    # for n_orange in range(M):
    #     bought_tokens = {'o1': n_orange}
    #     for i in range(N):
    #         bag = Bag(bought_tokens=bought_tokens)
    #         policy = GoBust()

    #         score, __ = policy.play(bag)
    #         scores[i, n_orange] = score

    # expected_score = np.mean(scores, axis=0)

    # fig, ax = plt.subplots(1, 1)
    # ax.grid(alpha=0.5)
    # ax.scatter(np.arange(0, M), expected_score)
    # ax.set_xticks([*range(M)])
    # ax.set_xlabel('Antal orangea brickor')
    # ax.set_ylabel('Förväntad poäng')
    # fig.savefig('n_orange.png')