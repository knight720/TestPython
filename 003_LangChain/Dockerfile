FROM python

# Define build arguments
ARG OPENAI_API_KEY=""

# Set environment variables from build arguments
ENV OPENAI_API_KEY=$OPENAI_API_KEY
ENV PATH="/root/.local/bin:${PATH}"

WORKDIR /app

RUN curl -sSL https://install.python-poetry.org | python3 - 

# Install LangChain and common dependencies
RUN pip install -qU "langchain[openai]"