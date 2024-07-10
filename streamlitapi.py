import pickle
import streamlit as st

model = pickle.load(open('salary_prediction_model.pkl', 'rb'))

def main():
    st.title('MEF Salary Prediction')

    # Display the image
    st.image('sal.png', caption='mef', use_column_width=True)

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
