import sys
from pathlib import Path

# Add parent directory to path to import from config
sys.path.append(str(Path(__file__).parent.parent))

from config.pivots import PIVOTS
from collective_impurity_gini import CollectiveImpurityGini
from collective_impurity_entropy import CollectiveImpurityEntropy
from config.config import config
from utils.ingest import ingest_data, find_averages
# from utils.partition_utils import find_best_partition
from tree_node import TreeNode

def main():
    training_data_path = config['data']['test_data']
    records = ingest_data(training_data_path)

    if(config['data']['FIND_AVERAGES']):
        averages = find_averages(records)
        print(f"Averages: {averages}")

    if(config['data']['FIND_BEST_SPLIT']):
        strategy = None
        if(config['data']['CALCULATION_TO_USE'] == 'gini'):
            strategy = CollectiveImpurityGini()
        elif(config['data']['CALCULATION_TO_USE'] == 'entropy'):
            strategy = CollectiveImpurityEntropy()
        else:
            raise ValueError("Invalid calculation type")

        tree = TreeNode(records, PIVOTS)
        tree.grow_tree(strategy)

    test_data_path = config['data']['test_data_2']
    test_records = ingest_data(test_data_path)
    records = tree.classify_records(test_records)

    correct_classifications = 0
    confusion_matrix = {
        "incorrect": {
            "Low Risk": 0,
            "High Risk": 0
        },
        "correct": {
            "Low Risk": 0,
            "High Risk": 0
        }
    }
    for record in records:
        if record.predicted_label == record.actual_label:
            confusion_matrix['correct'][record.actual_label] += 1
            correct_classifications = correct_classifications + 1
            print("CORRECT CLASSIFICATION", record.attrs['ID'], "=", record.predicted_label)
        else:
            confusion_matrix['incorrect'][record.actual_label] += 1
            print("WRONG CLASSIFICATION", record.attrs['ID'], "=", record.predicted_label)

    print("Correct Classifications:", correct_classifications)
    print("Total Classifications:", len(records))
    print("Accuracy:", correct_classifications / len(records))

    print("Confusion Matrix:", confusion_matrix)

if __name__ == "__main__":
    main()

