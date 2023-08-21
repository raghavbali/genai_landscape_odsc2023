import io
import streamlit as st

from utils import (
    sidebar,
    content_generator,
    text2image
)

from constants import (
    SYSTEM_MESSAGE_1, 
    SYSTEM_MESSAGE_2
    )

## Setup Page Header and Sidebar
st.set_page_config(page_title="SocialScribe:GenAI Powered Sidekick", page_icon="📝🤖", layout="wide")
st.header("SocialScribe📝🤖")
sidebar()


## Get User Input
with st.form(key="content"):
    txt = st.text_area("Enter Content for Your Post")
    submit = st.form_submit_button("Submit")

if submit:
    # get content for social media
    st.markdown("""### Social Media Content""")
    st.write('\n', content_generator(SYSTEM_MESSAGE_1,txt))
    st.markdown("""---""")

    # get content for text2img prompt
    st.markdown("""### Text2Image Prompt""")
    prompt = content_generator(SYSTEM_MESSAGE_2,txt,temperature=0)
    st.write('\n', prompt)

    # display the image
    st.markdown("""### Generated Image""")
    image = io.BytesIO(text2image(prompt))
    st.image(image, caption=prompt[:20]+"...")
    st.balloons()

