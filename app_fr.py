import streamlit as st
import time
from PIL import Image

from streamlit_option_menu import option_menu


image = Image.open('/mount/src/SmartCampus/Architechture_Face_Recog.png')

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
    st.markdown('Aim of the project is to build a machine learning based Smart Campus Surveillance model which checks whether students are attending \
        the lectures or bunking the lectures based on the camera feed received from the camera installed in the campus. It will send a alert notification to respective HOD or Class Teacher about the bunks done by student')
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
