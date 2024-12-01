
README for POC Algorithm Documentation Generator

---

Overview
This repository provides an automated solution for generating structured LaTeX documentation for Python algorithms using OpenAI's GPT-4 model. It simplifies the process of creating algorithm overviews, variable definitions, mathematical formulas, example plots, and Python code listings in a professional LaTeX format.

---

Features
- Converts Python algorithms into structured LaTeX documentation.
- Automatically generates LaTeX sections for introductions, variable descriptions, and formulas.
- Creates example subsections with plots and example calculations.
- Supports modular document assembly using pylatex.
- Outputs a polished PDF document with chapters for each algorithm.

---

Requirements
- Docker: To containerize the environment.
- Poetry: For dependency management.
- API Key: OpenAI GPT API key stored in a .env file.

---

Setup

1. Clone the Repository
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. Install Dependencies
   - Ensure Docker is installed and running.
   - Use Poetry to install project dependencies:
     ```bash
     poetry install
     ```

3. Set Up .env File
   Create a .env file in the root of the project and add your OpenAI API key:
   ```
   OPENAI_KEY=<your_openai_api_key>
   ```

4. Build Docker Container
   Build the Docker image for the project:
   ```bash
   docker build -t algo-doc-gen .
   ```

---

Usage

1. Run the Application
   Use Docker to execute the container:
   ```bash
   docker run -v $(pwd):/app -w /app algo-doc-gen
   ```

2. Generate LaTeX Documentation
   Place your Python algorithm files in the python_code/ directory. The system will:
   - Process each .py file.
   - Generate LaTeX .tex files for documentation and examples.
   - Include plots and code listings in the final LaTeX document.

3. Compile to PDF
   The generated LaTeX files are combined into a single .tex document and compiled into a PDF:
   ```bash
   pdflatex programmatic_report.tex
   ```

---

Repository Structure
- python_code/: Contains Python algorithm files.
- algo_docs/: Stores generated LaTeX documentation files.
- examples/: Contains example inputs for algorithms.
- plots/: Stores generated example plots.
- .env: Stores the OpenAI API key.
- Dockerfile: Configures the containerized environment.
- programmatic_report.tex: The final compiled LaTeX document.

---

Key Scripts
1. ask_chat_gpt(prompt)
   Communicates with the OpenAI API to generate content based on provided prompts.

2. make_algo_doc_gpt_promt(name)
   Creates a prompt for GPT to generate the main LaTeX documentation for an algorithm.

3. make_algo_example_gpt_promt(name)
   Creates a prompt for GPT to generate example content for an algorithm.

4. make_algo_doc(name)
   Generates .tex files for the algorithm documentation.

5. make_algo_example(name)
   Generates .tex files for example sections with plots and calculations.

6. pylatex Integration
   Assembles the .tex files into a full LaTeX document, adds metadata, and integrates plots and code listings.


For questions or contributions, feel free to open an issue or submit a pull request.