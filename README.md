# Package Installation

```bash
pip install -r requirements.txt
```

# Install Fine Tuned Model

```bash
python setup_model.py
```

Once you run this command the fine tuned model will automatically saved in models/leave

# Tree

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

# Running Server

```bash
uvicorn api:app --host 0.0.0.0 --port 8000
```

# Running App

```bash
streamlit run app.py
```

The POC app will be available on localhost


# Test AI Server

###  /leave - parameter (querry) 
querry = 'YOUR QUERRY'


```bash
curl --location --request POST 'http://127.0.0.1:8000/leave?querry=i%20want%20to%20take%20leave%20because%20i%20am%20going%20trip'
```
Response
```json
{
    "response": "Context: i want to take leave because i am going trip|\nLeave: yes\nCategory: vacation\nStatus: requesting"
}
```
---
###  /leave/common - parameter (querry) 
querry = 'YOUR QUERRY' \
This method can able translate understand any language and communicate with trained model.

```bash
curl --location --request POST 'http://127.0.0.1:8000/leave/common?querry=%E0%AE%8E%E0%AE%A9%E0%AE%95%E0%AF%8D%E0%AE%95%E0%AF%81%20%E0%AE%A8%E0%AE%BE%E0%AE%B3%E0%AF%88%20%E0%AE%B2%E0%AF%80%E0%AE%B5%E0%AF%81%20%E0%AE%B5%E0%AF%87%E0%AE%A3%E0%AF%8D%E0%AE%9F%E0%AF%81%E0%AE%AE%E0%AF%8D%0A'
```
the data sent here is '**எனக்கு நாளை லீவு வேண்டும்**' and the 
Response is
```json
{
    "response": "Context: I want to leave tomorrow|\nLeave: yes\nCategory: none\nStatus: requesting"
}
```

---