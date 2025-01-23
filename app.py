from flask import Flask, render_template, request, jsonify, redirect, url_for
import joblib

# Create a Flask app
app = Flask(__name__)

# Load the pre-trained AdaBoost model
model = joblib.load('best_Ada_boost.pkl')

# Define the home route
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

# Define the form route
@app.route('/form')
def form():
    return render_template('form.html')

# Define the prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form inputs
        bmi = request.form.get('BMI')
        family_history = request.form.get('FamilyHistoryKidneyDisease')
        systolic_bp = request.form.get('SystolicBP')
        fasting_blood_sugar = request.form.get('FastingBloodSugar')
        hba1c = request.form.get('HbA1c')
        serum_creatinine = request.form.get('SerumCreatinine')
        bun_levels = request.form.get('BUNLevels')
        gfr = request.form.get('GFR')
        protein_in_urine = request.form.get('ProteinInUrine')
        edema = request.form.get('Edema')
        muscle_cramps = request.form.get('MuscleCramps')
        itching = request.form.get('Itching')

        # Check if all fields are filled
        if not all([bmi, family_history, systolic_bp, fasting_blood_sugar, hba1c, serum_creatinine, bun_levels, gfr, protein_in_urine, edema, muscle_cramps, itching]):
            return render_template('form.html', error="!Please fill in all the fields")

        # Convert form inputs to the appropriate data types
        bmi = float(bmi)
        family_history = int(family_history)
        systolic_bp = int(systolic_bp)
        fasting_blood_sugar = float(fasting_blood_sugar)
        hba1c = float(hba1c)
        serum_creatinine = float(serum_creatinine)
        bun_levels = float(bun_levels)
        gfr = float(gfr)
        protein_in_urine = float(protein_in_urine)
        edema = int(edema)
        muscle_cramps = float(muscle_cramps)
        itching = float(itching)

        # Prepare the input features for the model
        input_features = [[bmi, family_history, systolic_bp, fasting_blood_sugar, hba1c, serum_creatinine, bun_levels, gfr, protein_in_urine, edema, muscle_cramps, itching]]

        # Make a prediction using the model
        prediction = model.predict(input_features)[0]

        # Determine the result message based on the prediction
        if prediction == 1:
            result_message = "The person suffers from chronic kidney disease"
        else:
            result_message = "The person does not suffer from chronic kidney disease"

        # Render the form template with the result
        return render_template('form.html', result=result_message)

        # Handle any exceptions and return the error message
    except Exception as e:
        return str(e)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
