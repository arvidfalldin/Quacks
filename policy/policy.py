
from policy.policy_utils import explosion_probability


class BrewingPolicyBase:
    def __init__(self, name: str):
        self.name = name

    def __call__(self, observation):
        raise NotImplementedError("Policy must implement __call__ method.")
    
class AlwaysExplodePolicy(BrewingPolicyBase):
    def __init__(self):
        super().__init__("AlwaysExplode")

    def __call__(self, observation):
        return 1  # Draw a chip no matter what

class StopAtProbabilityPolicy(BrewingPolicyBase):
    """
    This brewing policy will stop drawing chips when the probability of
    explosion exceeds a certain threshold.
    """
    def __init__(self, threshold: float):        
        super().__init__(f"StopAtProbability_{threshold}")
        self.threshold = threshold

    def __call__(self, observation):
        pot, bag = observation.pot, observation.bag
        prob = explosion_probability(pot, bag)

        return 1 if prob <= self.threshold else 0