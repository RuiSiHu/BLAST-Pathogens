import datetime
import os

from tools.LogUtil import my_logger

def BLASTProteinProcess(input_path, parameters, output_path):
    database, outfmt, evalue, max_target_seqs = parameters["protein_database_type"], parameters["protein_outfmt"], parameters[
        "protein_evalue"], parameters["protein_max_target_seqs"]
    database_dict = {
        "Virus": "virus_pep",
        "Bacterium": "bacterium_pep",
        "Rickettsia": "rickettsia_pep",
        "Chlamydia": "chlamydia_pep",
        "Spirochete": "spirochete_pep",
        "Parasite": "parasite_pep",
        "Fungus": "fungus_pep"
    }
    database_path = os.path.join("tools", "BLAST", "BLAST_index", database.lower(), database_dict[database])
    current_time = datetime.datetime.now().strftime('%b%d_%H-%M-%S')
    output_path = os.path.join(output_path, "blast_protein_" + current_time + "_blast.out")  #
    file = open(output_path, 'w+')
    file.close()
    command = r"blastp -query " + input_path + " -out " + output_path + " -db " + database_path\
              + " -outfmt " + outfmt + " -evalue " + evalue + " -num_threads 2 -max_target_seqs " + max_target_seqs
    my_logger.info("The command is: " + command)
    command_return = os.popen(command)
    my_logger.info("BLASTProteinProcess output:")
    my_logger.info(command_return.read())
    return output_path


def BLASTGeneProcess(input_path, parameters, output_path):
    database, outfmt, evalue, max_target_seqs = parameters["gene_database_type"], parameters["gene_outfmt"], parameters[
        "gene_evalue"], parameters["gene_max_target_seqs"]
    database_dict = {
        "Virus": "virus_nuc",
        "Bacterium": "bacterium_nuc",
        "Rickettsia": "rickettsia_nuc",
        "Chlamydia": "chlamydia_nuc",
        "Spirochete": "spirochete_nuc",
        "Parasite": "parasite_nuc",
        "Fungus": "fungus_nuc"
    }
    database_path = os.path.join("tools", "BLAST", "BLAST_index", database.lower(), database_dict[database])
    current_time = datetime.datetime.now().strftime('%b%d_%H-%M-%S')
    output_path = os.path.join(output_path, "blast_gene_" + current_time + "_blast.out")  #
    file = open(output_path, 'w+')
    file.close()
    command = r"blastn -query " + input_path + " -out " + output_path + " -db " + database_path + \
              " -outfmt " + outfmt + " -evalue " + evalue + " -num_threads 2 -max_target_seqs " + max_target_seqs
    my_logger.info("The command is: " + command)
    command_return = os.popen(command)
    my_logger.info("BLASTGeneProcess output:")
    my_logger.info(command_return.read())
    return output_path
