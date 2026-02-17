import os
import logging
from Bio import SeqIO
from config import *
from epitope_prediction import predict_ctl, predict_htl, predict_bcell
from filtering import filter_epitopes
from vaccine_builder import build_vaccine
from utils import setup_logging

def main():

    os.makedirs("results", exist_ok=True)
    os.makedirs("logs", exist_ok=True)

    setup_logging()
    logging.info("Starting Phase 3 pipeline")

    all_ctl = []
    all_htl = []
    all_bcl = []

    for record in SeqIO.parse(INPUT_FASTA, "fasta"):
        seq = str(record.seq)

        ctl = predict_ctl(seq, CTL_LENGTH)
        htl = predict_htl(seq, HTL_LENGTH)
        bcl = predict_bcell(seq, BCL_LENGTH)

        all_ctl.extend(filter_epitopes(ctl))
        all_htl.extend(filter_epitopes(htl))
        all_bcl.extend(filter_epitopes(bcl))

    selected_ctl = all_ctl[:MAX_SELECTED]
    selected_htl = all_htl[:MAX_SELECTED]
    selected_bcl = all_bcl[:MAX_SELECTED]

    final_construct = build_vaccine(
        ADJUVANT,
        selected_ctl,
        selected_htl,
        selected_bcl,
        CTL_LINKER,
        HTL_LINKER,
        BCL_LINKER,
        BLOCK_LINKER
    )

    with open(OUTPUT_FASTA, "w") as f:
        f.write(">Multi_epitope_construct\n")
        f.write(final_construct)

    logging.info("Vaccine construct generated successfully.")
    print("Pipeline completed successfully.")

if __name__ == "__main__":
    main()
