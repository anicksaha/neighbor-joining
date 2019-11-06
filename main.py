from utils_io import read_fasta_file
from utils_io import write_distance_file
from utils import get_difference_matrix
import sys

def main(filename):
    # read the fna file and return the ids and id sequence mappings
    ids, id_sequences = read_fasta_file(filename)

    # generate the difference matrix
    distance_matrix = get_difference_matrix(ids, id_sequences)

    # write the distances.txt file (distance matrix)
    write_distance_file(ids, distance_matrix)

if __name__ == '__main__':
    main(sys.argv[1])