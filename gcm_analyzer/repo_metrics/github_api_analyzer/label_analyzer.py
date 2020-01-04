import pandas
import json


def _create_result_list():
    result_list = {
                    "nameWithOwner": [],
                    "LabelPerClosedIssue": [],
                }
    return result_list


def _get_label_per_issue(repository):
    issue_count = repository['closedIssueCount']
    label_count = repository['hasLabelClosedIssue']

    if issue_count > 0:
        return {"LabelPerClosedIssue": label_count/issue_count}
    else:
        return {"LabelPerClosedIssue": 0}


def _add_result_list(result_list: dict, result: dict):
    for key in result_list.keys():
        result_list[key].append(result[key])

    return result_list


def get_all_label_info(repository_result, repository_list):
    result_list = _create_result_list()

    for repo_name in repository_list:
        result = _get_label_per_issue(repository_result[repo_name])
        result['nameWithOwner'] = repo_name
        result_list = _add_result_list(result_list, result)

    print(json.dumps(result_list, indent=4))

    return result_list
