# ShinyPokemon
Simple python code calculating the odds of the number of encounters it takes to find a shiny Pokemon. Made as a probability exercise.

# How it works
If you are starting a shiny hunt in Pokémon and you want to find the odds of finding a shiny pokemon in a certain interval of encounters (e.g. after 1000 encounters, between 500 and 600 encounters, under 100 encounters etc.), you can use this code to do so.

If a user wishes to find the probability with an interval of [a, $\infty$) then the user can add the string 'inf' as the variable b.

# Maths
Used a simple exponential function to model the probability in this case:

$$ f(x) = \frac{1}{\lambda}\exp\left(-\frac{x}{\lambda}\right) $$

with $\lambda$ being the mean number of encounters before finding a shiny (usually 8192 in most games) and $x$ representing the number of encounters.

given an interavl for $x$, the probability for encountering a shiny in this interval is given by

$$ P[a < x < b] = \int_{a}^{b} f(x) dx$$

# Examples

## For a bounded interval 
!(../images/Screenshot 2025-11-03 at 12.08.51.png)
!(../images/graph_bounded_interval.png)

## For an unbounded interval
!(../images/Screenshot 2025-11-03 at 12.09.39.png)
!(../images/graph_unbounded_interval.png)

