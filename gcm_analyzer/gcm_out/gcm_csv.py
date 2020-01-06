from pandas import DataFrame
from pathlib import Path


def out_csv(result: DataFrame, path_to_output_file: Path):
    result.to_csv(str(path_to_output_file),
                  index=False,
                  encoding='utf-8')
