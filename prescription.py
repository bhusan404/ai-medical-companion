import json

# Load the medicine dataset
with open('medicine_dataset.json', 'r') as file:
    medicine_data = json.load(file)

# Function to generate a prescription for high fever
def generate_prescription_for_fever(medicine_data):
    prescription = []
    high_fever_medicines = []

    # Search for medicines suitable for high fever
    for medicine in medicine_data:
        if "Fever reduction" in medicine["indications"]:
            high_fever_medicines.append(medicine)

    # Sort medicines by dosage strength (assuming higher strength is for severe cases)
    high_fever_medicines.sort(key=lambda x: x["dosage_forms"][0]["strength"])

    # Generate prescription
    if high_fever_medicines:
        prescription.append("Prescription for High Fever:")
        for i, medicine in enumerate(high_fever_medicines):
            prescription.append(f"{i + 1}. {medicine['name']} - {medicine['dosage_forms'][0]['strength']}")
            prescription.append(f"   Instructions: {medicine['dosage_forms'][0]['usage_instructions']}")
        return "\n".join(prescription)
    else:
        return "No suitable medicines found for high fever."

# Generate and print the prescription
fever_prescription = generate_prescription_for_fever(medicine_data)
print(fever_prescription)
