import numpy as np
import matplotlib.pyplot as plt

from game_mechanics import Bag
from policies import GoBust

if __name__ == "__main__":
    
    N = 10000
    M = 16

    scores = np.zeros((N, M))

    for n_orange in range(M):
        bought_tokens = {'o1': n_orange}
        for i in range(N):
            bag = Bag(bought_tokens=bought_tokens)
            policy = GoBust()

            score, __ = policy.play(bag)
            scores[i, n_orange] = score

    expected_score = np.mean(scores, axis=0)

    fig, ax = plt.subplots(1, 1)
    ax.grid(alpha=0.5)
    ax.scatter(np.arange(0, M), expected_score)
    ax.set_xticks([*range(M)])
    ax.set_xlabel('Antal orangea brickor')
    ax.set_ylabel('Förväntad poäng')
    fig.savefig('n_orange.png')