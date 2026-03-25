# GRA Swarm Arena

**GRA Swarm Arena** is an abstract, game-like multi-agent simulation: swarms of simple agents move on a 2D grid with hazards (“traps”) and goal cells, trying to reduce the **entropy** of their paths using a simplified GRA-like coordination mechanism.

The project is intended for educational and research purposes:
multi-agent coordination, planning in noisy environments, and experiments
with entropy-based metrics.

---

## Features

- Discrete grid arena (N×N) with different types of traps and goal cells.
- Multiple agent strategies:
  - `random` – purely random walk.
  - `greedy` – naive movement towards a goal.
  - `gra_guided` – uses a simple GRA-like hint to reduce path chaos.
- Basic metrics:
  - path entropy,
  - number of losses (trap hits),
  - average steps to reach goals (for those who succeed).
- Jupyter notebooks for experiments and parameter sweeps.
- Simple matplotlib visualization of the arena and agent paths.

---

## Installation

```bash
git clone https://github.com/USER/gra-swarm-arena.git
cd gra-swarm-arena
pip install -r requirements.txt
