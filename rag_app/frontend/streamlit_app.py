import streamlit as st
from main_controller import handle_upload, handle_query

def main():
    st.title("RAG Application")
    # action = st.sidebar.radio("Select Action", ["Upload Document", "Query LLM"])
    
    # if action == "Upload Document":
    st.header("Upload Document")
    uploaded_file = st.file_uploader("Choose a file", type=["pdf"])
    if uploaded_file is not None:
        if st.button("Upload"):
            try:
                result = handle_upload(uploaded_file)
                st.success(result.get("message", "Document uploaded successfully."))
            except Exception as e:
                st.error(f"Upload failed: {e}")
    # else: 
    query_text = st.text_input("Enter your query:")
    top_k = st.slider("Number of results", 1, 10, 5)
    if st.button("Submit Query"):
        if query_text:
            try:
                result = handle_query(query_text, top_k)
                if "answer" in result:
                    st.subheader("Generated Answer")
                    st.write(result["answer"])
                
                st.subheader("Retrieved Documents")
                docs = result.get("retrieved_documents", [])
                if docs:
                    for idx, doc in enumerate(docs, start=1):
                        st.write(f"**Document {idx}:**")
                        st.write(doc)
                else:
                    st.info("No documents retrieved.")
            except Exception as e:
                st.error(f"Query failed: {e}")
        else:
            st.warning("Please enter a query.")


if __name__ == "__main__":
    main()
