## Question

Write a script that can take in a file as input and output the following:
- Whether or not it is a valid non-zero sized file
- Whether or not it is a valid VCF file
- Separate header and content of the VCF file into 2 separate variables
- Print the reference assembly that the VCF was used to generate it
- Extract how many types of each variant - SNV Indels are present on each chromosome
- Output that content on the screen


Note:
VCF file contains information about 1 sample only
Familiarize and get used to argparse - we will extend this problem as well in a subsequent version

*** NEW ***
- Add in a command line flag to accept a bed file as input
- Add in a feature to generate the bed intersect (You can use bedtools intersect)
- Output should first be a valid set of records that fall within the intersected region
- Now implement this without bedtools intersect
- Verify your results with bedtools intersect
- In increments of 10%, can you print a breakdown of variant type counts for each AF interval i.e 0-10%, 10-20% ... 80-100%