import os.path
import sys
from argparse import ArgumentParser
from pathlib import Path


class CLI:
    def __init__(self):
        self.input_file = Path('')
        self.output_file = None
        self.lang_file = None
        self.analyze_num = 1
        self.loc_arg = None

    def _set_argument(self):
        parser = ArgumentParser()

        parser.add_argument('path_to_input_file',
                            type=Path)

        parser.add_argument('-o',
                            '--out',
                            required=True,
                            type=Path,
                            help='path to output file')

        parser.add_argument('--num',
                            '-n',
                            type=int,
                            default=1,
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

        self.input_file = args.path_to_input_file  # type: Path
        self.output_file = args.out.expanduser().resolve()  # type: Path
        self.num = args.num  # type: int
        self.lang_file = args.lang  # type: Path
        self.loc_arg = args.loc

    @staticmethod
    def _get_file_list(path_to_input_file: Path):
        file_list = []
        with open(str(path_to_input_file), 'r') as f:
            for repository in f:
                # 末尾の改行を削除してリストに追加
                repository = repository.rstrip(os.linesep)
                # 最後に空行入れたりしてる場合を排除
                if len(repository) == 0:
                    continue
                file_list.append(repository)

        if not file_list:
            print('Error: file has no list', file=sys.stderr)
            sys.exit(1)

        return file_list

    @staticmethod
    def _get_number_of_analysis(analyze_num: int, repo_num: int):
        if analyze_num < 1:
            print('Error: number is negative number.', file=sys.stderr)
            sys.exit(1)

        if repo_num < analyze_num:
            return repo_num

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
        repository_list = self._get_file_list(self.input_file)

        # args.outは最後がfile名なのでdirectoryとfile名を分けてdirectoryを渡す
        self._make_directory(self.output_file.parent)

        # 対象とするrepository数を取得
        self.analyze_num = self._get_number_of_analysis(self.analyze_num,
                                                        len(repository_list))

        lang_list = None
        if self.lang_file is not None:
            lang_list = self._get_file_list(self.lang_file)

        return repository_list, self.output_file, self.analyze_num, lang_list, self.loc_arg
