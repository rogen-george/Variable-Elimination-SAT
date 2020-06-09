import utils
import numpy as np
import pandas as pd
from pgmpy.models import BayesianModel
from pgmpy.inference import VariableElimination

def print_cpd_tables(graph):
    for cpd in graph.get_cpds():
        print(cpd)

# targets are nodes we want to return CPD for
# given evidence nodes and values
# targets = list, evidence = dictionary
def graph_inference(graph, targets, evidence):
    inf = VariableElimination(graph)
    query = inf.query(variables=targets, evidence=evidence)
    print(query)
#     for t in targets:
#         print(query[t])
#         print(query[t].variables, query[t].values)

    return query

def return_marginals(graph, batch_size, evidence):
    df = pd.DataFrame(columns=utils.KEEP_ATTS)

    targets = []
    for val in KEEP_ATTS:
        if val not in evidence.keys():
            targets.append(val)
    query = graph_inference(graph, targets, evidence)

    # just repeat it for the entire batch, since we want to pass the same evidence in
    for i in range(batch_size):
        for val in KEEP_ATTS:
            if val not in targets:
                df.loc[i, val] = evidence[val]
                #print(val, 1)
            else:
                df.loc[i, val] = query[val].values[1]
                #print(val, query[val].values[1])

    df = df.apply(pd.to_numeric, downcast='float', errors='coerce')
    return df.values
