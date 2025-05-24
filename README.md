# mle-setup-render
deploy a simple app on render in this structure


app/
├── __init__.py
├── main.py
├── api/
│   ├── __init__.py
│   ├── sentiment.py
│   └── summarize.py
├── schemas/
│   ├── __init__.py
│   ├── sentiment.py
│   └── summarize.py
├── services/
│   ├── __init__.py
│   ├── model.py
│   └── summarizer.py
├── Dockerfile
├── requirements.txt
├── .github/
│   └── workflows/
│       └── ci.yml        # CI/CD pipeline
└── README.md


![CI](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME/actions/workflows/ci.yml/badge.svg)
