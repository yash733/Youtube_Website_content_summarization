FROM python:3.9

WORKDIR /Youtube_Website_content_summarization

COPY . /Youtube_Website_content_summarization

RUN pip install -r requirements

EXPOSE 8501

CMD ["streamlit","run","/src/ui/app.py"]
