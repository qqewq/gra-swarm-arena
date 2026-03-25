from .metrics import path_entropy
import numpy as np

class GRACoordinator:
    """
    Game-level GRA-like coordinator:
    evaluates path entropy and gives hints to agents
    to avoid overly chaotic trajectories.
    """
    def __init__(self, entropy_weight=1.0, reset_threshold=0.7):
        self.entropy_weight = entropy_weight
        self.reset_threshold = reset_threshold

    def evaluate_agents(self, agents):
        entropies = [path_entropy(a.path) for a in agents]
        return np.array(entropies, dtype=float)

    def gra_hint_fn(self, arena):
        """
        Returns a simple hint function for gra_guided strategy.
        """

        def hint(agent, arena_inner):
            from .agents import MOVES
            best_move = None
            best_score = 1e9
            for mv in MOVES:
                new_pos = (agent.pos[0] + mv[0], agent.pos[1] + mv[1])
                if not arena_inner.in_bounds(new_pos):
                    continue
                visits = agent.path.count(new_pos)
                score = visits
                if score < best_score:
                    best_score = score
                    best_move = mv
            if best_move is None:
                best_move = (0, 0)
            return best_move

        return hint
