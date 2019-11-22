import os
import sys
import gzip
import argparse


def args_parse():

    parser = argparse.ArgumentParser(description="Find Gene with input")

    parser.add_argument('file_name',
                        type=str,
                        help='specify file input')

    parser.add_argument('gene_name',
                        type=str,
                        help='specify gene name')

    parser.add_argument('out_file_name',
                        type=str,
                        help='specify output file name')

    return parser.parse_args()


def linear_search(key, L):

    for i in range(len(L)):
        if key == L[i]:
            return i

    return -1


def gene_counts(gene_name, output_file, data):
    """
    Description:
    Writes a 'gene_counts file' of specified gene
    ________
    
    gene_name: (str) gene to search for

    output_file: (str) name of the gene_counts output file
    data: (str) name of the file to read data from

    """

    output = open(output_file, 'w')
    version = None
    dim = None
    rna_header = None

    for l in gzip.open(data, 'rt'):

        if version is None:
            version = l
            continue

        if dim is None:
            dim = l
            continue

        if rna_header is None:
            rna_header = l.rstrip().split('\t')
            description_idx = linear_search("Description", rna_header)
            continue

        rna_counts = l.rstrip().split('\t')

        if description_idx == -1:
            print('Gene not found in header')
            sys.exit(1)

        if rna_counts[description_idx] == gene_name:
            for i in range(description_idx + 1, len(rna_header)):
                output.write(rna_header[i] + ': ' + rna_counts[i])
                if i != len(rna_header) - 1:
                    output.write('\n')

            output.close()


def main():
    args = parse_args()
    if (not os.path.exists(args.gene_counts_file)):
        print('Cannot find file')
        sys.exit(1)

    gene_counts(args.gene, args.output_file, args.gene_counts_file)
    sys.exit(0)


if __name__ == '__main__':
    main()
