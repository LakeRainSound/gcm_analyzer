import pandas
import json


def create_result_list():
    result_list = {
                    "nameWithOwner": [],
                    "hasIssuesEnabled": [],
                    "closedIssueCount": [],
                    "hasLabelClosedIssue": [],
                }
    return result_list


def add_result_list(result_list: dict, result: dict):
    for key in result_list.keys():
        result_list[key].append(result[key])

    return result_list


def get_all_issues_info(repo_result, repo_list):
    result_list = create_result_list()

    for repo_name in repo_list:
        result_list = add_result_list(result_list, repo_result[repo_name])

    print(json.dumps(result_list, indent=4))

    return result_list
