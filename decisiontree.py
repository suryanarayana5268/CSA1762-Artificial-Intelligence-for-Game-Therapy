from sklearn.tree import DecisionTreeClassifier
import pandas as pd
data = {
    'Age': ['<=30', '<=30', '31-40', '>40', '>40', '>40', '31-40', '<=30', '<=30', '>40', '<=30', '31-40', '31-40', '>40'],
    'Income': ['High', 'High', 'High', 'Medium', 'Low', 'Low', 'Low', 'Medium', 'Low', 'Medium', 'Medium', 'Medium', 'High', 'Medium'],
    'Student': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'Yes'],
    'Credit_Rating': ['Fair', 'Excellent', 'Fair', 'Fair', 'Fair', 'Excellent', 'Excellent', 'Fair', 'Fair', 'Fair', 'Excellent', 'Excellent', 'Fair', 'Excellent'],
    'Buys_Computer': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']
}
df = pd.DataFrame(data)
df = df.apply(lambda col: col.astype('category').cat.codes)
X = df[['Age', 'Income', 'Student', 'Credit_Rating']]
y = df['Buys_Computer']
model = DecisionTreeClassifier(criterion='entropy', random_state=0)
model.fit(X, y)
new_customer = pd.DataFrame([[0, 1, 1, 0]], columns=['Age', 'Income', 'Student', 'Credit_Rating'])
prediction = model.predict(new_customer)
print("Prediction for new customer (Buys_Computer):", 'Yes' if prediction[0] == 1 else 'No')
