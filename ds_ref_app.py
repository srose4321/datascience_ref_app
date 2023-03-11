import pandas as pd
import streamlit as st

st.title("Data Science Resources")
st.sidebar.subheader("Quick Links:")
links = st.sidebar.container()
with links:
    st.sidebar.write("Link to Pay Comparisons: [Payscale](https://www.payscale.com/research/US/Job=Data_Scientist/Salary)")
    st.sidebar.write("Link to Training Resources: [Learn DS Online](https://www.simplilearn.com/resources-to-learn-data-science-online-article)")
    st.sidebar.write("Link to Job Comparison: [Different DS Job Types](https://builtin.com/data-science/data-science-jobs)")
    
    
tab1, tab2, tab3 = st.tabs(["Overview", "Job Types", "Common Reqs"])
with tab1:
   st.header("Quick Overview of Data Science:")
   url = "https://www.youtube.com/embed/xvEKQefqQ7A"
   st.video(url)
   st.text("What is the roadmap to becoming a Data Scientist?")
   st.image("modern_ds.webp")
   st.image('ds_roadmap.png')
   st.markdown("""#### What is the difference between AI/ML/DS?
   Definitions: 

    - AI: François Chollet, creator of Keras, described it as “the effort to automate intellectual tasks normally performed by humans”.
    - ML: a pioneer of ML, Arthur Samuel, defined it as a “field of study that gives computers the ability to learn without being explicitly programmed”.
         -  Includes single layer NN
    - DL:  a subset of ML that is inspired by how human brains work
         -  Multi-layer NN, CNN, RNN

        """)
   st.image('venn1.jpg')
   st.image('diagram_2.png')
   st.markdown("""#### What does a Data Scientist do?
    Drawing useful conclusions from data using computation 

        - Data Wrangling and Preprocessing 
            -  Gather, clean, normalize data
            
        - Exploration 
            -  Identifying patterns in information 
            -  Uses visualizations 
            
        - Inference
            -  Quantifying whether those patterns are reliable 
            -  Uses randomization 
            
        - Prediction 
            -  Making informed guesses 
            -  Uses machine learning 
            
        - Deploying 
            -  Make model results/features available to stakeholders/other teams

        - Data Storytelling 
            -  Share results/findings from model/analyses with stakeholders/other teams""")
   st.image('ds_process_2.jpeg')
   st.image('data-prep-approach-time.png')
   

with tab2:
    st.header("Differences in DS Jobs")
    url2='https://youtu.be/VrdnBxx8BBI'
    st.video(url2)
    st.caption("For different types of jobs in Data Science, here are some skill focus separations. \
        Keep in mind that every company is different and can align their DS roles slightly differently. \
            This is meant as a guide, not a steadfast rule.")
    st.image("ds_skills_comparison.webp")
    st.caption("Within a role, there are ways you can distinguish yourself. Are you interested in focusing in one area\
        and becoming a subject matter expert? Are you very curious and want to explore lots of different areas and want \
            to become more of a generalist? While all of these are good options, it is helpful in interviews to know \
                yourself, so you can market your strengths")
    st.image("types_of_ds.jpg")

with tab3:
    st.header("Common Requirements")
 

## bring in live pay, state, and title graphs