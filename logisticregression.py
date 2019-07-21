import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

frames = [pd.read_csv('first400.csv'), pd.read_csv('next700.csv')]

data_frame = pd.concat(frames)

data_frame = data_frame.drop(data_frame[data_frame.genre.isnull()].index)
data_frame = data_frame.drop('book_number', 1)
data_frame = data_frame.drop('author.1', 1)
data_frame = data_frame.drop('title', 1)

features = data_frame.drop('genre', 1)
labels = data_frame.genre

print(labels.value_counts())

for i in range(10):
    training_features, validation_features, training_labels, validation_labels = train_test_split(features, labels)

    logreg = LogisticRegression(
        penalty='l2',
        dual=False,
        tol=0.000001,
        C=10.0,
        fit_intercept=True,
        intercept_scaling=1,
        class_weight=None,
        random_state=1,
        solver='newton-cg',
        max_iter=100,
        multi_class='multinomial',
        verbose=0,
        warm_start=False,
        n_jobs=1)
    logreg.fit(training_features, training_labels)

    validation_predictions = logreg.predict(validation_features)

    unique, counts = np.unique(validation_predictions, return_counts=True)
    print(dict(zip(unique, counts)))

    accuracy = accuracy_score(validation_predictions, validation_labels)
    print(accuracy)

