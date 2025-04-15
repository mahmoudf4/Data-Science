import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

df_trips = pd.read_csv("Trips_by_Distance.csv")

# Features: number of trips at each distance band
X = df_trips[[
    'Number of Trips <1',
    'Number of Trips 1-3',
    'Number of Trips 3-5',
    'Number of Trips 5-10',
    'Number of Trips 10-25',
    'Number of Trips 25-50',
    'Number of Trips 50-100',
    'Number of Trips 100-250',
    'Number of Trips 250-500',
    'Number of Trips >=500'
]]

X = X.fillna(X.mean())

# Target: number of people who didn’t stay home
y = df_trips['Population Not Staying at Home'].fillna(y.mean())

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", round(mse))

r2 = r2_score(y_test, y_pred)
print("Mean Squared Error:", round(r2, 4))

# Optional: show coefficients
coefs = pd.Series(model.coef_, index=X.columns)
print("\nModel coefficients (importance of each trip type):")
print(coefs.sort_values(ascending=False))
