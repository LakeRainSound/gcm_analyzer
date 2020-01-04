import pandas
import json


def _create_result_list():
    result_list = {
                    "nameWithOwner": [],
                    "hasIssuesEnabled": [],
                    "closedIssueCount": [],
                    "hasLabelClosedIssue": [],
                }
    return result_list


def _add_result_list(result_list: dict, result: dict):
    for key in result_list.keys():
        result_list[key].append(result[key])

    return result_list


def get_all_issues_info(repository_result, repository_list):
    result_list = _create_result_list()

    for repo_name in repository_list:
        result_list = _add_result_list(result_list, repository_result[repo_name])

    print(json.dumps(result_list, indent=4))

    return result_list
