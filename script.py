#code for running the python script on the High Performance Cluster, Artemis at the University of Sydney



#!/bin/bash
#PBS -P DRDLM
#PBS -l select=1:ncpus=4:mem=64gb:ngpus=1
#PBS -l walltime=100:00:00

module load python/3.7.2
source tf/bin/activate
module load cuda/10.0.130
module load openmpi-gcc/3.1.3

cd $PBS_O_WORKDIR
python Model_adam2.py
