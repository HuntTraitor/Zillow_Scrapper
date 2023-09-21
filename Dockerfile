# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.10-slim

# Set env variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

EXPOSE 80

WORKDIR /app

# Install pip requirements
COPY ./requirements.txt /app
RUN python -m pip install -r requirements.txt

COPY . /app

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["python3", "app.py"]
