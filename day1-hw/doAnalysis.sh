
#!/bin/bash

echo "This Bash script should echo the commands to run FastQC and HISAT on all 24 samples.  e.g."
echo ""
echo "fastqc /Users/cmdb/qbb2015/rawdata/SRR072893.fastq.gz -o /Users/cmdb/qbb2015/assignments/day1-homework"
echo "hisat -p 4 -x /Users/cmdb/qbb2015/genomes/BDGP6 -U /Users/cmdb/qbb2015/rawdata/SRR072893.fastq.gz -S SRR072893.sam"
echo ""
echo "However, there are 6 mistakes!"

FASTQ_DIR="/Users/cmdb/qbb2015/rawdata"
OUTPUT_DIR="/Users/cmdb/qbb2015/assignments/day1-homework"

SAMPLE_PREFIX="SRR072"

GENOME_DIR="/Users/cmdb/qbb2015/genomes/BDGP6"
ANNOTATION="BDGP6.Ensembl.81.gtf"

CORES=4

for i in 893 894 895 896 897 898 899 900 901 902 903 904 905 906 907 908 909 910 911 912 913 914 915 916
do
  echo "fastqc $FASTQ_DIR/$SAMPLE_PREFIX$i.fastq.gz -o $OUTPUT_DIR"
  echo "hisat -p $CORES -x $GENOME_DIR -U $FASTQ_DIR/$SAMPLE_PREFIX$i.fastq.gz -S $SAMPLE_PREFIX$i.sam"
done