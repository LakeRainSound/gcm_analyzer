from pathlib import Path

from pandas import DataFrame


# 値の四分位数を取得
def out_quartile(result: DataFrame):
    print(result.quantile([0, 0.25, 0.5, 0.75, 1.0]))


# csvに出力
def out_csv(result: DataFrame, path_to_output_file: Path):
    result.to_csv(str(path_to_output_file),
                  index=False,
                  encoding='utf-8')


def out_issues_enabled(result: DataFrame):
    has_issue_unenabled_list = result[result['hasIssuesEnabled'] != True]
    print('\nIssue Page Disenabled Repository per All ')
    print('{}% ({}/{})'.format(len(has_issue_unenabled_list)/len(result)*100,
                               len(has_issue_unenabled_list),
                               len(result)))


def _get_dataframe_merged_dict(result_list):
    merged_dict = {}

    for result in result_list:
        merged_dict.update(result)

    return DataFrame(merged_dict)


def gcm_out_call(result_list, path_to_output_file: Path):
    result = _get_dataframe_merged_dict(result_list)
    # 全てのリポジトリ
    print('\n**** ALL Repositories ****\n')
    # csvに出力
    out_csv(result, path_to_output_file)
    # 四分位数を取得
    out_quartile(result)

    # issueページが利用可能かどうかを示す．
    out_issues_enabled(result)

    print('\n**** Repositories which have Issue Page ****\n')
    # 四分位数を取得(Issue Pageが利用可能な場合)
    out_quartile(result[result['hasIssuesEnabled']])
