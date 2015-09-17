# PrimitiveRecommenderSystem
A very primitive type of recommender system

### Data

The data for this assignment will be the MovieLens dataset
[MovieLens](http://grouplens.org/datasets/movielens/)

### Task

There are four parts to this assignment

- Write a MapReduce job to compute the frequency of co-occurrence for every pair of movies that receive a "High" ranking from the same user (the frequency is the number of users that give this ranking to both of the movies). High ranking corresponds to a 4 or a 5 ranking in the ratings file. You must do this using the 'pairs' and the 'stripes' approach (Lin & Dyer's book). Use different sizes of the dataset to obtain a graph similar to Figure 3.10 in the book. Then, output the most frequent 20 pairs by using the movie names in the movie data file (not the IDs)

- Modify your program above to compute the conditional probability P(B/A) where A,B are movies. (This is exactly what Lin calls relative frequency.). Use the 'pairs' approach to do this. And output the names (both A and B) of the movies whose conditional probability exceeds 0.8. (This can be used as a primitive way to recommend movie B to customers that rent movie A and like it.). Graph the time needed for this vs. size of the dataset.

- Further modify your programs to compute the lift between two movies. (Recall that lift(AB)=P(AB)/(P(A)*P(B))=P(A|B)/P(A)) Again, plot the time vs. size graph, and output pairs whose lift is greater than 1.5 (What does this mean?)

- Use the SON algorithm in MapReduce to compute all itemsets (groups of movies) that frequently receive high ranking by users. Tune your support so that the output is not overwhelming