from parent_strategy import ParentStrategy


class CollectiveImpurityGini(ParentStrategy):
    
    def calculate_impurity(self, true_prob: float, false_prob: float) -> float:
        """
        Calculate the gini purity of a two lists of Records.
        
        Uses the formula: G=1−(P(true)^2+P(false)^2)
        
        Args:
            true_prob: Probability of the true partition
            false_prob: Probability of the false partition
        
        Returns:
            float: The Gini impurity value
        """
        return 1 - (true_prob**2 + false_prob**2) # "**" is the exponent operator in python