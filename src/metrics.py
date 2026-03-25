import numpy as np
from collections import Counter

def path_entropy(path):
    """
    Simple entropy metric over visited cells.
    """
    counts = Counter(path)
    total = sum(counts.values())
    if total == 0:
        return 0.0
    probs = np.array([c / total for c in counts.values()], dtype=float)
    return float(-np.sum(probs * np.log(probs + 1e-12)))
