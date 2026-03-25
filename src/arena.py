import numpy as np
import yaml
from pathlib import Path

class Arena:
    def __init__(self, config_path: str):
        cfg = yaml.safe_load(Path(config_path).read_text(encoding="utf-8"))
        self.size = cfg["grid_size"]
        self.num_traps = cfg["num_traps"]
        self.trap_types = cfg["trap_types"]
        self.start_positions = cfg["start_positions"]
        self.goal_positions = cfg["goal_positions"]
        self.random = np.random.RandomState(cfg.get("random_seed", 0))
        self.grid = np.zeros((self.size, self.size), dtype=int)
        self.traps = {}
        self._place_traps()

    def _place_traps(self):
        positions = set()
        while len(positions) < self.num_traps:
            x = self.random.randint(0, self.size)
            y = self.random.randint(0, self.size)
            if (x, y) in positions:
                continue
            positions.add((x, y))
        for (x, y) in positions:
            self.grid[x, y] = 1
            # simple: assign first trap type penalty
            self.traps[(x, y)] = self.trap_types[0]["penalty"]

    def is_trap(self, pos):
        return tuple(pos) in self.traps

    def in_bounds(self, pos):
        x, y = pos
        return 0 <= x < self.size and 0 <= y < self.size

    def is_goal(self, pos):
        return list(pos) in self.goal_positions
