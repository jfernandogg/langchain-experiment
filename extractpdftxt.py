from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain_chroma import Chroma
import dotenv
import os

dotenv.load_dotenv()
chat = ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0.2)

# Ruta del directorio que deseas explorar
directorio = "../JFGG-Bootstrap-Templates/coassist/files"

# Obtener la lista de archivos en el directorio
archivos = os.listdir(directorio)

# Iterar sobre los archivos
pages = []
for archivo in archivos:
    # Combinar la ruta del directorio con el nombre del archivo
    ruta_completa = os.path.join(directorio, archivo)
    
    # Realizar alguna acción con el archivo (por ejemplo, cargarlo, procesarlo, etc.)
    # Aquí puedes adaptar tu código para trabajar con cada archivo
    print(f"Procesando archivo: {ruta_completa}")
    loader = PyPDFLoader(file_path)
    pages += loader.load_and_split()

vectorstore = Chroma.from_documents(documents=pages, embedding=OpenAIEmbeddings())
retriever = vectorstore.as_retriever(k=4)
docs = retriever.invoke("que seguros ofrece Coassist?")
print(docs)