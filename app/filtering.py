from Bio.SeqUtils.ProtParam import ProteinAnalysis

def antigenicity_score(peptide):
    analysis = ProteinAnalysis(peptide)
    return -analysis.gravy()

def is_non_allergenic(peptide):
    return "C" not in peptide

def is_non_toxic(peptide):
    toxic_motifs = ["KKK", "RRR"]
    return not any(m in peptide for m in toxic_motifs)

def filter_epitopes(peptides, threshold=0.5):
    selected = []

    for pep in peptides:
        if antigenicity_score(pep) > threshold \
        and is_non_allergenic(pep) \
        and is_non_toxic(pep):
            selected.append(pep)

    return selected
