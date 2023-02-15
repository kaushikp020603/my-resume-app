import streamlit as st
from docxtpl import DocxTemplate
from io import BytesIO

# Define the questions
questions = [
    "What is your full name?",
    "What is your email address?",
    "provide your linkedIn Profile?",
    "What is your phone number?",
    "What is your current job title?",
    "Add a summary about yourself",
    "What is your work experience?",
    "What are your key skills?",
    "What is your education background?",
    "What are your certifications and awards?",
    "What is your desired job position?",
    "Do you have any references? If so, please provide their contact information."
]

# Define the template file
template_file = "resume_template.docx"

# Define helper functions for rendering the form and generating the resume
def render_form():
    with st.form("resume-form"):
        col1, col2 = st.beta_columns(2)
        responses = []
        for i, q in enumerate(questions):
            if i <= 5:
                response = col1.text_input(q)
            else:
                response = col2.text_input(q)
            responses.append(response)
        col1.write("")
        col2.write("")
        submitted = st.form_submit_button("Generate Resume")
    return submitted, responses

def generate_resume(responses):
    doc = DocxTemplate(template_file)
    context = {
        'full_name': responses[0],
        'email': responses[1],
        'linkedIn_Profile': responses[2],
        'phone_number': responses[3],
        'current_job_title': responses[4],
        'summary': responses[5],
        'work_experience': responses[6],
        'key_skills': responses[7],
        'education_background': responses[8],
        'certifications_awards': responses[9],
        'desired_job_position': responses[10],
        'references': responses[11]
    }
    doc.render(context)
    doc_bytes = BytesIO()
    doc.save(doc_bytes)
    return doc_bytes.getvalue()

#About 

def about():
    st.title("About")
    st.write("This app is a Resume Generator built with Streamlit and DocxTemplate. It allows you to generate a personalized resume/CV by filling out a form with your information.")
    st.write("""
    Made with :heart: by AfnanKhan
    """, unsafe_allow_html=True)

# Define the main function to run the app
def main():
    
    st.set_page_config(page_title="Resume Generator", page_icon=":guardsman:", layout="wide")
    
    # Set the page background color using the css property
    
    st.markdown(
    """
    <style>
    body {
        background-color: #F5F5F5;
    }
    </style>
    """,
    unsafe_allow_html=True
)
    st.title("Resume Generator")

    st.write("Welcome to the Resume Generator! Please fill out the form below to generate a personalized resume/CV.")

    submitted, responses = render_form()

    if submitted:
        st.write("Generating your resume... Please wait.")
        resume_buffer = generate_resume(responses)
        st.write("Resume successfully generated!")
        st.download_button(label="Download Generated Resume", data=resume_buffer, file_name="generated_resume.docx")
        st.write("""
Made with :heart: by AfnanKhan
""", unsafe_allow_html=True)

# Add a button to link to the About page
    st.sidebar.button("About", on_click=about)
    
if __name__ == "__main__":
    main()

