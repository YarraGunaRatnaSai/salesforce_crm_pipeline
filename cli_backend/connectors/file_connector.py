import pandas as pd
import os

class FileConnector:
    """
    Handles file-based operations.
    """
    def __init__(self, file_path: str):
        """
        Initialize the file connector.
        :param file_path: Path to the file.
        """
        self.file_path = file_path

    def read_file(self):
        """
        Read data from the file based on its extension.
        """
        _, ext = os.path.splitext(self.file_path)
        try:
            if ext == ".csv":
                return pd.read_csv(self.file_path)
            elif ext == ".xls" or ext == ".xlsx":
                return pd.read_excel(self.file_path)
            elif ext == ".parquet":
                return pd.read_parquet(self.file_path)
            else:
                raise ValueError(f"Unsupported file extension: {ext}")
        except Exception as e:
            raise IOError(f"Failed to read file: {e}")

    def write_file(self, data: pd.DataFrame, format: str = "csv"):
        """
        Write data to the file in the specified format.
        :param data: Data to write.
        :param format: Format to write the file ('csv', 'excel', 'parquet').
        """
        try:
            if format == "csv":
                data.to_csv(self.file_path, index=False)
            elif format in ["xls", "xlsx"]:
                data.to_excel(self.file_path, index=False)
            elif format == "parquet":
                data.to_parquet(self.file_path, index=False)
            else:
                raise ValueError(f"Unsupported format: {format}")
        except Exception as e:
            raise IOError(f"Failed to write file: {e}")
