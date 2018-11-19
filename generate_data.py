import random
M = 10000
# features: 1. career, 2. cost, 3. playability, 4.nice game, 5. cost time, 6. gender, 7. activity, 8. environment, 9. ad
mapping = [['others', 'student'], ['low', 'high'], ['boring', 'interesting'], ['normal', 'nice'], ['cost time', 'free'], ['female', 'male'], ['less or no activities', 'many activities'], ['nobody playing', 'someone playing'], ['no ads', 'many ads']]

def find_label(features):
    # others
    if features[0] == 0:
        # boring
        if features[2] == 0:
            return 0
        # interesting
        else:
            # nice game
            if features[3] == 1:
                return 1
            else:
                # cost time
                if features[4] == 0:
                    return 0
                else:
                    # female
                    if features[5] == 0:
                        return 0
                    else:
                        # many activities
                        if features[6] == 1:
                            return 1
                        else:
                            # somebody playing
                            if features[7] == 1:
                                return 1
                            else:
                                # ad
                                return features[8]
    else:
        # high price
        if features[1] == 1:
            return 0
        else:
            # boring
            if features[2] == 0:
                return 0
            # interesting
            else:
                # nice game
                if features[3] == 1:
                    return 1
                else:
                    # female
                    if features[5] == 0:
                        return 0
                    else:
                        # many activities
                        if features[6] == 1:
                            return 1
                        else:
                            # somebody playing
                            if features[7] == 1:
                                return 1
                            else:
                                # ad
                                return features[8]
    
def generate_data():
    data = []
    for counts in range(0, M):
        features = []
        for i in range(0, 9):
            features.append(random.randint(0, 1))
        label = find_label(features)
        features.append(label)
        data.append(features)
    return data

def main():
    data = generate_data()
    f = open('dataset.txt', 'w')
    f.write('career\tcost\tplayability\tnice game\tcost time\tgender\tactivity\tenvironment\tad\tlabel\n')
    for features in data:
        for i in range(0, 9):
            f.write(mapping[i][features[i]])
            f.write(',')
        f.write(str(features[9]))
        f.write('\n')
    f.close()

if __name__ == '__main__':
    main()
