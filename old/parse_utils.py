import argparse


def create_parser():
    parser = argparse.ArgumentParser()

    # Path to a yaml settings file
    parser.add_argument('--settings-file', type=str, default='settings.yml')

    # Number of times to repeat an experiment
    parser.add_argument('--num-trials', type=int, default=1)

    return parser


def load_settings(yaml_file):
    import yaml
    loader = yaml.SafeLoader
    if yaml_file is not None:
        # Load settings from yaml file
        with open(yaml_file, 'r') as f:
            settings = yaml.load(f, Loader=loader)
    else:
        settings = {}
    return settings