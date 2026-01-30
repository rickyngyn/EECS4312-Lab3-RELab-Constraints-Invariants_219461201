from datetime import date

class DispenseEvent:
    """
    Represents a single medication dispensing event for a patient.

    """
    MAX_DAILY_DOSE_MG = {
        "Ibuprofen": 1200,
        "Amoxicillin": 3000,
        "Paracetamol": 4000,
    }

    # TODO Task 3: Encode and enforce input constraints (e.g., valid dose, quantity, identifiers)
    def __init__(self, patient_id, medication, dose_mg, quantity):
        """
        Initialize a new DispenseEvent.

        Args:
            patient_id: Unique identifier for the patient receiving medication.
            medication: Name or identifier of the medication being dispensed.
            dose_mg: Dose per unit in milligrams. Must be a positive number.
            quantity: Number of units dispensed. Must be a positive integer.

        """
        if not isinstance(dose_mg, (int, float)):
            raise ValueError("dose_mg must be a number expressed in milligrams")
        if dose_mg <= 0:
            raise ValueError("dose_mg must be positive")

        if not isinstance(quantity, int):
            raise ValueError("quantity must be an integer")
        if quantity <= 0:
            raise ValueError("quantity must be a positive integer")

        if medication not in self.MAX_DAILY_DOSE_MG:
            raise ValueError("medication is missing a configured maximum daily dose")

        max_allowed = self.MAX_DAILY_DOSE_MG[medication]
        if dose_mg > max_allowed:
            raise ValueError("dose_mg exceeds maximum daily dose for {medication}: {dose_mg} > {max_allowed}")

        self.patient_id = patient_id
        self.medication = medication
        self.dose_mg = dose_mg
        self.quantity = quantity
        self.event_date = date.today()

    # TODO Task 4: Define and check system invariants 
    def invariant_holds(existing_events, new_event):
        """
        Check whether adding a new dispense event preserves all system invariants.

        Args:
            existing_events: Iterable of previously recorded DispenseEvent objects.
            new_event: The proposed DispenseEvent to validate.

        Returns:
            bool: True if all invariants hold after adding new_event; False otherwise.
            
        """
        for e in existing_events:
            if (e.patient_id == new_event.patient_id and e.medication == new_event.medication and e.event_date == new_event.event_date):
                return False
        return True
