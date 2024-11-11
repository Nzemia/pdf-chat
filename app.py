import streamlit as st


def main():
    st.set_page_config(page_title="PDF Chat", page_icon=":books")
    
    
    st.header("PDF Chat")
    st.text_input("Ask me any question about your PDFs")

    with st.sidebar:
        st.subheader("Your documents")
        st.file_uploader("Upload your PDF")
        st.button("Upload")
        st.button("Clear")
    


if __name__ == "__main__":
    main()
