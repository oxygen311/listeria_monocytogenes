from bg.grimm import GRIMMReader

file = 'data_1/parebrick_output/5000/preprocessed_data/genomes_permutations_unique.txt'

def get_index(or_and_nums):
    only_nums = [num for or_, num in or_and_nums]
    for i in range(1, 50):
        try:
            return only_nums.index(str(i))
        except ValueError:
            continue

name, ext = file.rsplit('.', 1)

with open(file) as rf:
    with open(name + '_permuted.' + ext, 'w') as wf:
        for line in rf:
            if GRIMMReader.is_genome_declaration_string(line):
                print(line.replace('.', '_'), file=wf, end='')
                continue

            if not GRIMMReader.is_comment_data_string(line) and not GRIMMReader.is_comment_string(line):
                _, or_and_nums = GRIMMReader.parse_data_string(line)
                index_1 = get_index(or_and_nums)

                if or_and_nums[index_1][0] == '-':
                    or_and_nums = [('+' if or_ == '-' else '+', num) for or_, num in or_and_nums[::-1]]
                    index_1 = get_index(or_and_nums)

                cyclic_shift = or_and_nums[index_1:] + or_and_nums[:index_1]

                print(' '.join(or_ + num for or_, num in cyclic_shift), file=wf)