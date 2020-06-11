# Variable-Elimination-SAT

In this project we use a SAT solver tool to select a Variable Elimination ordering that has the best performance for performing future inference queries to the model.

Variable Elimination can be considered a form of dynamic programming where we sum out the variables which are not of interest to us to get the marginal distribution of the variables in the query.  To sum up a given variable we find a subset of factors that mention the given variable. The complexity of this process is exponential in the maximum size of the subset formed during the process of summing the factors.  The complexity can be reduced significantly if we choose the right variable elimination order. 

Instructions:

	> python main.py --help --experiments <True/False> --brute <True/False> --dataset <celeba/mushroom>

	--help gives an argument summary.

	--dataset will specify which dataset to use. This should be run alone (no --experiments or --brute flags) The files mushroom_atts.csv, mushroom_edges.csv can be modified for graph structure on mushroom data. Similarly, celeb_atts.csv and celeb_edges.csv can be modified for the celeba data.

	--experiments will run sections 6.1 and 6.2 from the report (SAT runtime analysis). If True and --brute is False, it will only run this section. By default it runs on celeba data and would require modifications to perform on mushroom data.

	--brute will find the best ordering for the celeba graph specified by the two files celeb_atts.csv and celeb_edges.csv, just as with the --dataset flag, but will use NetworkX instead of SAT

File Modifications:

	The attribute files, mushroom_atts.csv and celeb_atts.csv, should be in a single row format and contain only names from the headers for the respective data set. Names should be given in no particular order, separated by commas, on one line. This specifies the set of random variables in the graph.

	The edges files, mushroom_edges.csv and celeb_edges.csv, should have an edge a -> b defined as a,b in each row. That is, each row specifies a directed edge from random variable a to random variable b. Only random variables specified in the attributes file associated with a given data set should be listed here. Also, there is no checking for cycles or duplicates, but these should be excluded or else the graph will not function properly. 
