from pysat.solvers import Glucose3
import utils
import numpy as np


# k-clique to sat reduction
# uses adjacency matrix for graph
def run_sat(K, adj_matrix, keep_atts):
    g = Glucose3()
    N = len(keep_atts)
    K = K
    temp = {}
    for i in range( N *K):
        indx = i% N
        pass_num = i // N + 1

        temp[i + 1] = keep_atts[indx] + str('_') + str(pass_num)
    # pprint(temp)
    idxes = np.arange(1, N * K + 1).reshape(K, N).astype(int)

    # is variable the rth element of clique?
    # print('***First Clauses***')
    for k in range(K):
        # print(np.arange(k*N+1, (k+1)*N+1).tolist())
        g.add_clause(np.arange(k * N + 1, (k + 1) * N + 1).tolist())

    # can't be rth and sth nodes of clique
    # print('\n***Second Clauses***')
    for i in range(idxes.shape[1]):
        curr_variable = idxes[:, i]
        for j in range(len(curr_variable) - 1):
            for w in range(j + 1, len(curr_variable)):
                clause_t = [-int(curr_variable[j]), -int(curr_variable[w])]
                # print(clause_t)
                g.add_clause(clause_t)

    # print('\n***Third Clauses***')
    for r in range(K):  # [0, 1, 2]
        for s in range(K):  # [0, 1, 2]
            if r != s:
                for i in range(N - 1):  # [0, ..., 8]
                    for j in range(i + 1, N):  # [1, ..., 9]
                        is_edge_ij = adj_matrix[i, j]
                        if is_edge_ij == False:
                            var_1 = idxes[r, i]
                            var_2 = idxes[s, j]
                            g.add_clause([-int(var_1), -int(var_2)])
                            # print([-var_1, -var_2])

    # can't be in the same clique if no edges between
    satisfiable = g.solve()
    clique = g.get_model()
    # print(satisfiable)
    # print(g.get_model())

    return satisfiable, clique, temp
