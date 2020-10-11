# Water-Measuring-Problem-in-AI
The popular water measuring problem in AI, also referred as Die Hard Water Puzzle is solved using python scripts.

Problem Statement: 

  In this problem, we are given two different containers with different capacities(volume). All we need to do is to 
  measure the given arbitary volume (in between two volumes of containers) which can not be directly measured using two containers.

In order to solve this problem, what I have found from several observations is that it can be solved using recursion.
To solve this problem all we need to do is play with three different set of moves.

  Move1: Fill the larger container

  Move2: Pour the water from larger to smaller container

  Move3: Empty the smaller container

The final desired volume is always in the larger container.
