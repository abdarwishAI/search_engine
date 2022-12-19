# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 20:48:10 2022

@author: ahmed.darwish
"""

import openai
import streamlit as st
import json
import pandas as pd


openai.api_key = "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"

def search (text):
    def chatGPT_openai (prompt):
        response = openai.Completion.create(
            engine = "text-davinci-002",
            prompt = prompt,
            temperature=0.4,
            max_tokens=64
            )
        return response

    output_model =  chatGPT_openai (text)
    json_string = json.dumps(output_model)
    json_dic = json.loads(json_string)
    
    for k, v in json_dic.items():
        if k == 'choices':
            output = v
    
    df = pd.DataFrame(output)
    txt2= df["text"][0]
    
    final_results = txt2[2:]
    return final_results


##### create a webUI

# hide burger menue
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)


st.title('ChatGPT Search_Darwish')
question = st.text_input("Write a sentence to search", value="")



if st.button('Search'):
    st.write(search(question))
else:
    st.write('write your question and click search')


st.write ("___________________________________________________________")
st.write ('Developed By: Ahmed B. Darwish')
st.write ("abdarwish.jp@gmail.com")
st.write ("")
st.write ("") 