## WriteFlow

WriteFlow is a small personal command-line tool for generating tailored cover letters during a job search. It is a single Python script rather than a full application: there is no server, no web frontend, and no AI API involved. Instead it uses Python's built-in string templating to fill a cover letter template with a candidate profile plus the job title and company supplied on the command line.

## What it does

Running the script with a job title and company name produces a complete cover letter built from a template, personalized with a profile dictionary defined at the top of the file (name, location, contact details, education, key achievements, availability and right-to-work status). An optional custom paragraph can be passed in to say something specific about the company; otherwise a sensible default sentence is generated from the company name. Every generated letter is saved as a timestamped .txt file in an output folder, and each run also appends an entry to a local applications.json file, so a simple history of what was drafted and when builds up automatically as the log grows.

## Usage

```bash
python writeflow.py --job "Business Analyst" --company "Tesco"
```

Add --custom to supply a bespoke paragraph, or --output to change where generated letters are saved. Run python writeflow.py --help to see all options.

## Tech stack

The script only uses the Python standard library: os, re, json, datetime, string.Template and argparse. There are no external dependencies to install and nothing to configure beyond editing the DEFAULT_PROFILE values at the top of writeflow.py to match the person using it.

## Project structure

The repository is intentionally minimal: writeflow.py contains the profile data, the template, the generation and saving logic, and the command-line entry point, and this README documents it. Generated output files and the applications log are created at runtime and are not checked into the repository.

## Honest framing

This is a genuinely small, working utility built to solve a real, specific problem during an active job search, not a scaffold for a larger product. The templating approach is deliberate: it is fast, predictable and has no external API dependency, at the cost of the letters all following the same structure.

## Possible next steps

Natural extensions would be exporting to PDF or DOCX in addition to plain text, and optionally wiring in an AI API for a first-draft custom paragraph instead of the current default sentence, while keeping the core templating approach as a reliable fallback.

## Author

Manoj Kumar Kavuri — [GitHub Profile](https://github.com/manojkumarkavuri20-a11y)
