import json
import argparse
import dotenv
import os
import numpy as np

dotenv.load_dotenv()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Rolls",
        description="Returns an embedding and an index vector for \
                    any input dataframe containing protein sequences"
    )
    parser.add_argument('-N', '--number', required=True, type=int)
    parser.add_argument('-u', '--url', required=True)
    args = parser.parse_args()
    N = args.number
    url = args.url
    if "seed" in os.environ:
        if not os.environ["seed"]:
            seed = None
        else:
            seed = int(os.environ["seed"])
    else:
        seed = None
    np.random.seed(seed)
    values = np.random.randint(1, 6, N)
    names = os.environ["names"].split(", ")
    rolls = {}
    for i, v in enumerate(values):
        name = names[i % len(names)]
        if name in rolls:
            rolls[name] += int(v)
        else:
            rolls[name] = int(v)
            
    with open(url, "w", encoding='utf-8') as f:
        json.dump(rolls, f)
        
        