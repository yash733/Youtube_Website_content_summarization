import streamlit as st
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from sidebar import sidebar

import validators
import langchain
from langchain.prompts import PromptTemplate, ChatMessagePromptTemplate
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import YoutubeLoader, UnstructuredURLLoader
from config.prompt.prompt_summarize import prompt

import markdown
import pdfkit
import tempfile
import io


st.set_page_config(page_title= 'Langchain: Content Summarizer', page_icon="🐉")

st.title("🐉 Langchain: Content Summarizer")

if 'user_selection' not in st.session_state:
    st.session_state.user_selection = {}
if 'config_saved' not in st.session_state:
    st.session_state.config_saved = False

if not st.session_state.user_selection.get('llm_model'):
    sidebar()
if st.session_state.config_saved:
    with st.sidebar:
        st.markdown("### Selected Configuration")
        st.write(f"**Model**: {st.session_state.user_selection['model']}")
        st.write(f"**Model Type**: {st.session_state.user_selection['model_name']}")

        if st.button('Reset Config'):
            st.session_state.config_saved = False
            st.session_state.user_selection = {}
            st.rerun()

# prompt_ = PromptTemplate(template=prompt(), input_variables=['text'])

# prompt_template="""
# Provide a summary of the following content in 300 words:
# Content:{text}

# """
prompt_=PromptTemplate(template=prompt(),input_variables=["text"])
# prompt_ = ChatMessagePromptTemplate.from_template(prompt())

if st.session_state.user_selection.get('llm_model'):
    model = st.session_state.user_selection['llm_model']
    
    st.subheader("Please provide URL to summarize your desired content")
    url = st.text_input(label="sdf", label_visibility='collapsed')

    if st.button("Next",key='Url_added') and url:
        if not validators.url(url):
            st.error("Please enter a valid Url. It can may be a YT video utl or website url")
        else:
            try:
                with st.spinner('Processing...'):
                    if 'youtube.com' in url:
                        loader = YoutubeLoader.from_youtube_url(url, add_video_info=True)
                    else:
                        loader = UnstructuredURLLoader(urls=[url],
                                                       headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"})
                    data = loader.load()

                    chain=load_summarize_chain(llm = model,chain_type="stuff",prompt=prompt_)
                    output_summary=chain.invoke({"input_documents":data}) # wont accept any other key input format
                    st.session_state.user_selection['html_'] = markdown.markdown(output_summary['output_text'])
            except Exception as e:
                st.error(f"Error found: {e}")

if st.session_state.user_selection.get('html_'):
    output_summary = st.text_area(label="Output:", value=st.session_state.user_selection['html_'], height=500)
    file_name = st.text_input(label="Setup File Name")
    if file_name:
        with tempfile.NamedTemporaryFile(delete=True, suffix=".pdf") as temp_pdf:
            config = pdfkit.configuration(wkhtmltopdf=r'Y:\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')  # <-- update this path

            pdfkit.from_string(st.session_state.user_selection.get('html_'), temp_pdf.name, configuration=config)
            temp_pdf.seek(0)
            pdf_bytes = temp_pdf.read()
        
        st.download_button(
            label = " Download Merged PDF",
            data = pdf_bytes,
            file_name= file_name+".pdf" if file_name else "summary.pdf",
            type = "primary",
            icon="📥"
        )
    else:
        st.stop()
        