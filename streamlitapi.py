import pickle
import streamlit as st
import os
import sklearn


# Load the model from the current directory
model_path = 'salary_prediction_model.pkl'

try:
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
except FileNotFoundError:
    st.error(f'Model file not found: {model_path}')
    model = None

def main():
    st.title('MEF Salary Prediction')

    # Display the image
    image_path = 'sal.png'
    if os.path.exists(image_path):
        st.image(image_path, caption='mef', use_column_width=True)
    else:
        st.warning('Image file not found: {}'.format(image_path))

    # Input variable
    Year = st.text_input('Year')
    
    # Prediction code
    if st.button('Predict'):
        try:
            # Convert the input to float
            Year = float(Year)
            makeprediction = model.predict([[Year]])
            output = round(makeprediction[0], 2)
            st.success(f'The predicted salary is {output}')
        except ValueError:
            st.error('Please enter a valid numeric value for Year')

if __name__ == '__main__':
    main()
