#!/bin/bash
#conda env create -f sandbox_env.yml
source $(conda info --base)/etc/profile.d/conda.sh
conda activate sandbox_env
python -m ipykernel install --user --name sandbox_env
#jupyter kernelspec list
#jupyter kernelspec remove sandbox_env
