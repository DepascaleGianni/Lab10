from model.model import Model

m = Model()
m.build_graph(1980)
for el in m._sol_graph.degree:
    if el[1] == 0:
        print(el)
m.printable_graph()
n = m.number_conn_comp()
