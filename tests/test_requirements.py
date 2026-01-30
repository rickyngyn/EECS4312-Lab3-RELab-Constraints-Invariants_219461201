# Contains requirement-driven tests for the dispensing subsystem.
# TODO: create at least 3 test cases

import pytest
from src.dispense import DispenseEvent

def test_negative_or_zero_dose_rejected():
    with pytest.raises(ValueError):
        DispenseEvent("P1", "Ibuprofen", 0, 10)

    with pytest.raises(ValueError):
        DispenseEvent("P1", "Ibuprofen", -5, 10)

def test_quantity_must_be_positive_integer():
    with pytest.raises(ValueError):
        DispenseEvent("P1", "Ibuprofen", 200, 0)

    with pytest.raises(ValueError):
        DispenseEvent("P1", "Ibuprofen", 200, -1)

    with pytest.raises(ValueError):
        DispenseEvent("P1", "Ibuprofen", 200, 2.5)

def test_exceeding_max_daily_dose_rejected():
    with pytest.raises(ValueError):
        DispenseEvent("P1", "Ibuprofen", 2000, 10)

def test_duplicate_dispensing_same_day_fails_invariant():
    e1 = DispenseEvent("P1", "Amoxicillin", 500, 10)
    e2 = DispenseEvent("P1", "Amoxicillin", 500, 10)

    assert DispenseEvent.invariant_holds([], e1) is True
    assert DispenseEvent.invariant_holds([e1], e2) is False