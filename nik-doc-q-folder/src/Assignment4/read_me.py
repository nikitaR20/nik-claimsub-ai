'''

1.Download Mistral mistral-7b-instruct-v0.1-q4_k_m.gguf and store the file in an appropriate folder.
2. Install required packages from requirements.txt
3. Rename config_template.py file to config.py and modify parameters as follows:
MODEL_PATH = "" -Full Path of Mistral .gguf file
FAISS_INDEX_FILE = "faiss_index"
PDF_FILE_PATH = "./pdfs"
FILE_PATH = r"" -Folder path of .html files to be given as an input
PDF_FILE_PATH = r""folder where html files converted to pdfs will be stored"
EMBEDDINGS_FILE = r"embeddings.npy"
FAISS_INDEX_FILE = r"faiss_store"

3. Run main.py file
'''