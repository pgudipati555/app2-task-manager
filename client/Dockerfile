FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

# Install with trusted hosts to bypass SSL verification
RUN pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r requirements.txt

COPY . .

CMD ["python", "api_client.py"]