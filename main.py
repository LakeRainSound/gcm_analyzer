from gcm_analyzer.repo_metrics.cloc_analyzer.cloc_analyzer import get_all_cloc_info
from gcm_analyzer.repo_metrics.github_api_analyzer.issue_analyzer import get_all_issues_info
from gcm_analyzer.repo_metrics.github_api_analyzer.label_analyzer import get_all_label_info
from gcm_analyzer.cli import CLI
from gcm_analyzer.gcm_error.gcm_error import RepositoryList
import json
import pandas as pd


def main():
    parser = CLI()
    gcm_result, repository_list, output_file, analyze_num, lang_list, loc_args = parser.parse()

    gcme = RepositoryList(repository_list=repository_list,
                          gcm_result=gcm_result['repository'],
                          number_of_repo=analyze_num)

    no_error_repo_list = gcme.get_no_error_repo_list()

    get_all_issues_info(repository_list=no_error_repo_list,
                        repository_result=gcm_result['repository'])

    get_all_label_info(repository_list=no_error_repo_list,
                       repository_result=gcm_result['repository'])

    get_all_cloc_info(repository_list=no_error_repo_list,
                      repository_result=gcm_result['repository'],
                      lang_list=lang_list,
                      loc_args=loc_args)
    return


if __name__ == '__main__':
    main()
