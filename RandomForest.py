import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
import random as rand

# Load the CSV file
data = pd.read_csv('ALL_STARS.csv')

# Check for missing values
print("Missing values per column:")
print(data.isnull().sum())

# Define the columns you want to keep
selected_columns = [
    'ra_epoch2000', 'dec_epoch2000', 'errHalfMaj', 'errHalfMin', 'errPosAng', 
    'source_id', 'ra_x', 'ra_error', 'dec_x', 'dec_error', 'parallax', 'parallax_error', 
    'parallax_over_error', 'pm', 'pmra', 'pmra_error', 'pmdec', 'pmdec_error', 
    'astrometric_n_good_obs_al', 'astrometric_gof_al', 'astrometric_chi2_al', 
    'astrometric_excess_noise', 'astrometric_excess_noise_sig', 'astrometric_params_solved', 
    'pseudocolour', 'pseudocolour_error', 'visibility_periods_used', 'ruwe', 
    'duplicated_source', 'phot_g_mean_flux', 'phot_g_mean_flux_error', 'phot_g_mean_mag', 
    'phot_bp_mean_flux', 'phot_bp_mean_flux_error', 'phot_bp_mean_mag', 'phot_rp_mean_flux', 
    'phot_rp_mean_mag', 'phot_bp_rp_excess_factor', 'bp_rp', 'dr2_radial_velocity', 
    'dr2_radial_velocity_error', 'dr2_rv_nb_transits', 'dr2_rv_template_teff', 
    'dr2_rv_template_logg', 'panstarrs1', 'sdssdr13', 'skymapper2', 'urat1', 
    'phot_g_mean_mag_error', 'phot_bp_mean_mag_error', 'phot_rp_mean_mag_error', 
    'phot_g_mean_mag_corrected', 'phot_g_mean_mag_error_corrected', 'phot_g_mean_flux_corrected', 
    'phot_bp_rp_excess_factor_corrected', 'ra_epoch2000_error', 'dec_epoch2000_error', 
    'ra_dec_epoch2000_corr', 'angDist'
]

# Select only these columns
X = data[selected_columns]
y = data['source']

# Encode the target column ('source') as numeric
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

# Optionally, encode categorical features (if any remain in X)
X = pd.get_dummies(X, drop_first=True)

# Split the data into training (2/3) and holdout (1/3) sets
X_train, X_holdout, y_train, y_holdout = train_test_split(X, y, test_size=1/3, random_state=rand.randint(1, 150))

# Initialize the Random Forest model
rf_model = RandomForestClassifier(random_state=rand.randint(1, 150), class_weight='balanced')

# Perform cross-validation on the training data (optional)
cross_val_scores = cross_val_score(rf_model, X_train, y_train, cv=5, scoring='accuracy')  # cv=5 for 5-fold cross-validation

# Print cross-validation results
print(f"Cross-validation scores: {cross_val_scores}")
print(f"Mean cross-validation score: {cross_val_scores.mean():.4f}")

# Train the model on the training data
rf_model.fit(X_train, y_train)

# Evaluate the model on the holdout set
y_holdout_pred = rf_model.predict(X_holdout)

# Generate the classification report for the holdout set
print("Classification report for holdout set:")
print(classification_report(y_holdout, y_holdout_pred))

# Feature importance analysis
importances = rf_model.feature_importances_
feature_importances = pd.DataFrame({'Feature': X.columns, 'Importance': importances})
feature_importances = feature_importances.sort_values(by='Importance', ascending=False)

print("Top features by importance:")
print(sorted(feature_importances['Feature']))

# Plot the feature importances
plt.figure(figsize=(12, 8))
plt.bar(feature_importances['Feature'], feature_importances['Importance'])
plt.title('Feature Importance')
plt.xlabel('Features')
plt.ylabel('Importance')
plt.xticks(rotation=90)
plt.tight_layout()  # Automatically adjusts layout
plt.show()
