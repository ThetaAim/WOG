FROM python:3.8-slim-buster
WORKDIR /

# Copy necessary files
COPY ../Tools/Scores.txt .
COPY ../Tools/e2e.py .
COPY ../Tools/main_score.py .
COPY ../Tools/utils.py .

# Copy the templates directory
COPY ../Tools/templates /templates

# Install dependencies
RUN pip install Flask
RUN pip install selenium

# Expose the port
EXPOSE 5040

# Define the command to run your application
CMD ["python", "main_score.py"]
