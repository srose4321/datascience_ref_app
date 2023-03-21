import pandas as pd
import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import string

import ds_ref_data as data

st.title("Data Science Resources")
st.sidebar.subheader("Quick Links:")
links = st.sidebar.container()
with links:
    st.sidebar.write("Link to Pay Comparisons: [Payscale](https://www.payscale.com/research/US/Job=Data_Scientist/Salary)")
    st.sidebar.write("Link to Training Resources: [Learn DS Online](https://www.simplilearn.com/resources-to-learn-data-science-online-article)")
    st.sidebar.write("Link to Job Comparison: [Different DS Job Types](https://builtin.com/data-science/data-science-jobs)")
    
    
tab1, tab2, tab3 = st.tabs(["Overview", "Job Types", "Job Req Analysis"])
with tab1:
   st.subheader("Quick Overview of Data Science:")
   url = "https://www.youtube.com/embed/xvEKQefqQ7A"
   st.video(url)
   st.text("What is the roadmap to becoming a Data Scientist?")
   st.image("images/modern_ds.webp")
   st.image('images/ds_roadmap.png')
   st.markdown("""#### What is the difference between AI/ML/DS?
   Definitions: 

    - AI: François Chollet, creator of Keras, described it as “the effort to automate intellectual tasks normally performed by humans”.
    - ML: a pioneer of ML, Arthur Samuel, defined it as a “field of study that gives computers the ability to learn without being explicitly programmed”.
         -  Includes single layer NN
    - DL:  a subset of ML that is inspired by how human brains work
         -  Multi-layer NN, CNN, RNN

        """)
   st.image('images/venn1.jpg')
   st.image('images/diagram_2.png')
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
   st.image('images/ds_process_2.jpeg')
   st.image('images/data-prep-approach-time.png')
   

with tab2:
    st.subheader("Differences in DS Jobs")
    url2='https://youtu.be/VrdnBxx8BBI'
    st.video(url2)
    st.caption("For different types of jobs in Data Science, here are some skill focus separations. \
        Keep in mind that every company is different and can align their DS roles slightly differently. \
            This is meant as a guide, not a steadfast rule.")
    st.image("images/ds_skills_comparison.webp")
    st.caption("Within a role, there are ways you can distinguish yourself. Are you interested in focusing in one area\
        and becoming a subject matter expert? Are you very curious and want to explore lots of different areas and want \
            to become more of a generalist? While all of these are good options, it is helpful in interviews to know \
                yourself, so you can market your strengths")
    st.image("images/types_of_ds.jpg")

with tab3:
    st.subheader("Job Req Analysis")
    st.caption("The data used for this study is obtained by aggregated data from [ai-jobs.net](https://ai-jobs.net), under this [license](https://creativecommons.org/publicdomain/zero/1.0/).")

    ## WordCloud
    data_df = data.gather_salary_data()
    text =str(data_df["job_title"].values)
    clean_text = text.translate(str.maketrans('','',string.punctuation))

    wordcloud = WordCloud(width=480, height=480, margin=0).generate(clean_text)

    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.margins(x=0,y=0)

    st.caption("Word Frequencies of Job Titles in 2020-2022")
    st.pyplot(fig=plt, clear_figure=True)

    highest_2022 = (data_df[data_df.work_year == 2022].groupby(["job_title", "experience_level", "company_size", "company_location"]).max()['salary_in_usd'].reset_index()
                                        ).sort_values(["salary_in_usd"], ascending=False).head(10)

    st.caption("Top 2022 Job Titles by Salaries")
    fig = plt.barh(highest_2022['job_title'], 
            highest_2022["salary_in_usd"]
            )
    plt.xlabel("Salaries")
    st.pyplot(fig=plt, clear_figure=True)

    average_earn = data_df.groupby(["job_title"]).mean()["salary_in_usd"].reset_index().sort_values(["salary_in_usd"], ascending=False).head(10)
    average_earn["salary_in_usd"]  = average_earn["salary_in_usd"].round(decimals=2)

    st.caption("Average Earnings by Job Title")
    fig = plt.barh(average_earn['job_title'], 
            average_earn["salary_in_usd"]
            )
    plt.xlabel('Salaries')
    st.pyplot(fig=plt, clear_figure=True)

    xp_level = (data_df.groupby("experience_level").mean()["salary_in_usd"].reset_index()
                .sort_values("salary_in_usd", ascending=False)
            .round(decimals=2))

    st.caption("Average Earnings by Experience Level")

    fig = plt.barh(xp_level['experience_level'], 
        xp_level["salary_in_usd"]
        )
    plt.xlabel('Salaries')
    st.pyplot(fig=plt, clear_figure=True)

    org_size = (data_df.groupby("company_size")
                        .mean()['salary_in_usd']
                            .reset_index()
                        .sort_values("salary_in_usd", ascending=False)
                    .round(decimals=2))
    st.caption("Average Earnings by Company Size")

    fig = plt.barh(org_size['company_size'], 
        org_size["salary_in_usd"]
        )
    plt.xlabel('Salaries')
    st.pyplot(fig=plt, clear_figure=True)
## future idea: bring in live pay, state, and title graphs