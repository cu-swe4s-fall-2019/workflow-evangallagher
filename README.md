# Assignment 10: Workflow

## Files
There are two main files used to create plots using this repository:

"GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz"
"GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt"

## Modules
**get_gene_counts:** this module searches the data set for amount of times a keyword gene is given.

**get_tissue_samples:** this module searches for a specified tissue type

**box.py:** this is the file that executes a function to create a boxplot for the data

**Snakefile:** a file that is used to run all previous modules at once

## How to use

To use functions, open terminal. All three files must be made executable with:

```
chmod +x test_func_get_gene_counts.sh
chmod +x test_get_tissue_sample.sh
chmod +x test_box.sh
```

Now, simply run snakemake in the terminal to complete 
