from sklearn.neighbors import NearestCentroid
import json
import os


def NC():
    root_dir = "."

    with open(os.path.join(root_dir, "Supervised_Learning", "Angle_Data.json"), "r") as file:
        angles = json.load(file)

    x = []
    y = []
    for i in range(len(angles)):
        for j in range(len(angles[i])):
            x.append(angles[i][j])
            y.append(i)

    clf = NearestCentroid()
    clf.fit(x, y)

    return clf
