FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
