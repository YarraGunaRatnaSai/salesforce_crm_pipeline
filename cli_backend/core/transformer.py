import pandas as pd

class Transformer:
    """
    Handles transformations on data.
    """
    def transform(self, data: pd.DataFrame, transformation_rules: dict):
        """
        Apply transformation rules on data.
        :param data: Input dataframe.
        :param transformation_rules: Dictionary of transformations to apply.
        """
        for column, func in transformation_rules.items():
            data[column] = data[column].apply(func)
        return data
