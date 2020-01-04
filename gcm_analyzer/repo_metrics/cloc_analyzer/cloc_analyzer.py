import json


def _create_result_dict(loc_args):
    result = {}
    # clocで取得するargを全て追加
    for loc_arg in loc_args:
        result[loc_arg] = 0
    result['cloc_sum'] = 0

    return result


def _get_loc_to_lang(lang_result: dict, loc_args):
    res = {}

    lang_sum = 0
    for loc_arg in loc_args:
        res[loc_arg] = lang_result[loc_arg]
        lang_sum += lang_result[loc_arg]

    res['cloc_sum'] = lang_sum
    return res


def _get_one_repo_cloc(cloc_result: dict, lang_list, loc_args):

    # clocの中身がない場合
    if cloc_result == {}:
        return _create_result_list(loc_args)

    # 言語の指定がない場合"SUM"部分を見て返す
    if lang_list is None:
        return _get_loc_to_lang(cloc_result['SUM'], loc_args)

    # 結果を格納するためのdictを作成
    all_lang_result = _create_result_dict(loc_args)

    # 指定された言語について結果を取得
    for lang in lang_list:
        # 所望の言語が結果にない場合は飛ばす
        if not (lang in cloc_result.keys()):
            continue

        # ある場合はget_loc_to_langから結果を受け取る
        result = _get_loc_to_lang(cloc_result[lang], loc_args)

        # loc_args + 'cloc_sum'の結果を加算
        for key in all_lang_result.keys():
            all_lang_result[key] += result[key]

    return all_lang_result


def _create_result_list(loc_args):
    all_result = {'nameWithOwner': [], 'cloc_sum': []}
    # clocで取得するargを全て追加
    for loc_arg in loc_args:
        all_result[loc_arg] = []

    return all_result


def _add_result_list(all_result: dict, result: dict):
    for key in all_result.keys():
        all_result[key].append(result[key])

    return all_result


def get_all_cloc_info(repository_result, repository_list, lang_list, loc_args):
    all_result = _create_result_list(loc_args)

    for repo_name in repository_list:
        cloc_result = repository_result[repo_name]['cloc']

        # clocの結果にrepo_nameを付け足す
        result = _get_one_repo_cloc(cloc_result, lang_list, loc_args)
        result['nameWithOwner'] = repo_name
        # 結果を付け足す
        all_result = _add_result_list(all_result, result)
    print(json.dumps(all_result, indent=4))
