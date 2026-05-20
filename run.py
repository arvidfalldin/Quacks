from engine.chips import Chip, ChipColor
from engine.player import Player
from engine.environment import QuacksEnvironment

from policy.policy import AlwaysExplodePolicy, StopAtProbabilityPolicy


def quantitative_test_1():

    player1 = Player("Alice")
    env = QuacksEnvironment(player1)

    coins = []
    exploded = []

    # Add a bunch of orange chips to the bag to test the policy
    for _ in range(20):
        player1.bag.add(Chip(color=ChipColor.ORANGE, value=1))

    for i in range(1000):
        # Create a brewing policy for the player
        # policy = AlwaysExplodePolicy()
        policy = StopAtProbabilityPolicy(0.0)
        obs, done = env.reset()

        while not done:
            action = policy(obs)
            obs, done = env.step(action)

        coins.append(obs.pot.current_coins())
        exploded.append(obs.pot.has_exploded())

    import matplotlib.pyplot as plt

    samples = [(c, e) for c, e in zip(coins, exploded)]

    # Compute the explosion rate under this policy
    explosion_rate = sum(e for _, e in samples) / len(samples)
    print(f"Explosion rate: {explosion_rate:.2%}")

    # Split by boolean
    true_values = [n for n, u in samples if u]
    false_values = [n for n, u in samples if not u]

    # Histogram bins
    bins = range(min(n for n, _ in samples),
                max(n for n, _ in samples) + 2)

    # Stacked histogram
    fig, ax = plt.subplots()
    ax.hist(
        [true_values, false_values],
        bins=bins,
        stacked=True,
        label=["Exploded", "Not Exploded"]
    )

    ax.set_xlabel("n")
    ax.set_ylabel("count")
    ax.legend()
    fig.savefig("Outcome1.png", bbox_inches='tight', dpi=300)

def quantitative_test_2():

    player1 = Player("Alice")
    env = QuacksEnvironment(player1)


    # Add a bunch of orange chips to the bag to test the policy
    for _ in range(10):
        player1.bag.add(Chip(color=ChipColor.ORANGE, value=1))

    import numpy as np
    thresholds = np.linspace(0.0, 1.0, num=40)

    explosion_rates = []
    coin_averages = []

    for threshold in thresholds:
        coins = []
        exploded = []
        for i in range(10000):
            # Create a brewing policy for the player
            # policy = AlwaysExplodePolicy()
            policy = StopAtProbabilityPolicy(threshold)
            obs, done = env.reset()

            while not done:
                action = policy(obs)
                obs, done = env.step(action)

            coins.append(obs.pot.current_coins())
            exploded.append(obs.pot.has_exploded())

        samples = [(c, e) for c, e in zip(coins, exploded)]

        # Compute the explosion rate under this policy
        explosion_rate = sum(e for _, e in samples) / len(samples)
        explosion_rates.append(explosion_rate)

        # Compute the average coins under this policy
        average_coins = sum(c for c, _ in samples) / len(samples)
        coin_averages.append(average_coins)

    import matplotlib.pyplot as plt
    fig, ax1 = plt.subplots(1, 1, figsize=(8, 6))
    ax1.plot(thresholds, explosion_rates, label="Explosion Rate")
    
    # Draw x=x as a reference line
    ax1.plot(thresholds, thresholds, color='gray', linestyle='--', label="y=x")
    ax1.set_xlabel("Threshold")
    ax1.set_ylabel("Value")
    ax1.legend()

    ax2 = ax1.twinx()
    ax2.plot(thresholds, coin_averages, color='red',
             label="Average Coins")
    ax2.set_ylabel("Value")
    ax2.legend(loc="lower right")
    fig.savefig("Outcome2.png", bbox_inches='tight', dpi=300)


def main():
    player1 = Player("Alice")
    env = QuacksEnvironment(player1)

    # Add a bunch of orange chips to the bag to test the policy
    for _ in range(5):
        player1.bag.add(Chip(color=ChipColor.ORANGE, value=1))


    policy = StopAtProbabilityPolicy(0.0)
    obs, done = env.reset()
    while not done:
        action = policy(obs)
        obs, done = env.step(action)
    
    print(env.pot)

if __name__ == "__main__":
    # quantitative_test1()
    quantitative_test_2()
    # main()

