FROM ghcr.io/astral-sh/uv:python3.14-trixie
WORKDIR /prj
COPY . /prj
RUN uv sync --locked
EXPOSE 8080
CMD ["uv", "run", "python", "weatherapp/manage.py", "runserver", "0.0.0.0:8000"]



