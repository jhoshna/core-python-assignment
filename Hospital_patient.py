def find_patients(data, disease):
    return [p["Name"] for p in data if p["Disease"].lower() == disease.lower()]


patients = [
    {"Name": "Alice", "Age": 30, "Disease": "Flu"},
    {"Name": "Bob", "Age": 45, "Disease": "Diabetes"},
    {"Name": "Charlie", "Age": 35, "Disease": "Flu"}
]

disease = "Flu"

result = find_patients(patients, disease)

print(f"Patients with {disease}:{result}")