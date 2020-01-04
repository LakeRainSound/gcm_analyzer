import pandas
import json


def create_result_list():
    result_list = {
                    "nameWithOwner": [],
                    "LabelPerClosedIssue": [],
                }
    return result_list


def get_label_per_issue(repository):
    issue_count = repository['closedIssueCount']
    label_count = repository['hasLabelClosedIssue']

    if issue_count > 0:
        return {"LabelPerClosedIssue": label_count/issue_count}
    else:
        return {"LabelPerClosedIssue": 0}


def add_result_list(result_list: dict, result: dict):
    for key in result_list.keys():
        result_list[key].append(result[key])

    return result_list


def get_all_label_info(repo_result, repo_list):
    result_list = create_result_list()

    for repo_name in repo_list:
        result = get_label_per_issue(repo_result[repo_name])
        result['nameWithOwner'] = repo_name
        result_list = add_result_list(result_list, result)

    print(json.dumps(result_list, indent=4))

    return result_list
