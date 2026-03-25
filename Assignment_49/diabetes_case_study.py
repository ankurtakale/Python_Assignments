#-----------------------------------------------------------------------------------------
#   1. Exploratory Data Analysis (EDA):
#           Load the dataset using pandas.
#           Display the first 5 rows.
#           Show column info and check for null values.
#           Display basic statistics using .describe ().
#           Plot the distribution of the target variable (Outcome).
#           Use graphs like hist, boxplot, or pairplot to identify patterns or outliers.
#
#   2. Data Preprocessing:
#           Check and handle missing or zero values in columns like Glucose, BloodPressure, etc.
#           Apply feature scaling using StandardScaler or MinMaxScaler.
#           Split the dataset into features (X) and target (y).
#
#   3. Model Building:
#           Train at least 2 different algorithms on the dataset:
#           Logistic Regression
#           K-Nearest Neighbors (KNN)
#           Decision Tree
#           Use train test split to divide the data.
#
#   4. Model Evaluation:
#           Print accuracy score, confusion matrix, precision, recall, and F1 score.
#           Use matplotlib or seaborn to visualize confusion matrix.
#
#   5. Final Output:
#           Predict whether a patient is diabetic based on test data.
#           Display predictions on screen and save them in a CSV file.
#-----------------------------------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix,recall_score,precision_score,f1_score

border = "-"*70 

def evaluate_models(Y_test, tree_pred, knn_pred, logistic_pred):

    results = {
        "Model": ["Decision Tree", "KNN", "Logistic Regression"],
        "Accuracy": [
            accuracy_score(Y_test, tree_pred),
            accuracy_score(Y_test, knn_pred),
            accuracy_score(Y_test, logistic_pred)
        ],
        "Precision": [
            precision_score(Y_test, tree_pred),
            precision_score(Y_test, knn_pred),
            precision_score(Y_test, logistic_pred)
        ],
        "Recall": [
            recall_score(Y_test, tree_pred),
            recall_score(Y_test, knn_pred),
            recall_score(Y_test, logistic_pred)
        ],
        "F1 Score": [
            f1_score(Y_test, tree_pred),
            f1_score(Y_test, knn_pred),
            f1_score(Y_test, logistic_pred)
        ]
    }

    df_results = pd.DataFrame(results)

    # Sorting based on Recall first, then F1 Score
    df_results = df_results.sort_values(by=["Recall", "F1 Score"], ascending=False)

    best_model_name = df_results.iloc[0]["Model"]

    return best_model_name

def data_preprocessing(df):

    # Handling missing or 0 values
    cols = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
    df[cols] = df[cols].replace(0,pd.NA)

    df.fillna(df.mean(),inplace=True)

    # Feature splitting
    X = df.drop('Outcome',axis=1)
    Y = df['Outcome']

    # Feature scaling
    scaler = StandardScaler()
    x_scaled = scaler.fit_transform(X)

    X_train,X_test,Y_train,Y_test = train_test_split(x_scaled,Y,test_size=0.2,random_state=42)

    tree_model = DecisionTreeClassifier(max_depth=3,random_state=42)
    knn_model = KNeighborsClassifier(n_neighbors=4)
    logistic_model = LogisticRegression(max_iter=500,random_state=42)

    tree_model.fit(X_train,Y_train)
    tree_pred = tree_model.predict(X_test)

    knn_model.fit(X_train,Y_train)
    knn_pred = knn_model.predict(X_test)

    logistic_model.fit(X_train,Y_train)
    logistic_pred = logistic_model.predict(X_test)

    print(border)

    print("Decision Tree accuracy : ",accuracy_score(Y_test,tree_pred))
    print("Decision tree confusion matrix : ")
    tree_cm = confusion_matrix(Y_test,tree_pred)
    print(tree_cm)
    print("Decision tree precision :",precision_score(Y_test,tree_pred))
    print("Decision tree recall :",recall_score(Y_test,tree_pred))
    print("Decision tree f1 score :",f1_score(Y_test,tree_pred))

    print(border)

    print("KNN accuracy : ",accuracy_score(Y_test,knn_pred))
    print("KNN confusion matrix : ")
    knn_cm = confusion_matrix(Y_test,knn_pred)
    print(knn_cm)
    print("KNN precision :",precision_score(Y_test,knn_pred))
    print("KNN recall :",recall_score(Y_test,knn_pred))
    print("KNN f1 score :",f1_score(Y_test,knn_pred))

    print(border)

    print("Logistic Regression accuracy : ",accuracy_score(Y_test,logistic_pred))
    print("Logistic Regression confusion matrix : ")
    logistic_cm = confusion_matrix(Y_test,logistic_pred)
    print(logistic_cm)
    print("Logistic Regression precision :",precision_score(Y_test,logistic_pred))
    print("Logistic Regression recall :",recall_score(Y_test,logistic_pred))
    print("Logistic Regression f1 score :",f1_score(Y_test,logistic_pred))

    print(border)

    sns.heatmap(tree_cm,annot=True,fmt='d',cmap='Oranges')
    plt.title("Decision Tree Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.show()

    sns.heatmap(knn_cm,annot=True,fmt='d',cmap='Blues')
    plt.title("KNN Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.show()

    sns.heatmap(logistic_cm,annot=True,fmt='d',cmap='Greens')
    plt.title("Logistic Regression Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.show()

    best_model = evaluate_models(Y_test,tree_pred,knn_pred,logistic_pred)

    # Best model selection on the basis of recall and f1 score
    if best_model == "Decision Tree":
        final_model = tree_model
    elif best_model == "KNN":
        final_model = knn_model
    else:
        final_model = logistic_model

    final_prediction = final_model.predict(X_test)

    print("\nFirst 20 final predictions : ",final_prediction[:20])

    output = pd.DataFrame({
        "Actual" : Y_test.values,
        "Predicted" : final_prediction
    })

    # Saving the predictions to a csv file
    output.to_csv("predictions.csv",index=False)

    print("Predictions saved to predictions.csv")

def data_analysis(filename):
    df = pd.read_csv(filename)

    print("First 5 entries : ")
    print(df.head())

    print(border)

    print("Column info : ")
    print(df.columns)

    df.info()

    print(border)

    print("null values count : ")
    print(df.isnull().sum())

    print(border)

    print("description : ")
    print(df.describe())

    print(border)

    plt.figure(figsize=(6,6))
    sns.countplot(data=df,x='Outcome')
    plt.show()

    df.hist(figsize=(10,10))
    plt.show()

    plt.figure(figsize=(8,6))
    sns.boxplot(data=df)
    plt.show()

    data_preprocessing(df)

def main():
    
    data_analysis("diabetes.csv")

if __name__ == "__main__":
    main()