import os.path
import sys
from argparse import ArgumentParser
from pathlib import Path
import json


class CLI:
    def __init__(self):
        self.gcm_result = Path('')
        self.repository_list_file = Path('')  # type: Path
        self.output_file = None
        self.lang_file = None
        self.analyze_num = -1
        self.loc_arg = None

    def _set_argument(self):
        parser = ArgumentParser()

        parser.add_argument('gcm_result',
                            type=Path)

        parser.add_argument('--repo',
                            type=Path,
                            default=None,
                            help='repository list file')

        parser.add_argument('-o',
                            '--out',
                            required=True,
                            type=Path,
                            help='path to output file')

        parser.add_argument('--num',
                            '-n',
                            type=int,
                            default=-1,
                            help='analyze a number of repositories')

        parser.add_argument('--lang',
                            type=Path,
                            default=None,
                            help='specify language')

        parser.add_argument('--loc',
                            default=['comment', 'blank', 'code'],
                            nargs='*',
                            choices=['comment', 'blank', 'code'],
                            help='choose comment, blank, code')

        args = parser.parse_args()

        with open(str(args.gcm_result), 'r') as f:
            self.gcm_result = json.load(f)  # type: dict
        self.repository_list_file = args.repo
        self.output_file = args.out.expanduser().resolve()  # type: Path

        # analyze_numに，numが0より大きいならnumを，そうでないならgcm resultのリポジトリ数を入れる
        if args.num > 0:
            self.analyze_num = args.num  # type: int
        else:
            self.analyze_num = len(self.gcm_result['repository'].keys())
            print(self.analyze_num)

        self.lang_file = args.lang  # type: Path
        self.loc_arg = args.loc

    @staticmethod
    def _get_file_list(path_to_input_file: Path):
        file_list = []
        list_set = set()
        with open(str(path_to_input_file), 'r') as f:
            for repository in f:
                # 末尾の改行を削除してリストに追加
                repository = repository.rstrip(os.linesep)
                # 最後に空行入れたりしてる場合を排除
                if len(repository) == 0:
                    continue

                if not (repository in list_set):
                    file_list.append(repository)

                list_set.add(repository)

        if not file_list:
            print('Error: file has no list', file=sys.stderr)
            sys.exit(1)

        return file_list

    @staticmethod
    def _get_number_of_analysis(analyze_num: int, repo_num):
        if repo_num < analyze_num:
            analyze_num = repo_num

        if analyze_num < 1:
            print('Error: --repo number is not positive or repo file has no list.', file=sys.stderr)
            sys.exit(1)
        return analyze_num

    @staticmethod
    def _make_directory(path_to_output_dir: Path):
        if path_to_output_dir.exists():
            return

        path_to_output_dir.mkdir(parents=True)
        print('make directory: ', path_to_output_dir)

    # parseして以降の処理で扱える形にした結果を返す．
    def parse(self):
        self._set_argument()

        # 対象とするリポジトリリストを取得，ファイルで指定されていない場合はgcm resultから取得
        if self.repository_list_file is not None:
            repository_list = self._get_file_list(self.repository_list_file)
        else:
            repository_list = self.gcm_result['repository'].keys()

        # args.outは最後がfile名なのでdirectoryとfile名を分けてdirectoryを渡す
        self._make_directory(self.output_file.parent)

        # 対象とするrepository数を取得
        self.analyze_num = self._get_number_of_analysis(self.analyze_num, len(repository_list))

        lang_list = None
        if self.lang_file is not None:
            lang_list = self._get_file_list(self.lang_file)

        return self.gcm_result, repository_list, self.output_file, self.analyze_num, lang_list, self.loc_arg
