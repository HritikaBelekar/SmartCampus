import streamlit as st
import time

from streamlit_option_menu import option_menu


image = Image.open('/mount/src/Smart_Campus/Architechture_Face_Recog.png')

with st.sidebar:
    
    selected = option_menu('Face Recognition Module',
                          
                          ['About Project',
                           'Project Contributors',
                           'Architechture Diagram',
                           'Face Recognition'
                            ],
                          icons=['activity','activity','activity','activity'],
                          default_index=0)

if (selected == 'About Project'):
    # page title
    st.title('Smart Campus Surveillance & Guidance System')
    st.markdown('Aim of the project is to build a machine learning model capable of predicting wheather or not someone has heart disease based on their medical attributes.')
    st.image(image, caption='Architecture Diagram')
    

if (selected == 'Project Contributors'):
    st.title("1. Sanjana Marode")
    st.title("2. Hritika Belekar")
    st.title("3. Pallavi Kurve")

if (selected == 'Architecture Diagram'):
    st.markdown("")

    # page title
# Heart Disease Prediction Page
if (selected == 'Face Recognition'):

# Set a title for your app
    st.title('Smart Campus Surveillance & Guidance System')

    st.title("Upload Video File")

    # Create a file uploader widget
    uploaded_file = st.file_uploader("Upload a file", type=["txt", "csv", "pdf", "jpg", "png"])

    if st.button("Run Face Recognition Module"):
        # Display a spinner while some processing is happening
        with st.spinner("Model Processing..."):
            # Simulate some time-consuming task (e.g., sleep for a few seconds)
            time.sleep(3)
    # Remove the spinner after the task is done
