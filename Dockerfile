FROM python:3

WORKDIR /opt

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# CMD [ "sleep", "infinity" ]
# CMD [ "python", "./your-daemon-or-script.py" ]