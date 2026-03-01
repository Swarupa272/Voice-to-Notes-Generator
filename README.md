# MyProject

This repository contains a full‑stack application with a **Python/FASTAPI backend** and a **simple frontend**. The project focuses on lecture transcription, summarization, and note generation using ASR and embedding pipelines.

## Repository Structure

```
MyProject/
├── README.md               # Project documentation
├── requirements.txt        # Python dependencies
├── app/                    # Utility scripts for ASR, embeddings, pipeline, summarizer
├── backend/                # FastAPI application
│   ├── app/                # Python modules for backend
│   │   ├── config.py       # Configuration settings
│   │   ├── db.py           # Database connection helpers
│   │   ├── main.py         # FastAPI application entry point
│   │   ├── models.py       # ORM models
│   │   ├── schemas.py      # Pydantic schemas
│   │   ├── routers/        # Route definitions (e.g. lectures)
│   │   ├── services/       # Business logic (transcription, notes, export)
│   │   └── utils/          # Utility functions (logging, etc.)
│   └── __init__.py
├── frontend/               # Static frontend files (HTML/JS/CSS)
└── .venv/                  # Python virtual environment (not checked in)
```

## Getting Started

### Prerequisites

- Python 3.11+ (create a virtual environment)
- `pip` for installing dependencies
- Optional: `node` and `npm` if the frontend evolves into a SPA

### Installation

```powershell
cd C:\Users\swaru_gs76lcx\Desktop\MyProject
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Running the Backend

```powershell
cd backend
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`.  Swagger UI can be accessed at `http://localhost:8000/docs`.

### Using the Frontend

Open `frontend/index.html` in a browser. It interacts with the backend API for uploading lectures, fetching transcripts, and generating summaries.

## Development

- Update Python modules under `backend/app` and corresponding tests if added.
- Use `uvicorn` with `--reload` during development to auto‑restart the server.
- Add dependencies to `requirements.txt` and update `.venv` accordingly.

## Contributing

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes and push to your fork.
4. Submit a pull request describing your changes.

## License

Specify your license here.
