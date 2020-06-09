from pgmpy.inference import VariableElimination
from bayes_net import create_bayes_net
from sat_reduction import run_sat
import numpy as np
import tqdm
import utils
from pprint import pprint
import itertools
import networkx as nx

def main():
    graph = create_bayes_net(utils.file, utils.edges)
    N = len(utils.KEEP_ATTS)
    perms = list(itertools.permutations(utils.KEEP_ATTS))
    ATT_DICT = { utils.KEEP_ATTS[i] : i+1 for i in range(0, len(utils.KEEP_ATTS) ) }
    mgraph = graph.to_markov_model()

    inference = VariableElimination(mgraph)
    max_widths = []
    cliques = []
    dictionaries = []
    for perm in tqdm.tqdm(perms):
        adj_matrix = np.zeros((N, N))
        igraph = inference.induced_graph(list(perm))

        edges = igraph.edges
        for ed in edges:
            first, second = ed
            first = ATT_DICT[first] - 1
            second = ATT_DICT[second] - 1
            adj_matrix[first, second] = 1
            adj_matrix[second, first] = 1
            adj_matrix[first, first] = 1
            adj_matrix[second, second] = 1
        adj_matrix = adj_matrix.astype(bool)
        max_width = 0
        curr_clique = []
        curr_dict = {}
        for width in range(3, N):
            satisfiable, clique, diction = run_sat(width, adj_matrix)
            if satisfiable and width > max_width:
                max_width = width
                curr_clique = clique
                curr_dict = diction
        max_widths.append(max_width)
        cliques.append(curr_clique)
        dictionaries.append(curr_dict)

    return np.array(max_widths), cliques, dictionaries

perms = list(itertools.permutations(utils.KEEP_ATTS))

max_widths, cliques, dictionaries = main()
min_tree_width_idx = np.argmin(max_widths)
min_tree_width = np.min(max_widths)
best_ordering = perms[min_tree_width_idx]
best_clique = cliques[min_tree_width_idx]
best_dictionary = dictionaries[min_tree_width_idx]
#print(best_clique)
#pprint(best_dictionary)
graph = create_bayes_net(utils.file, utils.edges)
mgraph = graph.to_markov_model()
inference = VariableElimination(mgraph)
# Perform inference using the best ordering 
igraph = inference.induced_graph(list(best_ordering))
print("The minimum tree width is " , min_tree_width)
print ("The best ordering is ", best_ordering)
#print(nx.graph_clique_number(igraph))
#nx.draw(igraph)
#print(igraph.nodes)
#print(igraph.edges)
