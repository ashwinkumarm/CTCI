""" This script pulls in mnist data, builds and test predictive models, and then
    make digits prediction on test data. """

__author__ = 'Ashwin Kumar Muruganandam'
__email__ = 'ashwinkumarmuruganandam@gmail.com'

import pickle
import numpy as np
import gzip
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.pipeline import make_pipeline
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import cross_val_score
from sklearn import metrics
from sklearn.model_selection import RandomizedSearchCV


def _float_to_block(d):
    """ Helper function to display the digit. """
    keys = [0.2, 0.4, 0.6, 0.8, 1]
    mapping = {0.2: " ", 0.4: "░", 0.6: "▒", 0.8: "▓", 1: "█"}
    for key in keys:
        if d <= key:
            return mapping[key]


def console_print(digit):
    """  Function to display the digit. """
    for row in digit:
        line = ""
        for cell in row:
            line = line + _float_to_block(cell)
        print(line)


def load_file(file_path):
    """ Loads the file given the path. """
    with gzip.open(file_path, "rb") as f:
        data, labels = pickle.load(f)
    f.close()
    return data, labels


def calc_no_of_misclassification(pred, y_test):
    """ Returns a dictionary for number of misclassification
         for each category. """
    d = {}
    for p, a in zip(pred, y_test):
        if p != a:
            if a in d:
                d[a] = d[a] + 1
            else:
                d[a] = 0
    return d


def construct_random_grid():
    """ Constructs random grid for tuning hyper parameter. """
    # Number of trees in random forest
    n_estimators = [int(x) for x in np.linspace(start=40, stop=60, num=10)]
    # Maximum number of levels in tree
    max_depth = [int(x) for x in np.linspace(10, 110, num=11)]
    max_depth.append(None)
    # Minimum number of samples required to split a node
    min_samples_split = [2, 5, 10]
    # Minimum number of samples required at each leaf node
    min_samples_leaf = [1, 2, 4]

    # Create the random grid
    random_grid = {'n_estimators': n_estimators,
                   'max_depth': max_depth,
                   'min_samples_split': min_samples_split,
                   'min_samples_leaf': min_samples_leaf
                   }

    return random_grid


def get_best_pram_random_forest():
    """ Finds the best parameter for random forest. """
    rf = RandomForestClassifier()
    grid = RandomizedSearchCV(estimator=rf, param_distributions=construct_random_grid(), n_iter=100, cv=3,
                              random_state=42, n_jobs=-1)
    grid.fit(feature_data_2dim, labels)
    print
    grid.best_params_


