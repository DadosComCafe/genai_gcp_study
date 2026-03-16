FROM python:3.12-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ENV UV_PROJECT_ENVIRONMENT=/app/.venv

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen --no-cache

COPY . .


#CMD ["/app/.venv/bin/fastapi", "run", "app/main.py", "--port", "3000"]
#CMD ["/app/.venv/bin/fastapi", "run", "main.py", "--port", "3000"]
CMD ["/app/.venv/bin/fastapi", "run", "main.py", "--port", "3000", "--host", "0.0.0.0"]