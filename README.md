# YouTube and WebPage Summarizer

A Streamlit app that uses LangChain and LLMs (Groq or Ollama) to summarize YouTube videos and web pages. Summaries are provided in markdown and can be downloaded as PDFs.

## Features

- Summarize YouTube videos (via transcript extraction)
- Summarize web pages (via content extraction)
- Choose between Groq and Ollama LLM providers
- Markdown output for summaries
- Download summaries as PDF
- Simple Streamlit UI

## Project Structure

```
YouTube_and_WebPage_Summarizer/
├── README.md
├── requirements.txt
├── logger/
│   └── logging.py
├── src/
│   ├── config/
│   │   ├── config.py
│   │   ├── config.ini
│   │   ├── model.py
│   │   └── prompt/
│   │       └── prompt_summarize.py
│   ├── ui/
│   │   ├── app.py
│   │   └── sidebar.py
```

## Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/YouTube_and_WebPage_Summarizer.git
    cd YouTube_and_WebPage_Summarizer
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Install [wkhtmltopdf](https://wkhtmltopdf.org/downloads.html):**
    - Download and install for your OS.
    - Update the path in `src/ui/app.py` if needed.

4. **Run the app:**
    ```bash
    streamlit run src/ui/app.py
    ```

## Usage

- Select your LLM provider and enter your API key.
- Enter a YouTube or web page URL.
- View the summary and download it as a PDF.

## Notes

- API keys for Groq or Ollama are required.
- For PDF export, ensure `wkhtmltopdf` is installed and the path is set correctly in the code.
- This project is for educational and research purposes.

---

**Enjoy summarizing content with AI!**