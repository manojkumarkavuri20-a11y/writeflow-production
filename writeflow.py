"""
WriteFlow Production - Cover Letter & Document Generator
AI-powered writing assistant for job seekers.
Author: Manoj Kumar Kavuri
"""

import os
import re
import json
from datetime import datetime
from string import Template
from typing import Optional


# ─────────────────────────────────────────────
# USER PROFILE
# ─────────────────────────────────────────────

DEFAULT_PROFILE = {
    "name": "Manoj Kumar Kavuri",
    "location": "Bracknell, UK",
    "email": "manojkumarkavuri20@gmail.com",
    "linkedin": "https://www.linkedin.com/in/manojkumarkavuri/",
    "education": "MSc International Business Management (Distinction), University of East London",
    "skills": "SQL, Power BI, Tableau, Advanced Excel, Google Analytics, n8n automation",
    "experience_summary": (
        "Graduate analyst with 27+ months of hands-on retail operations experience, "
        "digital marketing internship at BorderlessHR Inc., and volunteer Operations Support "
        "Analyst role at Care4Calais. Wharton Business Analytics certified."
    ),
    "key_achievement_1": "Delivered 30% higher campaign ROI through A/B testing and audience segmentation",
    "key_achievement_2": "Improved inventory accuracy by 25% through spreadsheet-based tracking systems",
    "key_achievement_3": "Cut donation processing time by 20% at Care4Calais with zero delivery delays",
    "availability": "Immediately available",
    "visa": "UK Graduate Route Visa — no sponsorship required",
}


# ─────────────────────────────────────────────
# COVER LETTER TEMPLATE
# ─────────────────────────────────────────────

COVER_LETTER_TEMPLATE = """
$name
$location | $email
$linkedin

$date

Dear Hiring Manager,

I am writing to apply for the $job_title role at $company_name. With $experience_summary, \
I am confident I can add immediate value to your team.

In my previous roles I have:
- $key_achievement_1
- $key_achievement_2
- $key_achievement_3

$custom_paragraph

I am $availability and hold the right to work in the UK ($visa).

I would welcome the opportunity to discuss how my background aligns with your needs.

Kind regards,
$name
"""


# ─────────────────────────────────────────────
# GENERATOR
# ─────────────────────────────────────────────

def generate_cover_letter(
    job_title: str,
    company_name: str,
    custom_paragraph: Optional[str] = None,
    profile: dict = DEFAULT_PROFILE,
) -> str:
    """
    Generate a tailored cover letter.

    Args:
        job_title: The role you are applying for.
        company_name: The company you are applying to.
        custom_paragraph: Optional bespoke paragraph about why this company.
        profile: Applicant profile dict (defaults to DEFAULT_PROFILE).

    Returns:
        Formatted cover letter as a string.
    """
    values = {
        **profile,
        "job_title": job_title,
        "company_name": company_name,
        "date": datetime.now().strftime("%d %B %Y"),
        "custom_paragraph": custom_paragraph or (
            f"I am particularly drawn to {company_name} because of its reputation "
            "for data-driven decision making and collaborative culture."
        ),
    }
    tmpl = Template(COVER_LETTER_TEMPLATE)
    return tmpl.substitute(values).strip()


def save_cover_letter(content: str, job_title: str, company_name: str, output_dir: str = "output") -> str:
    """Save the cover letter to a .txt file and return the file path."""
    os.makedirs(output_dir, exist_ok=True)
    safe_title = re.sub(r"[^\w\-]", "_", f"{company_name}_{job_title}")
    filename = f"{safe_title}_{datetime.now().strftime('%Y%m%d')}.txt"
    filepath = os.path.join(output_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Cover letter saved to: {filepath}")
    return filepath


def log_application(job_title: str, company_name: str, filepath: str, log_file: str = "applications.json"):
    """Append an application entry to a JSON log."""
    entry = {
        "date": datetime.now().isoformat(),
        "job_title": job_title,
        "company": company_name,
        "cover_letter": filepath,
        "status": "drafted",
    }
    log = []
    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            log = json.load(f)
    log.append(entry)
    with open(log_file, "w") as f:
        json.dump(log, f, indent=2)
    print(f"Application logged: {company_name} — {job_title}")


# ─────────────────────────────────────────────
# CLI ENTRY POINT
# ─────────────────────────────────────────────

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="WriteFlow — Cover Letter Generator")
    parser.add_argument("--job", required=True, help="Job title e.g. 'Business Analyst'")
    parser.add_argument("--company", required=True, help="Company name e.g. 'Tesco'")
    parser.add_argument("--custom", default=None, help="Optional custom paragraph")
    parser.add_argument("--output", default="output", help="Output directory")
    args = parser.parse_args()

    letter = generate_cover_letter(
        job_title=args.job,
        company_name=args.company,
        custom_paragraph=args.custom,
    )
    print("\n" + "=" * 60)
    print(letter)
    print("=" * 60 + "\n")

    path = save_cover_letter(letter, args.job, args.company, args.output)
    log_application(args.job, args.company, path)
