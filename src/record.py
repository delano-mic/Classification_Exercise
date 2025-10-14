class Record:
    def __init__(self, input_values, actual_label):
        self.attrs = input_values
        self.actual_label = actual_label
        self.predicted_label = None