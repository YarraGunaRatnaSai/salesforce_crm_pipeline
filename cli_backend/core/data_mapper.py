import pandas as pd

class DataMapper:
    """
    Handles mapping of data columns between source and destination.
    """
    def apply_mapping(self, data: pd.DataFrame, mapping: dict, na_action="drop", custom_na_value=None):
        """
        Apply column mappings and handle missing values.
        :param data: Input dataframe.
        :param mapping: Dictionary of source to destination column mappings.
        :param na_action: Action for missing values ('drop', 'mean', 'most_frequent', or 'custom').
        :param custom_na_value: Custom value to fill NA if na_action='custom'.
        """
        data = data.rename(columns=mapping)
        if na_action == "drop":
            return data.dropna()
        elif na_action == "mean":
            return data.fillna(data.mean())
        elif na_action == "most_frequent":
            return data.fillna(data.mode().iloc[0])
        elif na_action == "custom" and custom_na_value is not None:
            return data.fillna(custom_na_value)
        else:
            return data
