import numpy as np
from sklearn import svm

from Cechy_ruchu_no_zero import get_motion_feature


def check_result(condition, results):
    ok = 0
    for result in results:
        if result == condition:
            ok += 1
    return float(ok)/len(results)*100, "%"

normalTotalMotion, normalAngleMotion = get_motion_feature("Pure_Traffic1", 250, 1550, 2)
abnormalTotalMotion, abnormalAngleMotion = get_motion_feature("Man_through_road4", 70, 160, 2)

normal = np.zeros(len(normalTotalMotion))
abnormal = np.ones(len(abnormalTotalMotion))

X = np.column_stack((np.append(normalTotalMotion, abnormalTotalMotion), np.append(normalAngleMotion, abnormalAngleMotion)))
y = np.append(normal, abnormal)

clf = svm.SVC(class_weight={1: 50})
print clf.fit(X, y)

testTotalMotion = get_motion_feature("Man_through_road2", 1350, 1550, 0)
testAngleMotion = get_motion_feature("Man_through_road2", 1350, 1550, 1)

test = np.column_stack((testTotalMotion, testAngleMotion))

print clf.predict(test)
print check_result(1, clf.predict(test))
