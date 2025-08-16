import importlib.metadata
packages = [
    "langchain",
    "python-dotenv",
    "ipykernel",
    "langchain-community",
    "pypdf",
    "bs4",
    "arxiv",
    "pymupdf",
    "wikipedia",
    "langchain-text-splitters",
    "langchain-openai",
    "chromadb",
    "sentence_transformers",
    "langchain_huggingface",
    "faiss-cpu",
    "langchain_chroma",
    "duckdb",
    "pandas",
    "openai",
    "langchain-groq",
    "duckduckgo_search",
    "mysql-connector-python",
    "SQLAlchemy",
    "validators",
    "youtube_transcript_api",
    "unstructured",
    "pytube",
    "numexpr",
    "huggingface_hub",
    "langchain-ollama",
    "google-generativeai",
    "langchain_google_genai",
    "openpyxl",
    "langgraph",
    "langgraph-cli",
    "langchain-experimental",
    "structlog",
    "PyMuPDF",
    "pydantic",
    "pytest",
    "streamlit",
    "docx2txt",
    "fastapi" ,
    "uvicorn",
    "python-multipart"
]
for pkg in packages:
    try:
        version = importlib.metadata.version(pkg)
        print(f"{pkg}=={version}")
    except importlib.metadata.PackageNotFoundError:
        print(f"{pkg} (not installed)")

# # serve static & templates
# app.mount("/static", StaticFiles(directory="../static"), name="static")
# templates = Jinja2Templates(directory="../templates")