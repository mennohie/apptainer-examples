import pickle
import os
from tqdm import tqdm
import numpy as np
import pandas as pd
import dotenv
from transformers import AutoTokenizer, AutoModelForMaskedLM, pipeline
import torch
from util.bio import Bio

dotenv.load_dotenv()
class Embedder:
    def __init__(self, model_name, device):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForMaskedLM.from_pretrained(model_name)
        self.pipe = pipeline('feature-extraction', model=self.model, tokenizer=self.tokenizer,
                             device=device, aggregation_strategy='average')
     
    def extract_embeddings(self, df: pd.DataFrame, dtype=np.float16, batch_size=8):
        def batch(iterable, n=1):
            l = len(iterable)
            for ndx in range(0, l, n):
                yield iterable[ndx:min(ndx + n, l)]

        embeddings = []
        for b in tqdm(batch(df.index, batch_size)):
            for out in self.pipe(list(df.loc[b, "Sequence"])):
                embeddings.append(np.array(out, dtype=dtype).mean(axis=1))
        return np.vstack(embeddings), df.index


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        prog="Embed input dataset",
        description="Returns an embedding and an index vector for \
                    any input dataframe containing protein sequences"
    )
    parser.add_argument('-i', '--input', required=True)
    parser.add_argument('-m', '--model', required=True)
    parser.add_argument('-f', '--filename', required=True)
    parser.add_argument('-b', '--batch_size', type=int, required=False)
    args = parser.parse_args()
    model_name = args.model
    fasta_input = args.input
    if "index_loc" in os.environ:
        index_num = int(os.environ["index_loc"])
    else:
        index_num = 1
        
    sequences = Bio.load_fasta(fasta_input, index_num=index_num)
    embedder = Embedder(model_name, device=torch.device("cuda:0"))
    if args.batch_size is None:
        embeddings, indices = embedder.extract_embeddings(sequences, np.float32, batch_size=len(sequences.index))
    else:
        embeddings, indices = embedder.extract_embeddings(sequences, np.float32,
                                                          batch_size=int(args.batch_size))
    with open(f"/mnt/{args.filename}.pkl", "wb") as f:
        pickle.dump((embeddings, indices), f)