import numpy as np

MOVES = [(1, 0), (-1, 0), (0, 1), (0, -1)]

class Agent:
    def __init__(self, start_pos, strategy="random", vision_radius=1, rng=None):
        self.start_pos = tuple(start_pos)
        self.pos = tuple(start_pos)
        self.strategy = strategy
        self.vision_radius = vision_radius
        self.path = [self.pos]
        self.alive = True
        self.reached_goal = False
        self.rng = rng or np.random.RandomState()

    def reset(self):
        self.pos = self.start_pos
        self.path = [self.pos]
        self.alive = True
        self.reached_goal = False

    def step(self, arena, gra_hint=None):
        if not self.alive or self.reached_goal:
            return self.pos

        if self.strategy == "random":
            move = self.rng.choice(MOVES)
        elif self.strategy == "greedy":
            move = self._greedy_move(arena)
        elif self.strategy == "gra_guided" and gra_hint is not None:
            move = gra_hint(self, arena)
        else:
            move = self.rng.choice(MOVES)

        new_pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        if arena.in_bounds(new_pos):
            self.pos = new_pos
            self.path.append(self.pos)
        return self.pos

    def _greedy_move(self, arena):
        goals = [tuple(g) for g in arena.goal_positions]
        gx, gy = goals[0]
        dx = int(np.sign(gx - self.pos[0]))
        dy = int(np.sign(gy - self.pos[1]))
        candidates = [(dx, 0), (0, dy)]
        move = self.rng.choice(candidates)
        return move
