import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter


def get_pdf_text(pdf_docs):
    # get the pdf text
    text = ""
    for pdf in pdf_docs:
        pdf_reader  = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()            
    return text

def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
    )
    chunks = text_splitter.split_text(text)
    return chunks



def main():
    load_dotenv()
    st.set_page_config(page_title="PDF Chat", page_icon=":books:")
    
    
    st.header("PDF Chat")
    st.text_input("Ask me any question about your PDFs")

    with st.sidebar:
        st.subheader("Your documents")
        pdf_docs = st.file_uploader("Upload your PDFs", accept_multiple_files=True)

        if st.button("Process"):
            with st.spinner("Processing..."):
                # get the pdf text
                raw_text = get_pdf_text(pdf_docs)
                # st.write(raw_text)


                # get the text chunks
                text_chunks = get_text_chunks(raw_text)
                st.write(text_chunks)

                # create vector store


        # st.button("Clear")
    


if __name__ == "__main__":    
    main()


