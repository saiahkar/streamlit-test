import pickle
import streamlit as st
import os

# Load the model using a relative path
model_path = 'salary_prediction_model.pkl'
if os.path.exists(model_path):
    model = pickle.load(open(model_path, 'rb'))
else:
    st.error(f'Model file not found: {model_path}')
    model = None

def main():
    st.title('MEF Salary Prediction')

    # Display the image
    st.image('sal.png', caption='mef', use_column_width=True)

    # Input variable
    Year = st.text_input('Year')
    
     # Prediction code
    if st.button('Predict'):
        if model:
            try:
                # Convert the input to float
                Year = float(Year)
                makeprediction = model.predict([[Year]])
                output = round(makeprediction[0], 2)
                st.success(f'The predicted salary is {output}')
            except ValueError:
                st.error('Please enter a valid numeric value for Year')
        else:
            st.error('Model is not loaded properly.')

if __name__ == '__main__':
    main()