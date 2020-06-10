from pgmpy.inference import VariableElimination
from bayes_net import create_bayes_net
from sat_reduction import run_sat
import numpy as np
import tqdm
import utils
from pprint import pprint
import itertools
import networkx as nx
import argparse
import time
import pandas as pd
from csv import reader
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

def load_args():
    parser = argparse.ArgumentParser(description='arguments')
    parser.add_argument('--dataset', default='celeba', type=str)
    parser.add_argument('--experiments', default=False, type=bool)
    args = parser.parse_args()
    return args


def find_widths(file, keep_atts, edges):
    graph = create_bayes_net(file, keep_atts, edges)
    N = len(keep_atts)
    perms = list(itertools.permutations(keep_atts))
    ATT_DICT = { keep_atts[i] : i+1 for i in range(0, len(keep_atts) ) }
    mgraph = graph.to_markov_model()

    inference = VariableElimination(mgraph)
    max_widths = []
    cliques = []
    dictionaries = []
    sat_runtimes = []
    total_sat_runtime = 0
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
        runtime = 0
        start_time = time.time()
        for width in range(3, N):
            satisfiable, clique, diction = run_sat(width, adj_matrix, keep_atts)
            if satisfiable and width > max_width:
                max_width = width
                curr_clique = clique
                curr_dict = diction
        end_time = time.time()
        runtime = end_time-start_time
        total_sat_runtime += runtime
        max_widths.append(max_width)
        cliques.append(curr_clique)
        dictionaries.append(curr_dict)
        sat_runtimes.append(runtime)
    return np.array(max_widths), cliques, dictionaries, sat_runtimes, total_sat_runtime

def main(file, keep_atts, edges):

    perms = list(itertools.permutations(keep_atts))

    max_widths, cliques, dictionaries, sat_runtimes, total_sat_runtime = find_widths(file, keep_atts, edges)
    min_tree_width_idx = np.argmin(max_widths)
    min_tree_width = np.min(max_widths)
    best_ordering = perms[min_tree_width_idx]
    best_clique = cliques[min_tree_width_idx]
    best_dictionary = dictionaries[min_tree_width_idx]
    graph = create_bayes_net(file, keep_atts, edges)
    mgraph = graph.to_markov_model()
    inference = VariableElimination(mgraph)

    # Perform inference using the best ordering 
    igraph = inference.induced_graph(list(best_ordering))
    graph_size = len(keep_atts)
    density = nx.density(igraph)
    n_edges = igraph.number_of_edges()
    worst_runtime = np.max(sat_runtimes)
    print("Graph size ", graph_size)
    print("Graph density ", density)
    print("Graph edges ", n_edges)
    print("The minimum tree width is " , min_tree_width)
    print ("The best ordering is ", best_ordering)
    print("The worst case SAT runtime is ", worst_runtime)
    print("The total SAT runtime is ", total_sat_runtime)

    return graph_size, density, n_edges, worst_runtime, total_sat_runtime


# will just run this on the celebrity data
# it's possible to run it with mushrooms
# but need to correctly specify the set of nodes/edges you wish to check
# here I hardcoded everything
def experiments(file):
    g_sizes = []
    sat_runtimes = []
    for i in range(len(utils.EXPERIMENTAL_ATTS)):
        graph_size, density, n_edges, worst_runtime, total_runtime = main(file, utils.EXPERIMENTAL_ATTS[i], utils.EXPERIMENTAL_EDGES[i])
        g_sizes.append(graph_size)
        sat_runtimes.append(total_runtime)

    # NOTE: had to manually add size 8 onto the plot by running in a notebook with modified functions
    # saving everything to lists ran out of RAM...
    # by default, this will run up to size 7 - any higher takes a long time
    g_sizes.append(8)
    sat_runtimes.append(722)
    plt.title('SAT Runtime vs Number of Random Variables')
    plt.plot(g_sizes, sat_runtimes, 'r-.')
    plt.xlabel('Number of Variables')
    plt.ylabel('SAT Runtime (sec)')
    plt.savefig('./figures/runtime.png')
    plt.close('all')

    plt.title('SAT Runtime vs Number of Random Variables (logscale)')
    plt.plot(np.log(g_sizes), np.log(sat_runtimes), 'g-.')
    plt.xlabel('Number of Variables')
    plt.ylabel('SAT Runtime (sec)')
    plt.savefig('./figures/runtime_log.png')
    plt.close('all')

    e_nums = []
    sat_runtimes = []
    for i in range(len(utils.EXPERIMENTAL_ATTS_2)):
        graph_size, density, n_edges, worst_runtime, total_runtime = main(file, utils.EXPERIMENTAL_ATTS_2[i], utils.EXPERIMENTAL_EDGES_2[i])
        e_nums.append(n_edges)
        sat_runtimes.append(total_runtime)
    plt.title('SAT Runtime vs Number of Edges')
    plt.plot(e_nums, sat_runtimes, 'r-.')
    plt.xlabel('Number of Edges')
    plt.ylabel('SAT Runtime (sec)')
    plt.savefig('./figures/runtime_edges.png')
    plt.close('all')

    plt.title('SAT Runtime vs Number of Edges (logscale)')
    plt.plot(np.log(e_nums), np.log(sat_runtimes), 'g-.')
    plt.xlabel('Number of Edges')
    plt.ylabel('SAT Runtime (sec)')
    plt.savefig('./figures/runtime_log_edges.png')
    plt.close('all')
    print('Done')



if __name__=='__main__':
    args = load_args()
    # mushroom dataset loads RV's and edges from files

    if args.experiments:
        print('Experiments on Celebrity Data', end='\n\n')
        file = './data/list_attr_celeba.csv'
        experiments(file)
        exit(0)
    if args.dataset == 'mushroom':
        print('Mushrooms Data', end='\n\n')
        file = './data/mushrooms.csv'
        keep_atts = pd.read_csv('./graph/mushroom_atts.csv', header=None).values[0].astype(str)
        edges = []
        with open('./graph/mushroom_edges.csv', 'r') as read_obj: 
            csv_reader = reader(read_obj) 
            list_of_rows = list(map(tuple, csv_reader)) 
            edges = list_of_rows
        _,_,_,_,_ = main(file, keep_atts, edges)
        
    # celeb dataset loads RV's and edges from files
    elif args.dataset == 'celeba':
        print('Celebrity Data', end='\n\n')
        file = './data/list_attr_celeba.csv'
        keep_atts = pd.read_csv('./graph/celeb_atts.csv', header=None).values[0].astype(str)
        edges = []
        with open('./graph/celeb_edges.csv', 'r') as read_obj: 
            csv_reader = reader(read_obj) 
            list_of_rows = list(map(tuple, csv_reader)) 
            edges = list_of_rows
        _,_,_,_,_ = main(file, keep_atts, edges)
    else:
        print('Wrong dataset')
