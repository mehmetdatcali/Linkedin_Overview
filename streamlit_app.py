import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

########################################################################################################################
st.set_page_config(page_title='LinkedIn Overview', layout='wide')
hide_st_style = '''
                <style>
                MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                '''
st.markdown(hide_st_style, unsafe_allow_html=True)

st.markdown('<p style="text-align: left; font-size: xx-large">'
            '<b>Linked</b>'
            '<b style=" color: #0077B5;">in</b>'
            '<b>Overview.</b>'
            '<span style="font-size: small;">'
            '<a href="https://linkedin.com/in/mehmetdatcali/" style="text-decoration: none; color: #ffffff;"><em> DEVELOPER: MEHMET DATÇALI</em></a>'
            '</span>'
            '</p>', unsafe_allow_html=True)

########################################################################################################################
dataframe = pd.read_csv('data/linkedin')
dataframe = dataframe.applymap(lambda x: x.title())

sector = pd.read_csv('data/sector')
sector = sector.applymap(lambda x: x.title())

skill = pd.read_csv('data/skill')
skill = skill.applymap(lambda x: x.title())

########################################################################################################################
first = st.columns([0.6, 0.4])
second = st.columns([0.4, 0.6])
third = st.columns([0.4, 0.3, 0.3])
fourth = st.columns([0.6, 0.4])
colors = ['#5f0f40', '#9a031e', '#fb8b24', '#e36414', '#0f4c5c', '#5f0f40', '#9a031e', '#fb8b24', '#e36414', '#0f4c5c']
########################################################################################################################
with first[0]:
    st.markdown('<br>' * 2, unsafe_allow_html=True)
    st.markdown('*<p style="text-align: left; font-size: x-large">'
                '<strong>'
                'MOST FREQUENTLY ADVERTISED POSITIONS'
                '</strong>'
                '</p>*', unsafe_allow_html=True)

    st.markdown('<p style="text-align: left; font-size: medium; color: gray", >'
                "On June 20, 2024, in LinkedIn searches, you can find over 1500 job postings related to data science. "
                "However, after filtering and organizing, it turns out that there are actually around 400 job postings "
                "truly related to data science. The analyses presented here are derived from filtering and organizing "
                "processes specific to job postings shared on LinkedIn, aimed at determining data science job "
                "opportunities in Turkiye. These data aim to facilitate job seekers' access to relevant job postings "
                "and help them benefit from the analyses."
                '<br><br>'
                "Focusing on the most sought-after roles in Turkiye's data science sector, this analysis identifies "
                "prominent positions advertised in job postings and assists newcomers in understanding which job "
                "roles are popular in the industry."
                '</p>', unsafe_allow_html=True)

with first[1]:
    total_job = len(dataframe)
    stats_job = dataframe['JOB'].value_counts()
    jobs = go.Figure(data=[go.Pie(labels=stats_job.index,
                                  values=stats_job.values,
                                  title=f'Job Listings: {total_job}',
                                  textinfo='label + percent',
                                  textposition='outside',
                                  showlegend=False,
                                  marker=dict(colors=colors),
                                  hole=0.8)])
    st.plotly_chart(jobs)

########################################################################################################################
with second[0]:
    stats_experience = dataframe['EXPERIENCE'].value_counts()
    experiences = go.Figure(data=[go.Pie(labels=stats_experience.index,
                                         values=stats_experience.values,
                                         textinfo='label + percent',
                                         textposition='outside',
                                         showlegend=False,
                                         marker=dict(colors=colors),
                                         hole=0.8)])
    st.plotly_chart(experiences)

with second[1]:
    st.markdown('<br>' * 3, unsafe_allow_html=True)
    st.markdown('*<p style="text-align: right; font-size: x-large">'
                '<strong>'
                'PREFERRED PROFESSIONAL EXPERIENCE'
                '</strong>'
                '</p>*', unsafe_allow_html=True)

    st.markdown('<p style="text-align: right; font-size: medium; color: gray">'
                'Through detailed analysis of job postings, the preferred and required levels of professional '
                'experience in Turkiye are depicted in the graph. This information serves as a guiding tool for '
                'newcomers planning their careers and for experienced professionals seeking to grasp '
                'industry-wide trends.'
                '</p>', unsafe_allow_html=True)

########################################################################################################################
with third[0]:
    st.markdown('<br>' * 3, unsafe_allow_html=True)
    st.markdown('*<p style="text-align: left; font-size: x-large">'
                '<strong>'
                'DOMINANT EMPLOYMENT FORMATS'
                '</strong>'
                '</p>*', unsafe_allow_html=True)

    st.markdown('<p style="text-align: left; font-size: medium; color: gray">'
                'Analysis of job postings on LinkedIn reveals the prevalent employment formats preferred in '
                'Turkiye. This chart provides valuable insights for candidates evaluating their career options '
                'and for seasoned professionals aiming to align with industry practices.'
                '</p>', unsafe_allow_html=True)

with third[1]:
    stats_employment = dataframe['EMPLOYMENT'].value_counts()
    employments = go.Figure(data=[go.Pie(labels=stats_employment.index,
                                    values=stats_employment.values,
                                    textinfo='label + percent',
                                    textposition='outside',
                                    showlegend=False,
                                    marker=dict(colors=colors),
                                    hole=0.8)])
    st.plotly_chart(employments)

with third[2]:
    stats_workplace = dataframe['WORKPLACE'].value_counts()
    workplaces = go.Figure(data=[go.Pie(labels=stats_workplace.index,
                                  values=stats_workplace.values,
                                  textinfo='label + percent',
                                  textposition='outside',
                                  showlegend=False,
                                  marker=dict(colors=colors),
                                  hole=0.8)])
    st.plotly_chart(workplaces)

########################################################################################################################
with fourth[0]:
    stats_skill = skill['SKILL'].value_counts().sort_values(ascending=True)[-20:]
    skill = px.bar(y=stats_skill.values,
                   x=stats_skill.index,
                   color_discrete_sequence=[colors[3]]
                   )

    skill.update_layout(xaxis_title=None, yaxis_title='Count of Job Postings')
    st.plotly_chart(skill)

with fourth[1]:
    st.markdown('<br>' * 6, unsafe_allow_html=True)
    st.markdown('*<p style="text-align: right; font-size: x-large">'
                '<strong>'
                'HIGHLY SOUGHT-AFTER CREDENTIALS'
                '</strong>'
                '</p>*', unsafe_allow_html=True)

    st.markdown('<p style="text-align: right; font-size: medium; color: gray">'
                "Detailed analysis of job postings identifies the key professional qualifications and skills "
                "highly sought by employers in Turkiye's data science sector. This information supports "
                "newcomers in career planning and empowers experienced professionals to maintain "
                "competitiveness in the evolving industry landscape."
                '</p>', unsafe_allow_html=True)

########################################################################################################################
stats_sector = sector['SECTOR'].value_counts()[0:25]
sectors = px.bar(y=stats_sector.values,
                 x=stats_sector.index,
                 color_discrete_sequence=[colors[1]],
                 title='TOP 25 SECTORS')

sectors.update_layout(xaxis_title=None, yaxis_title='Count of Job Postings')
st.plotly_chart(sectors)

stats_company = dataframe['COMPANY'].value_counts()[0:25]
companies = px.bar(y=stats_company.values,
                   x=stats_company.index,
                   color_discrete_sequence=[colors[1]],
                   title='TOP 25 COMPANIES')

companies.update_layout(xaxis_title=None, yaxis_title='Count of Job Postings')
st.plotly_chart(companies)
