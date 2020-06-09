# Variable-Elimination-SAT

In this project we use a SAT solver tool to select a Variable Elimination ordering thathas the best performance for performing future inference queries to the model.

Variable Elimination can be considered a form of dynamic programming wherewe sum out the variables which are not of interest to us to get the marginal distri-bution of the variables in the query.  To sum up a given variable we find a subsetof factors that mention the given variable. The complexity of this process is expo-nential in the maximum size of the subset formed during the process of summingthe factors.  The complexity can be reduced significantly if we choose the rightvariable elimination order. 
