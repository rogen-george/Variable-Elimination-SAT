# Create a Bayes net given a data set of the form of a csv file
# Returns the graph
from pgmpy.models import BayesianModel
import pandas as pd
import utils

def create_bayes_net(file, edges):
    atts = pd.read_csv(utils.file)
    atts = atts[utils.KEEP_ATTS]
    graph = BayesianModel()
    graph.add_nodes_from(atts.columns)

    # defining the structure of edges
    graph.add_edges_from(utils.edges)

    # fit estimates the CPD tables for the given structure
    graph.fit(atts)

    return graph
