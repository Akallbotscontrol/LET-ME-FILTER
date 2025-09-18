FROM python:3.11-slim

# Install system dependencies: git, OpenSSL, CA certificates, tzdata
RUN apt update && apt upgrade -y && \
    apt install -y --no-install-recommends git openssl ca-certificates tzdata && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /Codeflix_Bots

COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade pip --root-user-action=ignore && \
    pip install --no-cache-dir -r requirements.txt --root-user-action=ignore

COPY . .

# Non-root user for security (Render friendly)
RUN useradd -m botuser
USER botuser

# Start the bot
CMD ["python3", "bot.py"]


## vps deploy commands 

# mkdir Deendayal_botz
# cd Deendayal_botz
# python3 -m venv venv
# source venv/bin/activate
# git clone https://github.com/Deendayal403/Deendayal_dhakad.git
# cd Deendayal_dhakad
# pip install -r requirements.txt
# python3 bot.py
