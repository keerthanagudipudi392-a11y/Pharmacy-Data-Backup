#---pharmacy Pediatric Dosage Calculator ---


def calculate_paracetamol_dose(weight_kg):
    # Standard pediatric dose: 15mg of paracetamol per 1kg of body weight
    dose_mg=weight_kg * 15
    return dose_mg

# Day 2: Dynamic User Input and Decisions!
child_weight = float(input("Enter the child's weight in kg:"))
final_dose = calculate_paracetamol_dose(child_weight)

print("---Pharmacy Dosage Check ---")

if child_weight > 50:
    print("⚠️ WARNING: Weight is too high for pediatric doses.Check adult guidelines!")
else:
    print(f"For a child weighing {child_weight}kg:")
    print(f"The correct Paracetamol dose is: {final_dose}mg")   