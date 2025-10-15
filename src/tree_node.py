from typing import Callable, List, Tuple, Dict
from config.pivots import PIVOTS
from parent_strategy import ParentStrategy
from record import Record

class TreeNode:
    def __init__(self, records: List['Record'], pivots: Dict[str, Callable[['Record'], bool]]):
        self.records = records
        self.pivots = pivots

        self.children = []
        self.partition_logic = None
        self.label_to_apply = None

        self.low_risk_count, self.high_risk_count = self.count_labels()

        pass

    def count_labels(self):
        lc0 = 0
        lc1 = 0
        for record in self.records:
            if record.actual_label == "Low Risk":
                lc0 += 1
            elif record.actual_label == "High Risk":
                lc1 += 1

        return lc0, lc1

    def make_partition(
        self,
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

    def find_best_partition(self, records: List['Record'], strategy: ParentStrategy):
        best_partition_category = None
        best_partition = None
        best_impurity = 1 # Accounts for entropy since gini can only reach 0.5... i think
        for pivot_name, pivot_func in PIVOTS.items():
            
            partition = self.make_partition(records, pivot_func)
            # impurity = strategy.calculate(partition)
            impurity = strategy.weighted_sum(partition)
            if impurity < best_impurity:
                best_impurity = impurity
                best_partition_category = pivot_name
                best_partition = partition

        return best_partition_category, best_partition

    def find_best_split(self):
        pass

    def grow_tree(self, strategy: ParentStrategy, i = 0):
        tabs = "\t" * i
        print(f"{tabs}Growing Tree Node: Low Risk Count: {self.low_risk_count}, High Risk Count: {self.high_risk_count}")
        if self.low_risk_count == 0 or self.high_risk_count == 0:
            print(f"{tabs}Node is pure")
            if self.low_risk_count > self.high_risk_count:
                self.label_to_apply = "Low Risk"
            else:
                self.label_to_apply = "High Risk"
        
        elif len(self.pivots) == 0:
            print(f"{tabs}No split functions remaining")
            if self.low_risk_count > self.high_risk_count:
                self.label_to_apply = "Low Risk"
            else:
                self.label_to_apply = "High Risk"
        else:
            best_partition_category, best_partition = self.find_best_partition(self.records, strategy)
            print(f"{tabs}Splitting further by {best_partition_category}")
            self.partition_logic = PIVOTS[best_partition_category]
            del(self.pivots[best_partition_category])
            self.children.append(TreeNode(best_partition[0], self.pivots))
            self.children.append(TreeNode(best_partition[1], self.pivots))
            
            for child in self.children:
                child.grow_tree(strategy, i + 1)

        # Base Case 1
        # do all records hafve the same label?]
        # # if so set tree nodw.label_to_apply to be whatever the label is
        # Base Case 2
        # do we still have lambdas in our pivits attr?
        # If not, set treenode.label_to_apply to be the most common label
        # recuirsive step
        # 1. find best new lambda to splkit on and do the split
        # 2. remove that lambda from our childrens list of future options
        # 3. make 2 children tree nod objects
        # 4. call our method for each child

        pass

    def classify_record_single(self, record: 'Record'):
        if len(self.children) == 0:
            record.predicted_label = self.label_to_apply
        else:
            if self.partition_logic(record) == True:
                self.children[0].classify_record_single(record)
            else:
                self.children[1].classify_record_single(record)

    def classify_records(self, records: List['Record']):
        for record in records:
            self.classify_record_single(record)
        
        return records
            
        