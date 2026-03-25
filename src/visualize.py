import matplotlib.pyplot as plt
from pathlib import Path
import yaml

from .arena import Arena
from .agents import Agent
from .gra_core import GRACoordinator
from .metrics import path_entropy


def run_simulation_for_viz():
    """Run one simulation episode and return arena + agents."""
    arena = Arena("config/arena_default.yaml")
    cfg_agents = yaml.safe_load(Path("config/agents_default.yaml").read_text(encoding="utf-8"))

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

    return arena, agents


def plot_arena_and_paths(arena, agents, show_entropies=True):
    size = arena.size

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(-0.5, size - 0.5)
    ax.set_ylim(-0.5, size - 0.5)
    ax.set_aspect("equal")

    # draw grid
    for x in range(size + 1):
        ax.axhline(x - 0.5, color="lightgray", linewidth=0.3)
        ax.axvline(x - 0.5, color="lightgray", linewidth=0.3)

    # draw traps
    trap_x = [pos[0] for pos in arena.traps.keys()]
    trap_y = [pos[1] for pos in arena.traps.keys()]
    ax.scatter(trap_y, trap_x, c="red", marker="s", s=40, label="traps")

    # draw goals
    goal_x = [g[0] for g in arena.goal_positions]
    goal_y = [g[1] for g in arena.goal_positions]
    ax.scatter(goal_y, goal_x, c="green", marker="s", s=60, label="goals")

    # draw paths
    colors = ["blue", "orange", "purple", "cyan", "magenta", "brown"]
    for i, ag in enumerate(agents):
        xs = [p[0] for p in ag.path]
        ys = [p[1] for p in ag.path]
        color = colors[i % len(colors)]
        ax.plot(ys, xs, "-", color=color, alpha=0.7)
        ax.scatter(ys[0], xs[0], color=color, marker="o", s=30)  # start
        if ag.reached_goal:
            ax.scatter(ys[-1], xs[-1], color=color, marker="*", s=60)  # end

    if show_entropies:
        ents = [path_entropy(a.path) for a in agents]
        mean_ent = sum(ents) / len(ents)
        ax.set_title(f"GRA Swarm Arena\nMean path entropy: {mean_ent:.3f}")
    else:
        ax.set_title("GRA Swarm Arena")

    ax.invert_yaxis()
    ax.legend(loc="upper right", fontsize=8)
    plt.tight_layout()
    plt.show()


def main():
    arena, agents = run_simulation_for_viz()
    plot_arena_and_paths(arena, agents)


if __name__ == "__main__":
    main()
