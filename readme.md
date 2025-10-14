### 1. Reflect on how the coding went.  What was easy and what was hard? Did this assignment serve its purpose? Why or why not?

The hardest part was understanding the formulas for gini purity and shannon entropy. The latex representation of the formulas were harder to understand than the actual implmentation in Python, which became clearer after some googling made me recall the simpler version that you'd shared in class.

The second hardest part was following the specific implementation instructions, specifically making sure that I had the right functions in the right files. 

### 2. What partition should we split on first according to our 2 calculations?
isSmoker

### 3. Please include all citations to other references you used and any AI prompts you used.
This is tricky to do retroactively. I used google extensively, particularly for the gini purity and shannon entropy functions. Other noteable places where I relied on google:

1. Finding out how to read a CSV file
2. How to add generic typing (`List['Record']`)
3. How to type a lambda function (`Callable[['Record'], bool]`)
4. What the max value across gini impurity and shannon entropy should be (`best_impurity = 1`)
5. Iterating a dictionary, which I've looked up so many times in this course (`for pivot_name, pivot_func in PIVOTS.items()`)
6. How to create an abtract method using ABC ```
    @abstractmethod
    def calculate_impurity(self, true_prob: float, false_prob: float) -> float:
        pass```


7. How to convert trithy/falsey to true/false (`record.attrs["IsSmoker"] == "TRUE"`)