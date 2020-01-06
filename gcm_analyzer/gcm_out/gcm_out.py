from pathlib import Path
from gcm_analyzer.gcm_out.gcm_csv import out_csv
from gcm_analyzer.gcm_out.gcm_quartile import out_quartile

from pandas import DataFrame


def _get_dataframe_merged_dict(result_list):
    merged_dict = {}

    for result in result_list:
        merged_dict.update(result)

    return DataFrame(merged_dict)


def gcm_out_call(result_list, path_to_output_file: Path):
    result = _get_dataframe_merged_dict(result_list)

    # csvに出力
    out_csv(result, path_to_output_file)
    # 四分位数を取得
    out_quartile(result)

