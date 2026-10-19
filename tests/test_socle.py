import importlib

import pytest

import agent_droits


def test_version():
    assert agent_droits.__version__ == "0.1.0"


@pytest.mark.parametrize("module", ["outils", "agent", "api", "garde_fous"])
def test_sous_paquets_importables(module):
    importlib.import_module(f"agent_droits.{module}")
