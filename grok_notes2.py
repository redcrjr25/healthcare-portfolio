import fhirpy

#Example: Fetch patient data (requires FHIR server access)
client = fhirpy.FHIRClient(url="https://your-fhir-server")
patients = client.resources("Patient").fetch()
for patient in patients:
    print(patient['name"][0]["given"]
[0])  #Prints patient names