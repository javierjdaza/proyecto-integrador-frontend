import streamlit as st 
import requests
import os
import json
from streamlit_option_menu import option_menu
import pandas as pd
st.set_page_config(page_title='Proyecto Integrador',page_icon=":brain:",initial_sidebar_state="collapsed")
import requests



st.markdown("<h1 style='text-align: center; color: #000000;'>Proyecto Integrador </h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #000000;'>Supervised vs Unsupervised Problem</h3>", unsafe_allow_html=True)
st.write('---')
menu_selection = option_menu(None, ["Prediccion", "The Team"], 
    icons=['robot', 'cup'], 
    menu_icon="cast", default_index=0, orientation="horizontal")
st.write('---')
st.write(' ')
st.write(' ')

if menu_selection == 'Prediccion':
    f1,f2 = st.columns(2,  vertical_alignment = 'center', gap = 'medium', border = True)
    f3,f4 = st.columns(2,  vertical_alignment = 'center', gap = 'medium', border = True)
    f5,f6 = st.columns(2, vertical_alignment = 'center', gap = 'medium', border = True)
    with f1:
        project_priority_slider = st.slider("🚨 Project Priority", min_value = 1, max_value = 4, value = 2, step=1)
    with f2:
        avg_risk_exposure_slider = st.slider("⚠️ Avg Risk Exposure", min_value = 0.0, max_value = 10.0, value = 2.5, step = 0.5, )
        
        
    with f3:
        total_headcount_slider = st.slider("👥 Total Headcount", min_value = 1, max_value = 30000, value = 50)
    with f4:
        num_tasks_slider = st.slider("📋 Num Tasks", min_value = 1, max_value = 1000, value = 100)
    
    with f5:
        duration_slider = st.slider("⏳ Duration", min_value = 1, max_value = 600, value = 30)
    with f6:
        predict_button = st.button('Prediccion',icon="🧠", use_container_width=True, type='tertiary')
        if predict_button:
            
            data = {
                'project_priority' : project_priority_slider,
                'avg_risk_exposure' : avg_risk_exposure_slider,
                'total_headcount' : total_headcount_slider,
                'num_tasks' : num_tasks_slider,
                'duration' : duration_slider,
            }
            r = requests.post('http://127.0.0.1:8000/predict', json= data)
            response = json.loads(r.content)
            st.text(f"Cluster Predicho: {response['y_predict']}")
            # st.text(f"{response['y_predict_proba']}")



    


def get_prediction():
    # r = requests.get(f'http://127.0.0.1:8000/melquiades/{promt}')
    # response = json.loads(r.text)

    return 'TODO'

def put_img(name,role, img_file_name):
    # st.image(f'./img/{img_file_name}.png', use_column_width=True)
    st.markdown(f"<h5 style='text-align: center; color: #000000;'>{name}<br>{role}</h5>", unsafe_allow_html=True)


if menu_selection == 'The Team':
    c1,c2,c3 = st.columns(3)

    with c1:
        put_img('Javier Daza', 'Descripcion', '')
    with c2:
        put_img('Maria Sofia Uribe', 'Descripcion', '')
    with c3:
        put_img('Pablo Jimeno', 'Descripcion', '')

