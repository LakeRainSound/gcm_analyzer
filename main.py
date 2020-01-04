import gcm_analyzer.repo_metrics.cloc_analyzer.cloc_analyzer as ca
import gcm_analyzer.repo_metrics.github_api_analyzer.issue_analyzer as ia
import gcm_analyzer.repo_metrics.github_api_analyzer.label_analyzer as la
from gcm_analyzer.gcm_error.gcm_error import RepositoryList
import json
import pandas as pd


def main():
    with open('test_out.json', 'r') as f:
        gcm_result = json.load(f)

    gcme = RepositoryList(repository_list=['LakeRainSound/get_code_metrics',
                                           'LakeRainSound/sample-java-project',
                                           'LakeRainSound/sample-java-project',
                                           'LakeRainSound/empty',
                                           'lslakaflkjc/vhjksfhkavvn',
                                           'sssffaf/sjkhfkjjf'],
                          gcm_result=gcm_result['repository'],
                          number_of_repo=4)
    no_error_repo_list = gcme.get_no_error_repo_list()
    print(no_error_repo_list)
    return


if __name__ == '__main__':
    main()
