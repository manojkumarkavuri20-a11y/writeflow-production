## Blueprint: WriteFlow

## Why this exists

WriteFlow was built to remove the most repetitive part of a job search: writing a fresh, correctly personalized cover letter for every application. Rather than reaching for a heavyweight framework or an external AI service, it solves the problem with the smallest tool that actually works: a single Python script that fills in a template with a candidate profile and the details of the specific role being applied for.

## How it works

The profile data (name, contact details, education, key achievements, availability and right-to-work status) lives in a DEFAULT_PROFILE dictionary at the top of writeflow.py, so the whole tool is personalized simply by editing those values. generate_cover_letter combines that profile with a job title and company name, using Python's string.Template to substitute the placeholders into a fixed cover letter template; if no custom paragraph is supplied, a default sentence referencing the company is generated automatically. save_cover_letter writes the result to a timestamped .txt file in an output directory, and log_application appends a record of the job title, company, date and output path to a local applications.json file, which functions as a lightweight application tracker over time.

## Command-line interface

The script is invoked directly with argparse-defined flags: --job and --company are required, --custom accepts an optional bespoke paragraph, and --output lets the save location be changed. Running it prints the generated letter to the terminal, then saves and logs it in the same run, so a single command produces both the document and the tracking entry.

## Honest framing

WriteFlow deliberately does not use an AI API. The templating approach was chosen because it is fast, has no external dependency or cost, and produces a predictable, professional result every time, at the cost of every letter sharing the same underlying structure. The README documents this trade-off explicitly rather than overselling the tool as AI-powered.

## What's next

The most useful next steps would be adding PDF or DOCX export alongside the current plain text output, and optionally layering an AI-generated custom paragraph on top of the existing template as an opt-in enhancement rather than a replacement for it.
