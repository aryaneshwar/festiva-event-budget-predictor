import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load data
data = pd.read_csv("data/events.csv")

# Convert categorical to numeric
data = pd.get_dummies(data, columns=["event_type", "city"])

# Features and target
X = data.drop("budget", axis=1)
y = data["budget"]

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Test prediction
sample = X_test.iloc[0:1]
prediction = model.predict(sample)

print("Predicted Budget:", int(prediction[0]))
print("Actual Budget:", int(y_test.iloc[0]))

from sklearn.metrics import mean_absolute_error

y_pred = model.predict(X_test)
error = mean_absolute_error(y_test, y_pred)

print("Mean Error:", int(error))
# Save feature columns
feature_columns = X.columns