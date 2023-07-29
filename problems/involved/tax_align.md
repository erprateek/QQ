In this exercise, you are provided two fastq.gz files representing paired end sequencing of one Illumina MiSeq library. The sequenced organism is a microbial isolate. You are asked to create a docker image (or other container type) that takes these two fastq.gz files as input and generates two output files.


A csv or txt report including the following fields:

Number of molecules sequenced

Sequencing configuration (read 1, index 1, index 2, and read 2 lengths)

Library type (Nextera or TruSeq)

Mean and standard deviation of library insert sizes after adapter removal

RefSeq or Genbank accession numbers of the sequenced organism.


A plot showing the instrument reported phred scores and alignment inferred quality scores across all positions of read 1 and read 2. Read 1 and Read 2 can be combined on the same plot or separated as 2 plots. The x-axis should represent positions across the read in units of base pairs. The y-axis should represent quality scores, calculated as -10*log10(error rate). Two lines on each plot should represent mean phred qualities reported by the instrument and quality scores inferred from alignment error rates respectively.


Please return the following items in a zipped folder by July 17, 2023


Well commented Dockerfile and associated python/bash scripts to generate the docker image. Please make sure to create any necessary environment inside the docker image.

README explaining how to build and run the Dockerfile, expected memory allocation and execution time. 

Output files from running the docker image: sample.bam and report.txt or report.csv


You may make any reasonable design or formatting choices that are not specified above. Please feel free to reach out with any questions.



Input file #1:


https://drive.google.com/file/d/1L97JR7-9ks9cbIOwN0RU0q1n25bqa-ES/view?usp=sharing



Input file #2: https://drive.google.com/file/d/1Wxopw58beFURnjI9lRtGPz9mumZFqoar/view?usp=sharing