FROM python:3.12-slim

WORKDIR /workspace

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen --no-install-project

COPY . .

EXPOSE 10000

CMD ["uv", "run", "streamlit", "run", "app/ui.py", "--server.port", "10000", "--server.address", "0.0.0.0"]