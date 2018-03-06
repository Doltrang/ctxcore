# -*- coding: utf-8 -*-

import pytest
from pyscenic.rnkdb import FeatherRankingDatabase as RankingDatabase
from pyscenic.genesig import GeneSignature


NOMENCLATURE = "HGNC"
TEST_DATABASE_FNAME = "../resources/hg19-tss-centered-10kb-10species.mc9nr.feather"
TEST_DATABASE_NAME = "hg19-tss-centered-10kb-10species"
TEST_SIGNATURE_FNAME = "../resources/c6.all.v6.1.symbols.gmt.txt"


@pytest.fixture
def db():
    return RankingDatabase(TEST_DATABASE_FNAME, TEST_DATABASE_NAME, NOMENCLATURE)

@pytest.fixture
def gs():
    return GeneSignature.from_gmt(TEST_SIGNATURE_FNAME, NOMENCLATURE,
                                    gene_separator="\t", field_separator="\t", )[0]

def test_init(db):
    assert db.name == TEST_DATABASE_NAME
    assert db.nomenclature == NOMENCLATURE

def test_total_genes(db):
    assert db.total_genes == 22284

def test_load_full(db):
    rankings = db.load_full()
    assert len(rankings.index) == 5
    assert len(rankings.columns) == 22284

def test_load(db, gs):
    rankings = db.load(gs)
    assert len(rankings.index) == 5
    assert len(rankings.columns) == 29
