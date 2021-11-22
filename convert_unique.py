from parebrick.utils.data.unique_gene_filters import grimm_filter_unique_gene


in_file = 'bifidobact/blocks/5000/genomes_permutations.txt'
out_file = in_file.replace('.txt', '_unique.txt')

grimm_filter_unique_gene(in_file, out_file, 100)