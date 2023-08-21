import os
import openai
import requests
from retry import retry
import streamlit as st

from constants import (
    OPENAI_API_KEY, 
    OPENAI_ORG_KEY, 
    HF_API_URL, 
    HF_HEADER
)

os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY
openai.organization = OPENAI_ORG_KEY
openai.api_key = os.getenv("OPENAI_API_KEY")

def sidebar():
    """
      Utility to add content to sidebar
    """
    with st.sidebar:

        st.markdown("---")
        st.markdown("# About")
        st.markdown(
            "📝🤖SocialScribe: GenAI Powered Sidekick"
        )
        st.markdown(
            """
            Your personal social media manager to help you create amazing posts tailored to your preferences.
            What's more, it generates a new image customised for your content. Give it a spin!!!
            """
        )
        st.markdown("Made by [raghav bali](https://twitter.com/rghv_bali)")
        st.markdown("---")

def get_completion_from_messages(messages, 
                                 model="gpt-3.5", 
                                 temperature=0, max_tokens=500):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, 
        max_tokens=max_tokens, 
    )
    return response.choices[0].message["content"]

def content_generator(sys_message,user_message,model='gpt-3.5-turbo',temperature=0):
    messages =  [  
    {'role':'system',
     'content': sys_message},
    {'role':'user',
     'content': user_message}
    ]
    return get_completion_from_messages(messages=messages,model=model,temperature=temperature)


def text2image(prompt="Dummy Dog"):

    response = requests.post(HF_API_URL, headers=HF_HEADER, json={"inputs":prompt})
    return response.content