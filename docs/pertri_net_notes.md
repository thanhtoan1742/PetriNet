# Petri Net

## Motivation
In operation researching, there's a need for a model that:
- Can model processes from "Business process management" which typically serves multiple purposes.
- Can handel concurrency well.

Perti Net is the mathematical model that can satisfy both needs.

## Petri net's definition and properties
### Petri net
A Petri net is a graphical tool (a bipartite graph consisting of places and transitions) for the description and analysis of concurrent processes which arise in systems with many components (distributed systems).

The graphics, together with the rules for their coarsening and refinement, were invented in August 1939 by Carl Adam Petri.

Formally, Petri net is a bipartite graph $N$ of *places* and *transitions*:
$$
N = (P, F, T)
$$
where $P$ is a finite set of *places*, $T$ is a finite set of *transitions*, and $F \subseteq (P \times T) \cup (T \times P)$ is a set of directed arcs.

### Preset and postset
Node $x$ is an input of node $y$ if there an directed arc from $x$ to $y$ i.e. $(x, y) \in F$.

Node $x$ is an output of node $y$ if there an directed arc from $y$ to $x$ i.e. $(y, x) \in F$.

Preset of node $x$ is the set of all input nodes of x denoted as $\bullet x = \{y| (y,x) \in f\}$.

Postset of node $x$ is the set of all output nodes of x denoted as $\bullet x = \{y| (x,y) \in f\}$.


### Tokens and marking
In addition to places and transitions, we have *tokens* which is a special node that can be held by places. A distribution $M$ of tokens across places is called a *marking*. A marked net is a pair $(N, M)$ of a Petri net and a marking.

### Firing
If all input places of a transition contains at least a token, the transition is a *enabled transition*. An enabled transition can fire which will:
- Consumes 1 token from each input places.
- Produces 1 token to each output places.

A enabled transition $t \in T$ at marking $M$ is denoted as $(N, M)[t \rangle$. Firing an enabled transition $t$ will change marking $M$ to marking $M_1 = (M \setminus \bullet t) \uplus t \bullet$. The firing is denoted as $(N, M)[t \rangle (N, M_1)$.

A sequence $\sigma = (t_1, t_2, ..., t_n) \in T^*$ is a firing sequence of marked Petri net $(N, M_0)$ if there exist marking $M_1, M_2, ..., M_n$ that $(N, M_i)[t_{i + 1} \rangle$ and $(N, M_i)[t_{i + 1} \rangle (N, M_{i + 1})$.

### Reachability
Marking $M$ is reachable from initial marking $M_0$ if there a firing sequence  leads $M_0$ to $M$.

The set of all reachable markings is denoted as $[ N, M_0 \rangle$

A *Perti net system* is a Petri net with an initial marking $(N, M_0)$.

### Superimposition

Given 2 Petri nets with the same initial marking $N_1 = (P_1, T1, F1, M_0)$ and $N_2 = (P_2, T2, F2, M_0)$ where $P_i$ could be disjoint, we can "merge" 2 Petri nets together using the superimposing operator.

The superimposing operator is defined as $\oplus : T_1 \times T_2 \longrightarrow T$ where:
- If $\bullet t_1 = \bullet t_2$ them $(t_1, t_2) \mapsto \oplus (t_1, t_2) = t \in T$.
- Else $\bullet t_1 \neq \bullet t_2$ them $(t_1, t_2) \mapsto \oplus (t_1, t_2) = \{t_1, t_2\} \subseteq T$.

The superimposed Petri net is defined as:
$$
N = N_1 \oplus N_2 = (P_1 \cup P_2, T, F_1 \cup F_2, M_0)
$$

### Labeling transition
If we label each transition with a function $l \in \{L: T \longrightarrow A\}$ where $A$ is the set of activity label, we have a *labeled Petri net*. Labeling gives us the ability to treat many transitions as one (by labeling them with the same label) or mark them as invisible (by labeling them with special label $\tau$).

## Modeling with Petri net
Transitions are active nodes of the net which typically represent actions that changes the state of the modeling target. Transitions are typically labeled with verbs.

Places are passive node of the net which when used together with tokes represent state of the modeling target.

A change in states is represented with a change in marking i.e. a change in the distribution of the tokens. A change occurred when an enabled transition fired.

## Petri net's reachability graph
### Transition system
A transition system is a triplet $TS = (S, A, T)$ where $S$ is the set of states, $A$ is the set of activities and $T \subseteq S \times A \times S$ is the set of transitions.

The following subsets are implicitly defined:
- $S^{start} \subseteq S$ is the set of initial states.
- $S^{end} \subseteq S$ is the set of final states.

<!-- properties of transition system -->

### Reachability graph

Given a labeled Petri net $N = (P, T, F, A, l)$ and an initial marking $M_0$, $(N, M_0)$ defines a transition system $TS = (S, A_1, TR)$ where:
- $S = [N, M \rangle, S^{start} = {M_0}$.
- $A_1 = A$.
- $TR = \{(M, l(t), M_1) \in S \times A \times S | \exist t \in T \vee (N, M)[t \rangle (N, M_1)\}$.

$TS$ is the reachability graph of $(N, M_0)$.