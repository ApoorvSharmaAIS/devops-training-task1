# Using python lightweight image
FROM python:3.11-slim

# set up working directory
WORKDIR /app

# copy files

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Expose port and run
EXPOSE 8000
CMD [ "python" , "app.py" ]
