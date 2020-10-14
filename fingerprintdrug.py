import xml.etree.ElementTree as ET

################################################################################
def generate_plif_lists(report_file, residue_list, lig_ident):

    #uses report.xml from PLIP to return list of interacting residues and update list of residues in binding site

        plif_list_all = []

        tree = ET.parse(report_file)

        root = tree.getroot()

        #list of residue keys that form an interaction

        for binding_site in root.findall('bindingsite'):

                nest = binding_site.find('identifiers')

                lig_code = nest.find('hetid')

                if str(lig_code.text) == str(lig_ident):

                        #get the plifs stuff here

                        nest_residue = binding_site.find('bs_residues')

                        residue_list_tree = nest_residue.findall('bs_residue')

                        for residue in residue_list_tree:

                                res_id = residue.text

                                dict_res_temp = residue.attrib

                                if res_id not in residue_list:

                                        residue_list.append(res_id)

                                if dict_res_temp['contact'] == 'True':

                                        if res_id not in plif_list_all:

                                                plif_list_all.append(res_id)

        return plif_list_all, residue_list

###############################################################################
plif_list_m006, residue_list = generate_plif_lists('m006/report.xml',residue_list, 'LIG')

plif_list_m009, residue_list = generate_plif_lists('m009/report.xml', residue_list, 'LIG')

plif_list_m004, residue_list = generate_plif_lists('m004/report.xml', residue_list, 'LIG')


from rdkit import Chem,  DataStructs

from rdkit.DataStructs import cDataStructs

################################################################################
def generate_rdkit_plif(residue_list, plif_list_all):

    #generates RDKit plif given list of residues in binding site and list of interacting residues

    plif_rdkit = DataStructs.ExplicitBitVect(len(residue_list), False)

    for index, res in enumerate(residue_list):

        if res in plif_list_all:

            print 'here'

            plif_rdkit.SetBit(index)

        else:

            continue

    return plif_rdkit

#########################################################################
plif_m006 = generate_rdkit_plif(residue_list, plif_list_m006)

plif_m009 = generate_rdkit_plif(residue_list, plif_list_m009)

plif_m004 = generate_rdkit_plif(residue_list, plif_list_m004)


def similarity_plifs(plif_1, plif_2):

    sim = DataStructs.TanimotoSimilarity(plif_1, plif_2)

    print sim

    return sim

###################################################################
print similarity_plifs(plif_m006, plif_m009)

print similarity_plifs(plif_m006, plif_m004)

print similarity_plifs(plif_m009, plif_m004)
