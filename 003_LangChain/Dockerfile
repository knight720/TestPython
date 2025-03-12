FROM python

# Define build arguments
ARG OPENAI_API_KEY=""

# Set environment variables from build arguments
ENV OPENAI_API_KEY=$OPENAI_API_KEY

# Install LangChain and common dependencies
RUN pip install -qU "langchain[openai]"