def plot_confusion_matrix(cm, title='Confusion matrix', cmap=plt.cm.Blues):
    """ plots the confusion matrix using matplotlib."""

    print
    "Confusion Matrix: "
    print
    cm

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(10)
    plt.xticks(tick_marks, ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
    plt.yticks(tick_marks, ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
    plt.tight_layout()

    plt.ylabel('True label')
    plt.xlabel('Predicted label')


def misclassified_cat7_with_cat1(pred, y_test):
    """" Returns the misclassified index of categories with are 7 but predicted as 1. """
    index = 0
    misclassified_index = []
    for predict, actual in zip(pred, y_test):
        if predict != actual and predict == 1 and actual == 7:
            misclassified_index.append(index)
        index += 1
    return misclassified_index


def plot_misclassified_cat7_with_cat1(misclassified_index, X_test, pred, y_test):
    """ Plots the misclassified data, predicted 7 actual 1. """
    plt.figure(figsize=(15, 15))
    for plotIndex, wrong in enumerate(misclassified_index[1:26]):
        plt.subplot(5, 5, plotIndex + 1)
        plt.imshow(np.reshape(X_test[wrong], (28, 28)), cmap=plt.cm.gray)
        plt.title('Predicted: {}, Actual: {}'.format(pred[wrong], y_test[wrong]))


def create_models(run_settings):
    """ creates the models which using the run_settings provided.
        0 - Only logistic Regression
        1 - Runs the best model. In our case we know its Random Forest
        2 - Runs all the models and finds the best one."""
    models = []

    # Logistic Regression
    lr = LogisticRegression()
    if run_settings == 0:
        models.extend([lr])
    # Random Forest Classifier
    rf = RandomForestClassifier(n_estimators=80, min_samples_split=5, max_depth=20, min_samples_leaf=1)
    if run_settings == 1:
        models.extend([rf])
    # Pipeline of PCA with Logistic Regression
    lr_std_pca = make_pipeline(PCA(), LogisticRegression())
    # Gradient Boosting Classifier
    gbm = GradientBoostingClassifier(n_estimators=40)
    if run_settings == 2:
        models.extend([lr, rf, lr_std_pca, gbm])
    return models


def tuning_best_model(models):
    """ It does the cross validation for given models list and returns the best model. """
    print("Beginning cross validation")
    max_acc = -1
    for model in models:
        scores = cross_val_score(model, X_train, y_train, cv=4)
        acc, var = scores.mean(), scores.std() * 2
        print
        model
        if max_acc < acc:
            max_acc = acc
            best_model = model
    print
    'Best Model'
    print
    best_model
    return best_model


def eval_model_predictions(model, X_train, y_train, X_test):
    """ Evaluates the model and also returns the predictions for test data set."""
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    print
    "accuracy is ", metrics.accuracy_score(y_test, pred)
    return pred


def get_file_path():
    """ returns the file path """
    path = "D:\\Downloads\\ericsson-mnist-assignment.pkl.gz"
    return path


def convert_to_two_dimensional(data):
    """ converts and returns the data in 2 dimensional """
    n_samples, nx, ny = data.shape
    data_2dim = data.reshape((n_samples, nx * ny))
    return data_2dim


def pipeline_create_tune_models(run_model_conf):
    running_model_dict = {0: "Logistic Regression",
                          1: "best model (random forest in our case)",
                          2: "all our model (Logistic, pipeline with logistic and PCA, Random forest and gradient boositng)"
                          }
    print
    "Running ", running_model_dict[run_model_conf]
    models = create_models(run_model_conf)
    best_model = tuning_best_model(models)
    return best_model


# this helps us to use the import this class and use the above functions
# without the following code being executed
if __name__ == '__main__':
    # define input file paths
    file_path = get_file_path()

    # load data
    print
    "loading data"
    feature_data, labels = load_file(file_path)

    # Examine the data
    print
    "Training data shape, ", feature_data.shape
    print
    "Target data shape, ", labels.shape
    # print random digit to verify print function
    console_print(feature_data[1])

    # converting the ndarray to 2 dimensional
    feature_data_2dim = convert_to_two_dimensional(feature_data)

    # examining the modified data
    print
    "Shape of modified data to 2 dimensional, ", feature_data_2dim.shape

    # Splitting the data for train and test.
    # We can avoid this because we are using cross validation in our case.
    #  But since we dont have separte test data set we need to go for this.
    X_train, X_test, y_train, y_test = train_test_split(feature_data_2dim, labels, test_size=0.30, random_state=1)

    # Creates the model and returns the best model.
    #  0 - only logistic regression.
    #  1 - best model (random forest in our case).
    #  2 - creates all our model
    # Configure the model you want to run here.
    run_model_conf = 1
    best_model = pipeline_create_tune_models(run_model_conf)

    # We evaluate the best model with our entire training data and evaluate our model's performance
    best_model.fit(X_train, y_train)
    predictions = best_model.predict(X_test)
    print
    "Accuracy of our model is ", metrics.accuracy_score(y_test, predictions)

    # prints a dict of key - category and value - no of misclassification
    d = calc_no_of_misclassification(predictions, y_test)
    print
    "Dictionary of misclassifications for each category: "
    print
    d

    # We understand that 7 is being misclassify a lot, followed by 1.
    # Now Let's explore more on this and verify by creating a confusion matrix.
    # The confusion matrix would help us explore more on the misclassfication and
    # would let us know which pairs are wrongly judged if applicable.

    # creating and ploting confusion matrix.
    cm = confusion_matrix(y_test, predictions)
    plot_confusion_matrix(cm)

    # using heat map provided by sns just for clearer view
    sns.heatmap(cm)
    plt.ylabel('actual')
    plt.xlabel('predicted')

    # Since we understand that 1 and 7 are wrongly predicted.
    # Lets explore few of the wrongly predicted data in this category to get a better understanding
    # and what can be done next

    # gets the misclassified list of index. actual 7 but predicted as 1 and plots them
    d = misclassified_cat7_with_cat1(predictions, y_test)
    plot_misclassified_cat7_with_cat1(d, X_test, predictions, y_test)

    # We can infer that several images are acually 7 but being labelled wrongly as 1.
    # To improve the performance of the model, we dont have to go for bigger ensemble models.
    # All we need to do is find the data which are wrongly labelled and correctly label them.



