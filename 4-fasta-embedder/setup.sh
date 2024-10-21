#!/bin/bash
/opt/miniconda3/bin/conda create -n embedder python=3.12.7
/opt/miniconda3/bin/conda run -n embedder python -m pip install -r /app/requirements.txt
/opt/miniconda3/bin/conda install -n embedder -y pytorch==2.4.0 cudatoolkit=11.8 -c pytorch -c nvidia
/opt/miniconda/bin/conda run -n embedder python -m pip install --upgrade setuptools

