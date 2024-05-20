def extract_duplicate_genes(fasta_file):
    duplicates = []
    with open(fasta_file, 'r') as file:
        gene_info = {}
        for line in file:
            if line.startswith('>'):  # Start of a new gene
                gene_name = line[1:].split()[0]
                gene_info = {'name': gene_name, 'sequence': '', 'duplication': False}
            elif 'duplication' in line:
                gene_info['duplication'] = True
                gene_info['sequence'] = ''.join(duplicates)
                duplicates = []
            else:
                duplicates.append(line.strip())
        # Add last gene if file doesn't end with a newline
        if gene_info['duplication']:
            gene_info['sequence'] = ''.join(duplicates)
            duplicates = []
            duplicates.append(gene_info)

    return duplicates

# Assuming 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa' is the FASTA file
duplicates = extract_duplicate_genes('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
# Process and output the duplicates to a new FASTA file
with open('duplicate_genes.fa', 'w') as outfile:
    for gene in duplicates:
        outfile.write(f">{gene['name']}\n{gene['sequence']}\n")
    