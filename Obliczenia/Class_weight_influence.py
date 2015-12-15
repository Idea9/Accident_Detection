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

testTotalMotion, testAngleMotion = get_motion_feature("Man_through_road4", 70, 160, 2)
test = np.column_stack((testTotalMotion, testAngleMotion))

xx = []
yy = []
for i in range(1, 10):
    clf = svm.SVC(class_weight={1: i})
    print clf.fit(X, y)
    a = clf.predict(test)
    print check_result(1, a)
    xx.append(i)
    yy.append(check_result(1, a))

line, = plt.plot(xx, yy, 'g', linewidth=2)
plt.grid(True)
plt.title("Class weight influence on Anomaly Detection")
plt.xlabel("Waga probek klasy 1")
plt.ylabel("Prawidlowe probki[%]")
plt.show()
