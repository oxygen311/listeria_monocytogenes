from ete3 import Tree

t = Tree("data_1/listeria_21.newick")

print(t)
print(len(t.get_leaves()))
t.render("listeria_21_test.pdf")