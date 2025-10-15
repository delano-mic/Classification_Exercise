import csv
from typing import List, Dict
from record import Record


def ingest_data(file_path: str) -> List['Record']:
    """
    Ingest CSV data and convert to Record objects.
    
    Args:
        file_path: Path to the CSV file
        
    Returns:
        List of Record objects
    """
    records = []
    
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            attrs = {
                'ID': int(row['ID']),
                'Age': int(row['Age']),
                'Systolic Blood Pressure': int(row['Systolic Blood Pressure']),
                'OnHypertensionMedication': row['OnHypertensionMedication'] == 'TRUE',
                'HasDiabetes': row['HasDiabetes'] == 'TRUE',
                'IsSmoker': row['IsSmoker'] == 'TRUE',
                'Total Cholesterol': int(row['Total Cholesterol']),
                'HDL cholesterol': int(row['HDL cholesterol']),
                'IsAfricanAmerican': row['IsAfricanAmerican'] == 'TRUE',
                'Gender': row['Gender']
            }
            
            label = row['Assessment']
            
            records.append(Record(attrs, label))
    
    return records

def find_averages(records: List['Record']) -> Dict[str, float]:
    averages = {
        'Age': 0,
        'Systolic Blood Pressure': 0,
        'Total Cholesterol': 0,
        'HDL cholesterol': 0
    }
    
    for record in records:
        averages['Age'] += record.attrs['Age']
        averages['Systolic Blood Pressure'] += record.attrs['Systolic Blood Pressure']
        averages['Total Cholesterol'] += record.attrs['Total Cholesterol']
        averages['HDL cholesterol'] += record.attrs['HDL cholesterol']
        
    averages['Age'] = averages['Age'] / len(records)
    averages['Systolic Blood Pressure'] = averages['Systolic Blood Pressure'] / len(records)
    averages['Total Cholesterol'] = averages['Total Cholesterol'] / len(records)
    averages['HDL cholesterol'] = averages['HDL cholesterol'] / len(records)
    
    return averages