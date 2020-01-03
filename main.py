import gcm_analyzer.repo_metrics.cloc_analyzer.cloc_analyzer as ca
import json


def main():
    with open('test_out.json', 'r') as f:
        result = json.load(f)
    ca.get_all_repo_cloc(lang_list=['Python', 'Markdown'],
                         loc_args=['comment', 'blank', 'code'],
                         repo_list=['LakeRainSound/get_code_metrics',
                                    'LakeRainSound/sample-java-project'],
                         repo_result=result['repository'])
    return


if __name__ == '__main__':
    main()
