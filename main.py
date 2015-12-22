import numpy as np
from sklearn import svm
from matplotlib import pyplot as plt
from Cechy_ruchu_no_zero import get_motion_feature


def check_result(condition, results):
    ok = 0
    for result in results:
        if result == condition:
            ok += 1
    return float(ok) / len(results) * 100


normalTotalMotion, normalAngleMotion = get_motion_feature("Pure_Traffic1", 250, 1550, 2)
abnormalTotalMotion, abnormalAngleMotion = get_motion_feature("Man_through_road2", 1350, 1550, 2)

normal = np.zeros(len(normalTotalMotion))
abnormal = np.ones(len(abnormalTotalMotion))

X = np.column_stack(
    (np.append(normalTotalMotion, abnormalTotalMotion), np.append(normalAngleMotion, abnormalAngleMotion)))
y = np.append(normal, abnormal)

testTotalMotion, testAngleMotion = get_motion_feature("Pure_Traffic3", 70, 1600, 2)
test = np.column_stack((testTotalMotion, testAngleMotion))


clf = svm.SVC(class_weight="balanced")
print clf.fit(X, y)
a = clf.predict(test)
print check_result(0, a)