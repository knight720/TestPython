FROM python

# Define build arguments

# Set environment variables from build arguments
ENV PATH="/root/.local/bin:${PATH}"

WORKDIR /app

RUN curl -sSL https://install.python-poetry.org | python3 - 

# Install LangChain and common dependencies
RUN pip install -qU "langchain[openai]"
RUN poetry config virtualenvs.in-project true