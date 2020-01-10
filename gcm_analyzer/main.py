from gcm_analyzer.repo_metrics.cloc_analyzer.cloc_analyzer import get_all_cloc_info
from gcm_analyzer.repo_metrics.github_api_analyzer.issue_analyzer import get_all_issues_info
from gcm_analyzer.repo_metrics.github_api_analyzer.label_analyzer import get_all_label_info
from gcm_analyzer.cli import CLI
from gcm_analyzer.gcm_no_error_repo.gcm_no_error_repo import RepositoryList
from gcm_analyzer.gcm_out.gcm_out import gcm_out_call


def main():
    result_list = []

    parser = CLI()
    gcm_result, repository_list, path_to_output_file, analyze_num, lang_list, loc_args = parser.parse()

    gcme = RepositoryList(repository_list=repository_list,
                          gcm_result=gcm_result['repository'],
                          number_of_repo=analyze_num)

    no_error_repo_list = gcme.get_no_error_repo_list()
    # issueの結果を取得
    issue_info = get_all_issues_info(repository_list=no_error_repo_list,
                                     repository_result=gcm_result['repository'])
    result_list.append(issue_info)
    # labelの結果を取得
    label_info = get_all_label_info(repository_list=no_error_repo_list,
                                    repository_result=gcm_result['repository'])
    result_list.append(label_info)
    # clocの結果を取得
    cloc_info = get_all_cloc_info(repository_list=no_error_repo_list,
                                  repository_result=gcm_result['repository'],
                                  lang_list=lang_list,
                                  loc_args=loc_args)
    result_list.append(cloc_info)

    gcm_out_call(result_list, path_to_output_file)
    return


if __name__ == '__main__':
    main()
