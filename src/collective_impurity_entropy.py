import math
from typing import List, Tuple
from parent_strategy import ParentStrategy
from record import Record

class CollectiveImpurityEntropy(ParentStrategy):

    def calculate_impurity(self, true_prob: float, false_prob: float) -> float:
        """
        Calculate the entropy of a two lists of Records.
        
        Uses the formula: H(data) = -(P(true)⋅log2(P(true)) + P(false)⋅log2(P(false)))
        
        Args:
            true_prob: Probability of the true partition
            false_prob: Probability of the false partition
        
        Returns:
            float: The entropy value for combined lists
            
        Raises:
            ValueError: If both lists are empty
        """
        return - (true_prob * math.log2(true_prob) + false_prob * math.log2(false_prob))