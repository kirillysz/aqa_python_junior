FROM python:3.12-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    tar \
    gzip \
    curl \
    ca-certificates \
    firefox-esr \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

RUN wget -q -O /tmp/geckodriver.tar.gz \
    "https://github.com/mozilla/geckodriver/releases/download/v0.34.0/geckodriver-v0.34.0-linux64.tar.gz" \
    && tar -xzf /tmp/geckodriver.tar.gz -C /tmp/ \
    && mv /tmp/geckodriver /usr/local/bin/ \
    && chmod +x /usr/local/bin/geckodriver \
    && geckodriver --version

RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app
RUN mkdir -p /allure-results

COPY . .

RUN uv sync

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh


ENTRYPOINT ["/entrypoint.sh"]