import sys


class RepositoryList:
    def __init__(self, repository_list, gcm_result, number_of_repo: int):
        self.repository_list = repository_list
        self.gcm_result = gcm_result
        self.number_of_repo = number_of_repo

    @staticmethod
    def _is_error(repo_name, result_dict):
        if 'errors' in result_dict:
            print('ERROR: {}'.format(repo_name))
            for error in result_dict['errors']:
                print(error['message'])
            return True

        return False

    def _repository_exists(self, repo_name):
        if not(repo_name in self.gcm_result.keys()):
            print('ERROR: {} doesn\'t exist in gcm result file'.format(repo_name))
            return False

        return True

    @staticmethod
    def _repository_list_empty(no_error_repo_list):
        if len(no_error_repo_list) == 0:
            print("ERROR: No Repository which has no error.", file=sys.stderr)
            sys.exit(1)

    def get_no_error_repo_list(self):
        no_error_repo_list = []
        i = 0
        # 重複を排除するためのset
        repository_set = set()
        for repo_name in self.repository_list:
            # 結果にそもそも指定したリポジトリが存在していない場合は飛ばす
            # あるいはすでに追加したリポジトリは削除
            if not self._repository_exists(repo_name) or repo_name in repository_set:
                continue

            repository = self.gcm_result[repo_name]

            error_flag = False
            if self._is_error(repo_name, repository):
                error_flag = True

            if self._is_error(repo_name, repository['cloc']):
                error_flag = True

            # すべてのエラーに引っかからなかった場合
            if not error_flag:
                no_error_repo_list.append(repo_name)
                repository_set.add(repo_name)
                i += 1

            if i == self.number_of_repo:
                break

        self._repository_list_empty(no_error_repo_list)

        return no_error_repo_list
