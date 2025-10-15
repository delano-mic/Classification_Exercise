from abc import ABC, abstractmethod
from typing import List, Tuple


class ParentStrategy(ABC):

    @abstractmethod
    def calculate_impurity(self, true_prob: float, false_prob: float) -> float:
        pass

    def weighted_sum(self, partitions: Tuple[List['Record'], List['Record']]) -> float:
        true_records, false_records = partitions
        true_count = len(true_records)
        false_count = len(false_records)
        total_count = true_count + false_count
        if total_count == 0:
            raise ValueError("Values must be provided for true and false partitions")

        true_prob = true_count / total_count
        false_prob = false_count / total_count

        w_sum = 0
        for partition in partitions:
            weight = len(partition) / total_count
            w_sum += weight * self.calculate_impurity(true_prob, false_prob)
        
        return w_sum

    def calculate(self, partitions: Tuple[List['Record'], List['Record']]) -> float:
        true_records, false_records = partitions
        true_count = len(true_records)
        false_count = len(false_records)
        total_count = true_count + false_count
        if total_count == 0:
            raise ValueError("Values must be provided for true and false partitions")

        true_prob = true_count / total_count
        false_prob = false_count / total_count

        return self.calculate_impurity(true_prob, false_prob)