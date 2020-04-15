# -*- coding: utf-8 -*-
# pylint:disable=relative-beyond-top-level
"""
Status: Dev
Run the featurization on the CSD MOF subset
"""
from __future__ import absolute_import
from __future__ import print_function
import os
import pickle
import concurrent.futures
from glob import glob
from pathlib import Path
from tqdm import tqdm
from mine_mof_oxstate.featurize import GetFeatures


OUTDIR = "/scratch/kjablonk/oximachine_all"
INDIR = "/work/lsmo/jablonka/2020-4-7_all_csd_for_oximachine/cif_for_feat"
ALREADY_FEAUTRIZED = [Path(p).stem for p in glob(os.path.join(OUTDIR, "*.pkl"))]


def load_pickle(f):  # pylint:disable=invalid-name
    with open(f, "rb") as fh:  # pylint:disable=invalid-name
        result = pickle.load(fh)
    return result


def featurize_single(structure, outdir=OUTDIR):
    if Path(structure).stem not in ALREADY_FEAUTRIZED:
        try:
            gf = GetFeatures.from_file(structure, outdir)  # pylint:disable=invalid-name
            gf.run_featurization()
        except Exception: 
            pass


def main():
    all_structures = glob(os.path.join(INDIR, "*.cif"))
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for _ in tqdm(
            executor.map(featurize_single, all_structures), total=len(all_structures)
        ):
            pass


if __name__ == "__main__":
    print(("working in {}".format(INDIR)))
    main()  # pylint: disable=no-value-for-parameter
