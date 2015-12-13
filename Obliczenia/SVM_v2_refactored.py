import numpy as np
from sklearn import svm

from Cechy_ruchu import get_motion_feature

normalTotalMotion = get_motion_feature("Pure_Traffic1", 50, 350, 0)
abnormalTotalMotion = get_motion_feature("Man_through_road4", 70, 160, 0)

normalAngleMotion = get_motion_feature("Pure_Traffic1", 50, 350, 1)
abnormalAngleMotion = get_motion_feature("Man_through_road4", 70, 160, 1)

normal = np.zeros(len(normalTotalMotion))
abnormal = np.ones(len(abnormalTotalMotion))

X = np.column_stack((np.append(normalTotalMotion, abnormalTotalMotion), np.append(normalAngleMotion, abnormalAngleMotion)))
y = np.append(normal, abnormal)

clf = svm.SVC()
print clf.fit(X, y)

testTotalMotion = get_motion_feature("Pure_Traffic3", 1350, 1550, 0)
testAngleMotion = get_motion_feature("Pure_Traffic3", 1350, 1550, 1)

test = np.column_stack((testTotalMotion, testAngleMotion))

print clf.predict(test)