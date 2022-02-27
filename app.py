import streamlit as st
import numpy as np
from PIL import Image, ImageOps
import base64
from dateutil.relativedelta import relativedelta
import datetime
import pandas as pd  

st.balloons()
# option = st.sidebar.radio("Menu",['Home', 'About','Contributors'])
st.sidebar.markdown('<h1 style="margin-left:8%; color:	#FF9933 ">Menu </h1>',
                    unsafe_allow_html=True)
option = st.sidebar.radio(" ",("Home", "About", "Features", "Select AOI Data Parameters", "Visualizations", "Conclusion", "Team"))


if option == 'Home':
    col1,col2,col3 = st.columns([50,100,1])
    
    # col2.image('chapter_logo.png')
    st.markdown(
        """
        <style>
        .container1 {
        display: flex;
    }
    .logo-img1 {
            float:right;
            width:350px;
            height:350px;
            margin: 0px 0px 0px 170px;
    }
    </style>
    """,
    unsafe_allow_html=True
    )
    st.markdown(
        """
        <style>
        .container2 {
        display: flex;
    }
    .img {
            float:right;
            width:300px;
            height:350px;
            margin: 0px 0px 0px 200px;
    }
    </style>
    """,
    unsafe_allow_html=True
    )
    st.markdown(
        f"""
        <div class="container1">
            <img class="logo-img1" src="data:image/png;base64,{base64.b64encode(open('chapter_logo.png', "rb").read()).decode()}">
        </div>
        """,
        unsafe_allow_html=True
    )
    # st.title('Omdena - Hamburg, Germany Chapter')
    st.markdown("<h1 style='text-align: center; color: white;'>Omdena - Hamburg, Germany Chapter</h1>", unsafe_allow_html=True)
    # st.header('Feasibility and ROI Analysis for Renewable Resources Infrastructure using Computer Vision')
    st.text("")
    st.text("")
    st.text("")
    html_temp = """
    <div style="background-color:blue;padding:10px">
    <h2 style="color:white;text-align:center;">Feasibility and ROI Analysis for Renewable Resources Infrastructure using Computer Vision</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    st.text("")
    


        
    ana_type = st.sidebar.selectbox(
        "To know more about the parameters used in this project ",
        ("Select a parameter","Global Horizontal Irradiance","Global Tilted Irradiation/Irradiance","Temperature","Diffused Solar Radiation"))
        
    if ana_type == 'Global Horizontal Irradiance':
        # image1 = Image.open('Parameters/plastic.jpeg')
        # st.sidebar.image(image1, caption='Global Horizontal Irradiance')
        st.sidebar.write("Give description for Global Horizontal Irradiance")
    
    elif ana_type =='Global Tilted Irradiation/Irradiance':
        # image2 = Image.open('Parameters/glass.jpeg')
        # st.sidebar.image(image2, caption='Global Tilted Irradiation/Irradiance')
        st.sidebar.write("Give description for Global Tilted Irradiation/Irradiance")
        
    elif ana_type =='Temperature':
        # image3 = Image.open('Parameters/cardboard.jpeg')
        # st.sidebar.image(image3, caption='Temperature')
        st.sidebar.write("Give description for Temperature")
        
    elif ana_type =='Diffused Solar Radiation':
        # image4 = Image.open('Parameters/paper.jpeg')
        # st.sidebar.image(image4, caption='Diffused Solar Radiation')
        st.sidebar.write("Give description for Diffused Solar Radiation")
    
      
     
         



elif option == 'About':
  html_temp = """
        <div style="background-color:blue;padding:10px">
        <h2 style="color:white;text-align:center;">Model Description</h2>
        </div>
        """
  st.markdown(html_temp,unsafe_allow_html=True)
  st.text("")
  st.text("")
  st.subheader("Model Name Description: ")
  st.markdown('model',unsafe_allow_html=True)
  

elif option == "Features":
  html_temp = """
        <div style="background-color:blue;padding:10px">
        <h2 style="color:white;text-align:center;">Project Description</h2>
        </div>
        """
  st.markdown(html_temp,unsafe_allow_html=True)
  st.text("")
  st.text("")
  st.markdown('write description',unsafe_allow_html=True)
  

elif option == 'Select AOI Data Parameters':

   
    
    st.subheader('SELECT FOR AOI DATA PARAMETERS')    
    
    col1, col2 = st.columns(2)

    

    area = st.text_input('Type Area Of Interest', 'Hamburg')

    
    
    prm_type = col1.selectbox(
        "Data Visualization Parameters",
        ("Global Horizontal Irradiance","Global Tilted Irradiation/Irradiance","Temperature","Diffused Solar Radiation")
    )

    long = st.number_input('Longitude',min_value=72.6026 , format="%.4f")

    lat = st.number_input('Latitude', min_value =23.0063 ,format="%.4f")
    
    col3,_ = st.columns((1,2)) # To make it narrower
    
    format = 'MMM DD, YYYY'  # format output
        
    start1 = datetime.date(year=2020,month=1,day=1)-relativedelta(years=1) #  I need some range in the past

    start2 = datetime.date(year=2021,month=11,day=1)
    st.text("")
    st.text("")
    
    
    st.text("")
    st.text("")

    
    st.text("")
    st.text("")
    
    max_days = start2-start1
        
    slider1 = col3.slider('Select Start Date', min_value=start1, value=start2 ,max_value=start2, format=format)
        
    st.table(pd.DataFrame([[start1, slider1,start2]],
                      columns=['start1',
                               'start_selected',
                               'start2'],
                      index=['date']))

    end1 = datetime.date(year=2020,month=1,day=15)-relativedelta(years=1) #  I need some range in the past
    
    end2 = datetime.date(year=2021,month=12,day=31)
    
    max_days = end2-end1
        
    slider2 = col3.slider('Select End Date', min_value=end1, value=end2, max_value=end2, format=format)
        
    st.table(pd.DataFrame([[end1, slider2, end2]],
                      columns=['end1',
                               'end_selected',
                               'end2'],
                      index=['date']))
    
    

    
    if st.button('Submit'):
        
        st.write("Submitted")



elif option == 'Visualizations':
    
    st.subheader('PROJECT VISUALIZATIONS')
    
   
    
elif option == 'Conclusion':

    st.subheader('TECH STACK')

    

    st.subheader('PROJECT SUMMARY')

    


elif option == 'Team':
      rebecca_IMAGE = "Contributors/navneet.jpeg"
      html_temp = """
            <div style="background-color:blue;padding:10px">
            <h2 style="color:white;text-align:center;">Team</h2>
            </div>
            """
      st.markdown(
          """
          <style>
          .container {
          display: flex;
        }
        .navneet-img {
             float:right;
             width:170px;
             height:180px;
             margin: 0px 0px 0px 28px;
        }
        
        </style>
        """,
        unsafe_allow_html=True
      )
      st.markdown(html_temp,unsafe_allow_html=True)
      st.subheader("Project Manager/Chapter Lead")
      st.write("• &nbsp;  &nbsp;    [Navneet Singh Arora](https://www.linkedin.com/in/navneet-singh-arora/)")
      st.markdown(
            f"""
            <div class="container">
                  <img class="rebecca-img" src="data:image/png;base64,{base64.b64encode(open(rebecca_IMAGE, "rb").read()).decode()}">
            </div>
            """,
            unsafe_allow_html=True
      )
      st.subheader("Contributors")
      