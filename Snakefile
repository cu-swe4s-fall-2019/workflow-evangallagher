GENES = ["SDHB", "MEN1", "KCNH2", "MSH2", "MYL2", "BRCA2"]
TISSUES = ["Brain", "Heart", "Blood", "Skin"]

rule all:
    input:
        '-'.join(TISSUES) + '_' + '-'.join(GENES) +'.png'

rule gene_sample_counts:
    input:
        'GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz?raw=true.gz'
    output:
        expand('{gg}_counts.txt', gg=GENES)
    shell:
        'for GG in {GENES}; do ' \
        + 'python get_gene_counts.py, {input}; '


rule tissue_samples:
    input:
        'GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt'
    output:
        expand('{tg}_samples.txt', tg=TISSUE_GROUP)
    shell:
        'python get_tissue_samples.py, {input}'


rule box_plot:
    input:
        rules.tissue_samples.output,
        rules.gene_sample_counts.output
    output:
        'Brain-Heart-Blood-Skin_SDHB-MEN1-KCNH2-MSH2-MYL2-BRCA2.png'
    shell:
        'python box.py {output} \"{GENES}\"  \"{TISSUES}\" {TISSUE_GROUP}_samples.txt'
