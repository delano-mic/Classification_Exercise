PIVOTS = {
    "IsSmoker": lambda record: record.attrs["IsSmoker"] == "TRUE",
    "OnHypertensionMedication": lambda record: record.attrs["OnHypertensionMedication"] == "TRUE",
    "HasDiabetes": lambda record: record.attrs["HasDiabetes"] == "TRUE",
    "IsAfricanAmerican": lambda record: record.attrs["IsAfricanAmerican"] == "TRUE",
    "Age": lambda record: record.attrs["Age"] < 65.1,
    "Systolic Blood Pressure": lambda record: record.attrs["Systolic Blood Pressure"] < 155.8,
    "Total Cholesterol": lambda record: record.attrs["Total Cholesterol"] < 177.3,
    "HDL cholesterol": lambda record: record.attrs["HDL cholesterol"] > 58.4
}