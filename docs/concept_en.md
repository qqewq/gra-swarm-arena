# GRA Swarm Arena — Concept

GRA Swarm Arena is an abstract grid-based multi-agent simulation.

A number of agents move across a discrete arena that contains:
- neutral cells,
- "trap" cells with some penalty,
- goal cells.

Agents can use different strategies (random, greedy, GRA-guided) to reach
the goals. We measure how "chaotic" their trajectories are using a simple
entropy metric over visited cells.

A simplified GRA-like mechanism is used to:
- evaluate the entropy of paths,
- provide hints that encourage agents to avoid overly repetitive or chaotic paths.

The model is not tied to any real-world weapons, air defenses, or military
applications. It is meant as a **game / educational simulation** for
experiments with multi-agent coordination and entropy-based reasoning.
