# PageRank-implementation-from-scratch-in-python

In this repo we demonstrate page rank algorithm usefulness for graph data.

Page rank algorithm's first aim is to learn a static probability distribution. We have multiple states stored within a graph data structue what's the likeliness for a random walker to end-up in a particular states at a given timestep. It works for all markov chains and particularly usefull for reductible markov chains like the one shown below :

![Alt text](/demo_images./markov_chains.png?raw=true "Reductible markov chain") 

This chain is called reductible since there's a couple states which once visited by the walker won't let him return outside states 1 and 2 in the left chain are an illustration of this. Once the walker get into state one or two, He won't be able to visit 0 or 3 because he will be trapped inside and bounce back and forth from 1 and 2 infinetly. 

The right chain is also reductible,in fact the random walker can be easily trapped in state 2. In general we don't want to end-up stuck in a state infinetly. Even when we model real-word systems, it's rare for a system to end-up trapped in particular states forever. There will always be room for all possibilities. A web surfer for example isn't likely to stay in a webpage forever but can still transition to all other webpages.

From a modelling standpoint we define a probability Beta called damping factor, such that with probability Beta, the walker will move according to the  usual transition matrix (which mean he will stay trapped in those states) or he will move randomly to any other normal states with probability 1-Beta
The new transition matrix will look like :

![Alt text](/demo_images./new_transition_matrix.png?raw=true "Reductible markov chain") 

with P being the usual transition matrix and 

![Alt text](/demo_images./vectors.png?raw=true "Reductible markov chain") 

# Interpretations

n being the number of states in the graph, the vectors e refers to a uniform probability distribution over all the states in the graph multiplied by 1-Beta (this product can be interpreted as join probability between the two event (not following P usual transition rates 1-Beta, transition to any possible state (veT). The component (1-Beta)veT is what models that the fact that a random walker who got into a dead end (a web page with no outlinks) can jump to any other webpage. The closer Beta is to 1, the least likely it's that the walker will jump to other webpages after a dead end, we should aim for higher values if our graph of states doesn't contains dead ends. While the closer it's to 0 the more likely it's for the walker to jumpy from one state to another following a uniform probability distribution, in this case we lose a lot of informations about the relationships between the states which is undesirable. Therefore Beta parameter should be tweaked carefully to be as close to 1 as possible.

# How to use 
We apply the learning process to the following chain :

![Alt text](/demo_images./example.png?raw=true "Reductible markov chain") 

run : python3 main.py

The first input should be the number of states followed by ID's and initial pagerank values

![Alt text](/demo_images./graphnodes.png?raw=true "Reductible markov chain") 

Then the links between nodes

![Alt text](/demo_images./edges1.png?raw=true "Reductible markov chain") 

![Alt text](/demo_images./edges2.png?raw=true "Reductible markov chain")

Then parameters iterations, damping factors

![Alt text](/demo_images./para.png?raw=true "Reductible markov chain")

The algorithm outputs the pagerank values after learning from the R matrix, ranked from the highest to lowest 

![Alt text](/demo_images./ranke.png?raw=true "Reductible markov chain") 




