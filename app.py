from cmath import phase
import json
from os import link
import requests
import pandas as pd
from flask import Flask,request,render_template

app = Flask(__name__)

df_basic_info = pd.read_excel('data.xlsx',sheet_name='Basic Info')
df_skills = pd.read_excel('data.xlsx',sheet_name='Skills')
df_experience = pd.read_excel('data.xlsx',sheet_name='Experience')
df_education = pd.read_excel('data.xlsx',sheet_name='Education')
df_projects = pd.read_excel('data.xlsx',sheet_name='Projects')

df_basic_info.fillna('',inplace=True)
name = df_basic_info[df_basic_info['Column']=='Name']['Value'].values[0]

@app.route('/')
def home():
    name = df_basic_info[df_basic_info['Column']=='Name']['Value'].values[0]
    designation = df_basic_info[df_basic_info['Column']=='Designation']['Value'].values[0]
    description = df_basic_info[df_basic_info['Column']=='Description']['Value'].values[0]
    photo = df_basic_info[df_basic_info['Column']=='Photo']['Value'].values[0]
    github = df_basic_info[df_basic_info['Column']=='GitHub Profile Link']['Value'].values[0]
    linkedin = df_basic_info[df_basic_info['Column']=='LinkedIn Profile Link']['Value'].values[0]
    instagram = df_basic_info[df_basic_info['Column']=='Instagram Profile Link']['Value'].values[0]
    email = df_basic_info[df_basic_info['Column']=='Email Id']['Value'].values[0]

    return render_template('home.html',name=name,designation=designation,description=description,photo=photo,
                            github=github,linkedin=linkedin,instagram=instagram,email=email)

@app.route('/skills')
def skills():
    df_skills.fillna('',inplace=True)
    d = {}
    for i in range(len(df_skills)):
        skill = df_skills.iloc[i]['Skill']
        image = df_skills.iloc[i]['Image']
        experience = df_skills.iloc[i]['Experience']
        d[skill]={}
        d[skill]['image']=image
        d[skill]['experience']=experience
        
    return render_template('skills.html',skillinfo=d,name=name)

@app.route('/education')
def education():
    df_education.fillna('',inplace=True)
    d = {}
    for i in range(len(df_education)):
        institute = df_education.iloc[i]['Institute']
        degree = df_education.iloc[i]['Degree']
        date = df_education.iloc[i]['Date']
        extrainfo = df_education.iloc[i]['Extra Info']
        image = df_education.iloc[i]['Image']
        d[institute]={}
        d[institute]['degree']=degree
        d[institute]['date']=date
        d[institute]['extrainfo']=extrainfo
        d[institute]['image']=image  
    return render_template('education.html',educationinfo=d,name=name)

@app.route('/experience')
def experience():
    df_experience.fillna('',inplace=True)
    d = {}
    for i in range(len(df_experience)):
        designation = df_experience.iloc[i]['Designation']
        company = df_experience.iloc[i]['Company']
        image = df_experience.iloc[i]['Image']
        date = df_experience.iloc[i]['Date']
        info = df_experience.iloc[i]['Info']
        d[company]={}
        d[company]['designation']=designation
        d[company]['image']=image
        d[company]['date']=date
        d[company]['info']=info
    return render_template('experience.html',experienceinfo=d,name=name)

@app.route('/projects')
def projects():
    df_projects.fillna('',inplace=True)
    d = {}
    for i in range(len(df_projects)):
        projectname = df_projects.iloc[i]['Project Name']
        description = df_projects.iloc[i]['Description']
        image = df_projects.iloc[i]['Image']
        date = df_projects.iloc[i]['Date']
        d[projectname]={}
        d[projectname]['image']=image
        d[projectname]['description']=description
        d[projectname]['date']=date
    return render_template('projects.html',projectinfo=d,name=name)

@app.route('/resume')
def resume():
    df_basic_info.fillna('',inplace=True)
    resumelink = df_basic_info[df_basic_info['Column']=='Resume Link']['Value'].values[0]
    return render_template('resume.html',resumelink=resumelink,name=name)


if __name__ == '__main__':
    app.run(debug=True)