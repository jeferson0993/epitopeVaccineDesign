from Bio.SeqUtils.ProtParam import ProteinAnalysis

def sliding_window(sequence, length):
    return [sequence[i:i+length] for i in range(len(sequence)-length+1)]

def predict_ctl(sequence, length):
    return sliding_window(sequence, length)

def predict_htl(sequence, length):
    return sliding_window(sequence, length)

def predict_bcell(sequence, length):
    candidates = sliding_window(sequence, length)
    filtered = []

    for pep in candidates:
        analysis = ProteinAnalysis(pep)
        if analysis.gravy() < 0:  # hidrofílico
            filtered.append(pep)

    return filtered
