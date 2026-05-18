import numpy as np
import matplotlib.pyplot as plt

from game_mechanics_file import Bag
from policies import POLICYS
from experiments import EXPERIMENTS
from datahandlers import DATAHANDLERS
from parse_utils import create_parser, load_settings

if __name__ == "__main__":

    parser = create_parser()
    args, __ = parser.parse_known_args()
    settings = load_settings(args.settings_file)

    ExperimentClass = EXPERIMENTS[settings['experiment']]
    experiment = ExperimentClass(settings)

    # Run the experiment
    experiment.run()

    # Process the outcome of the experiment(s)
    experiment.process_results()
