from pandas import DataFrame


def out_quartile(result: DataFrame):
    print(result.quantile([0, 0.25, 0.5, 0.75, 1.0]))
