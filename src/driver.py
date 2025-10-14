import sys
from pathlib import Path

# Add parent directory to path to import from config
sys.path.append(str(Path(__file__).parent.parent))

from collective_impurity_gini import CollectiveImpurityGini
from collective_impurity_entropy import CollectiveImpurityEntropy
from config.config import config
from utils.ingest import ingest_data, find_averages
from utils.partition_utils import find_best_partition

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
            
        best_partition = find_best_partition(records, strategy)
        print(f"Best partition: {best_partition}")

if __name__ == "__main__":
    main()

