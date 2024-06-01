# Install Fine Tuned Model

https://drive.google.com/file/d/1gjnI1YwQyCf-jUUaFVu6DPcLpyigu-gO/view?usp=share_link


# Tree

Place the downloaded model from drive to the path ./models folder.
```
.
├── Audios
│   ├── langs.py
│   └── process.py
├── README.md
├── ai.py
├── api.py
├── app.py
├── models
│   ├── leave
│   │   ├── config.json
│   │   ├── generation_config.json
│   │   └── model.safetensors
│   └── leave.zip
├── requirements.txt
└── test.json
```

# Package Installation

```bash
pip install -r requirements.txt
```

# Running Server

```bash
uvicorn api:app --host 0.0.0.0 --port 8000
```

# Running App

```bash
streamlit run app.py
```

The POC app will be available on localhost