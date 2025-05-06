# Automate App Writing

A tool to automatically generate tailored resumes and cover letters based on job descriptions.

## Overview

This project helps you quickly customize your resume and cover letter for multiple job applications. It analyzes job descriptions and suggests targeted modifications to make your application more relevant.

## Features

- Process multiple job descriptions at once (up to 100)
- Generate tailored resumes and cover letters for each job
- Extract company name and job title from descriptions
- Find relevant keywords to highlight in your application
- Optional AI-assisted tailoring with OpenAI

## Setup

1. **Install dependencies**

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

2. **Set up your input files**

- Put your resume template in `input/resumes/` (supports .docx, .pdf, .txt)
- Put your cover letter template in `input/cover_letters/` (supports .docx, .txt)
- Add job descriptions in `input/job_descriptions/` (as .txt files)

3. **Template format**

In your cover letter template, you can use placeholders that will be automatically replaced:
- `[COMPANY_NAME]` - Will be replaced with the company name
- `[POSITION_TITLE]` - Will be replaced with the job title

4. **Optional: Set up OpenAI integration**

For AI-powered tailoring suggestions, set your OpenAI API key:

```bash
# On Windows
set OPENAI_API_KEY=your-api-key-here

# On Linux/Mac
export OPENAI_API_KEY=your-api-key-here
```

## Usage

**Process all jobs at once:**

```bash
python tailor_documents.py
```

**Process a specific job:**

```bash
python tailor_documents.py --job "software-engineer-acme"
```

**Use a configuration file:**

```bash
python tailor_documents.py --config my_config.json
```

## Output

Tailored documents will be saved in the `output/` directory, organized by job name:

```
output/
├── job1/
│   ├── Resume_CompanyName_job1.docx
│   └── CoverLetter_CompanyName_job1.docx
└── job2/
    ├── Resume_CompanyName_job2.docx
    └── CoverLetter_CompanyName_job2.docx
```

## Example Templates

- Check the `examples/` directory for sample resume and cover letter templates
- Place your own templates in the `input/` directories

## Notes

- For best results, format your resume and cover letter with clear sections
- Job descriptions should be plain text (.txt) files
- Company names and job titles are automatically extracted, but may need verification 