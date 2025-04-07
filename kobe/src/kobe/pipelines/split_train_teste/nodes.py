"""
This is a boilerplate pipeline 'split_train_teste'
generated using Kedro 0.19.12
"""
from sklearn.model_selection import train_test_split


def split_data(data, target_column, test_size=0.2, random_state=42):
    X = data.drop(columns=[target_column])
    y = data[target_column]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )

    train = X_train.copy()
    train[target_column] = y_train

    test = X_test.copy()
    test[target_column] = y_test

    return train, test

