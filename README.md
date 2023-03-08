# Streamlit - Google Authenticator
This project was created by [datahungry.dev](https://www.facebook.com/datahungry)

## Pre-requirement
```bash
pip install -r requirements.txt
```

## Let's run it
```bash
streamlit run streamlit_app.py
```

## Run with Docker

```bash
docker build -t streamlit-gauth .
docker run -p 8501:8501 --name="streamlit-gauth" -d streamlit-gauth
```