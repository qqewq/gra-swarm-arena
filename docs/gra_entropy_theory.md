# GRA and Entropy (short outline)

This project uses a very simplified idea inspired by "GRA" concepts:
- Treat agent behaviour as a source of "foam" (messy, chaotic trajectories).
- Define a simple entropy metric over paths.
- Introduce a coordinator that tries to reduce this entropy by nudging agents
  towards cleaner, less redundant paths.

In this toy setting:
- GRA-like logic is just a function that scores trajectories and suggests
  low-entropy moves.
- It can be extended for more sophisticated research, e.g.:
  - multi-objective planning,
  - resource allocation,
  - information filtering.

The emphasis here is on **abstract multi-agent behaviour** and **entropy
minimization**, not on any real-world combat use.
