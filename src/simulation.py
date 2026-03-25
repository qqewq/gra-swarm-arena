from pathlib import Path
import yaml

from .arena import Arena
from .agents import Agent
from .gra_core import GRACoordinator
from .metrics import path_entropy

def run_simulation():
    arena = Arena("config/arena_default.yaml")
    cfg_agents = yaml.safe_load(Path("config/agents_default.yaml").read_text(encoding="utf-8"))
    cfg_rules = yaml.safe_load(Path("config/game_rules.yaml").read_text(encoding="utf-8"))

    import numpy as np
    rng = np.random.RandomState(0)

    agents = []
    strategies = cfg_agents["strategies"]
    for i in range(cfg_agents["num_agents"]):
        start = arena.start_positions[0]
        strat = strategies[i % len(strategies)]
        agents.append(
            Agent(
                start_pos=start,
                strategy=strat,
                vision_radius=cfg_agents["vision_radius"],
                rng=rng,
            )
        )

    gra = GRACoordinator(**cfg_agents["gra_params"])
    gra_hint = gra.gra_hint_fn(arena)

    max_steps = cfg_agents["max_steps"]
    for _ in range(max_steps):
        for ag in agents:
            if ag.strategy == "gra_guided":
                ag.step(arena, gra_hint)
            else:
                ag.step(arena)

    entropies = [path_entropy(a.path) for a in agents]
    mean_entropy = sum(entropies) / len(entropies)
    print("Mean path entropy:", mean_entropy)

if __name__ == "__main__":
    run_simulation()
