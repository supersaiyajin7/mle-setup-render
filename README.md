# mle-setup-render
deploy a simple app on render in this structure


llm-sentiment-api/
├── app/
│   ├── main.py           # FastAPI app instance
│   ├── api.py            # API routes
│   ├── schemas.py        # Pydantic models
│   ├── model.py          # LLM model logic
│  
├── tests/
│   ├── test_api.py
│   └── test_model.py
├── Dockerfile
├── requirements.txt
├── .github/
│   └── workflows/
│       └── ci.yml        # CI/CD pipeline
└── README.md

