from dsa103.chemistry_tools import calculate_molecular_formula, calculate_molecular_weight


def test_calculate_molecular_formula():
    """Tests for calculate_molecular_formula."""

    formula_water = calculate_molecular_formula("O")
    assert formula_water == "H2O"

    formula_caffeine = calculate_molecular_formula("CN1C=NC2=C1C(=O)N(C(=O)N2C)C")
    assert formula_caffeine == "C8H10N4O2"

def test_calculate_molecular_weight():
    """Tests for calculate_molecular_weight."""

    weight_water = calculate_molecular_weight("O")
    # Molecular weight of H2O is about 18.0106
    assert round(weight_water, 4) == 18.0106

    weight_caffeine = calculate_molecular_weight("CN1C=NC2=C1C(=O)N(C(=O)N2C)C")
    # Molecular weight of C8H10N4O2 is about 194.0804
    assert round(weight_caffeine, 4) == 194.0804
