import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

def prompt():
    return """Summarize the provided content: "{text}", thoroughly, covering all key details.
            Additionally, offer relevant context about the main topics discussed.
            Ensure the summary is clear, concise, and informative.
            *The Output should be in markdown format*"""
    # return {'role':'system',
    #         'content':"""Summarize the provided content: "{text}", thoroughly, covering all key details.
    #          Additionally, offer relevant context about the main topics discussed.
    #          Ensure the summary is clear, concise, and informative.
    #          *The Output should be in markdown format*"""}