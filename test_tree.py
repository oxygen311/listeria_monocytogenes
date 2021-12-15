from ete3 import Tree


from parebrick.utils.data.parsers import parse_infercars_to_df

t = Tree("bifidobact/bifidobact_all.nwk")

print(t)
print(len(t.get_leaves()))
t.render("listeria_21_test.pdf")

df = parse_infercars_to_df('bifidobact/parebrick_output/5000/preprocessed_data/blocks_coords.infercars')

set_blocks = set(df.species)
set_tree = set(n.name for n in t.get_leaves())

print(set_blocks)
print(set_tree)

print(len(set_blocks))
print(len(set_tree))

print(len(set_tree & set_blocks))

print(set_blocks - (set_tree & set_blocks))
print(set_tree - (set_tree & set_blocks))