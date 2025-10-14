from typing import Callable, List, Tuple
from config.pivots import PIVOTS
from parent_strategy import ParentStrategy

def make_partition(
    records: List['Record'], 
    func: Callable[['Record'], bool] # bool here is the return type and NOT a lambda param
) -> Tuple[List['Record'], List['Record']]:
    true_list: List['Record'] = []
    false_list: List['Record'] = []
    for record in records:
        if func(record):
            true_list.append(record)
        else:
            false_list.append(record)
    return (true_list, false_list)

def find_best_partition(records: List['Record'], strategy: ParentStrategy):
    best_partition_category = None
    best_impurity = 1 # Accounts for entropy since gini can only reach 0.5... i think
    for pivot_name, pivot_func in PIVOTS.items():
        
        partition = make_partition(records, pivot_func)
        impurity = strategy.calculate(partition)
        if impurity < best_impurity:
            best_impurity = impurity
            best_partition_category = pivot_name

    return best_partition_category