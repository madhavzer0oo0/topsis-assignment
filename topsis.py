import sys
import pandas as pd
import numpy as np

def topsis(input_file, weights, impacts, output_file):
    try:
        df = pd.read_excel(input_file)
        # df.to_csv("data.csv", index=False)
    except FileNotFoundError:
        print("Error: File not found")
        sys.exit(1)

    if df.shape[1] < 3:
        print("Error: Input file must contain at least 3 columns")
        sys.exit(1)

    data = df.iloc[:, 1:].values

    if not np.issubdtype(data.dtype, np.number):
        print("Error: Non-numeric data found")
        sys.exit(1)

    weights = list(map(float, weights.split(',')))
    impacts = impacts.split(',')

    if len(weights) != data.shape[1] or len(impacts) != data.shape[1]:
        print("Error: Weights, impacts and columns count mismatch")
        sys.exit(1)

    for i in impacts:
        if i not in ['+', '-']:
            print("Error: Impacts must be + or -")
            sys.exit(1)

    norm = np.sqrt((data ** 2).sum(axis=0))
    norm_data = data / norm
    weighted = norm_data * weights

    ideal_best = []
    ideal_worst = []

    for i in range(len(impacts)):
        if impacts[i] == '+':
            ideal_best.append(weighted[:, i].max())
            ideal_worst.append(weighted[:, i].min())
        else:
            ideal_best.append(weighted[:, i].min())
            ideal_worst.append(weighted[:, i].max())

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    dist_best = np.sqrt(((weighted - ideal_best) ** 2).sum(axis=1))
    dist_worst = np.sqrt(((weighted - ideal_worst) ** 2).sum(axis=1))

    score = dist_worst / (dist_best + dist_worst)

    df['Topsis Score'] = score
    df['Rank'] = df['Topsis Score'].rank(ascending=False).astype(int)

    df.to_csv(output_file, index=False)
    print("Result saved to", output_file)


if len(sys.argv) != 5:
    print("Usage: python topsis.py <InputFile> <Weights> <Impacts> <OutputFile>")
    sys.exit(1)

topsis(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
