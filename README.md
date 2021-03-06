# GDC VEP Tool
![Version badge](https://img.shields.io/badge/VEP-v84-<COLOR>.svg)

Contains VEP plugins, utility scripts, and a dockerfile for running the VEP pipeline.
See https://github.com/NCI-GDC/vep-cwl for more information about the GDC workflow
associated with this.

## VEP Plugins

We have only tested these plugins on the software dependencies listed in the
Dockerfile:

* BioPerl 1.6.924
* VEP v84

All of these plugins require tabix to be installed and in your `PATH` which is often
installed automatically (via htslib) during the VEP installation process.

### Entrez

The `GDC_entrez.pm` plugin uses a pre-populated JSON file containing mappings from GENCODE to
Entrez identifiers. The JSON file can be created using the `vep-plugins/utils/make_ensembl_entrez_json.py`
script. The required input files for generating the JSON are:

* Gencode Entrez Gene IDs file: `ftp://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_22/gencode.v22.metadata.EntrezGene.gz`
* NCBI human gene info file: `ftp://ftp.ncbi.nih.gov/gene/DATA/GENE_INFO/Mammalia/Homo_sapiens.gene_info.gz`

__Note: The NCBI file is not versioned, so it may differ.__

VEP Usage: `--plugin GDC_entrez,<entrez_ensembl.json>`

### Evidence

The `GDC_evidence.pm` plugin uses the tabix-indexed VEP evidence VCF to add in the evidence values for dbSNP
annotations.

VEP Usage: `--plugin GDC_evidence,<variation.vcf.gz>`
