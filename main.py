import gcm_analyzer.repo_metrics.cloc_analyzer.cloc_analyzer as ca
import gcm_analyzer.repo_metrics.github_api_analyzer.issue_analyzer as ia
import gcm_analyzer.repo_metrics.github_api_analyzer.label_analyzer as la
import json
import pandas as pd


def main():
    with open('test_out.json', 'r') as f:
        result = json.load(f)
    ca.get_all_repo_cloc(lang_list=['Python', 'Markdown'],
                         loc_args=['comment', 'blank', 'code'],
                         repo_list=['LakeRainSound/get_code_metrics',
                                    'LakeRainSound/sample-java-project'],
                         repo_result=result['repository'])
    issue_result = ia.get_all_issues_info(repo_list=['LakeRainSound/get_code_metrics',
                                                     'LakeRainSound/sample-java-project'],
                                          repo_result=result['repository'])

    label_result = la.get_all_label_info(repo_list=['LakeRainSound/get_code_metrics',
                                                    'LakeRainSound/sample-java-project'],
                                         repo_result=result['repository'])
    issue_result = pd.DataFrame(issue_result)
    label_result = pd.DataFrame(label_result)
    print(pd.merge(issue_result, label_result, on='nameWithOwner'))
    return


if __name__ == '__main__':
    main()
