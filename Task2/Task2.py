# ============================================
# AI PROJECT 2 - DATA CLASSIFICATION USING AI
# DecodeLabs Internship Project
# ============================================

# Import Libraries
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# ============================================
# STEP 1: LOAD DATASET
# ============================================

iris = load_iris()

# Create DataFrame
data = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

# Add target column
data['target'] = iris.target

print("First 5 Rows of Dataset:\n")
print(data.head())

# ============================================
# STEP 2: DEFINE FEATURES AND LABELS
# ============================================

X = iris.data      # Features
y = iris.target    # Labels

# ============================================
# STEP 3: SPLIT DATASET
# ============================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Data Size:", len(X_train))
print("Testing Data Size:", len(X_test))

# ============================================
# STEP 4: CREATE MODEL
# ============================================

model = LogisticRegression(max_iter=200)

# ============================================
# STEP 5: TRAIN MODEL
# ============================================

model.fit(X_train, y_train)

print("\nModel Training Completed!")

# ============================================
# STEP 6: MAKE PREDICTIONS
# ============================================

y_pred = model.predict(X_test)

# ============================================
# STEP 7: EVALUATE MODEL
# ============================================

accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", accuracy * 100, "%")

print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

# ============================================
# STEP 8: TEST CUSTOM INPUT
# ============================================

sample = [[5.1, 3.5, 1.4, 0.2]]

prediction = model.predict(sample)

print("\nPrediction for sample data:", prediction[0])

# Convert numeric prediction to flower name
flower_name = iris.target_names[prediction[0]]

print("Predicted Flower:", flower_name)