from Bio import SeqIO
import pandas as pd

class Bio:
    @staticmethod
    def df_to_fasta(df: pd.DataFrame, url: str, column_name: str = "Sequence"):
        def write_fasta_row(row, f):
            f.write(f'>{row.name}\n{row[column_name]}\n')

        with open(f'{url}.fasta', 'w') as f:
            df.apply(lambda x: write_fasta_row(x, f), axis=1)

    @staticmethod
    def load_fasta(url: str, index_num: int = 1):
        sequences = {}
        for sequence in SeqIO.parse(url, "fasta"):
            seq_id = sequence.id.split("|")[index_num]
            sequences[seq_id] = [str(sequence.seq)]
        sequences = pd.DataFrame.from_dict(sequences, orient="index")
        sequences.columns = ["Sequence"]
        return sequences