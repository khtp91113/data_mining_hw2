from sklearn import tree
import graphviz
from subprocess import call

mapping = [{'student': 1, 'others': 0}, {'high': 1, 'low': 0}, {'boring': 0, 'interesting': 1}, {'nice': 1, 'normal': 0}, {'cost time': 0, 'free': 1}, {'male': 1, 'female': 0}, {'many activities': 1, 'less or no activities': 0}, {'someone playing': 1, 'nobody playing': 0}, {'many ads': 1, 'no ads': 0}]
feature_names = ['career', 'cost', 'playability', 'nice game', 'cost time', 'gender', 'activity', 'environment', 'ad']
class_names = ['won\'t play', 'will play']

def read_data():
    data = []
    label = []
    f = open('dataset.txt', 'r')
    while True:
        string = f.readline()        
        if string == '':
            break
        string = string.rstrip()
        parts = string.split(',')
        if len(parts) == 1:
            continue
        tmp = []
        for i in range(0, len(parts)-1):
            tmp.append(mapping[i][parts[i]])
        label.append(int(parts[-1]))
        data.append(tmp)
    f.close()
    return data, label

def main():
    data, label = read_data()
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(data, label)
    tree.export_graphviz(clf, out_file='tree.dot', feature_names=feature_names, class_names=class_names, filled=True, rounded=True)
    call(['dot', '-Tpng', 'tree.dot', '-o', 'tree.png'])

if __name__ == '__main__':
    main()
