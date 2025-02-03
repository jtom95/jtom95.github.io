#!/usr/bin/env python
# coding: utf-8

"""
This script reads a BibTeX file (e.g., "my_publications.bib") and converts each entry
into a Markdown file with front-matter structured as:

---
title: "Paper Title Number 1"
collection: publications
category: manuscripts
permalink: /publication/2009-10-01-paper-title-number-1
excerpt: 'This paper is about the number 1. The number 2 is left for future work.'
date: 2009-10-01
venue: 'Journal 1'
slidesurl: 'http://academicpages.github.io/files/slides1.pdf'
paperurl: 'http://academicpages.github.io/files/paper1.pdf'
citation: 'Your Name, You. (2009). &quot;Paper Title Number 1.&quot; <i>Journal 1</i>. 1(1).'
---
 
Each Markdown file will be written to <output_folder>/<filename>. The filename is based on the publication date and a URL‐friendly slug of the title.
"""

import os
import re
import html
from datetime import datetime
from pybtex.database.input import bibtex

# ---------------------------
# User Settings
# ---------------------------

# Name of the BibTeX file to process.
bib_filename = "my_publications.bib"

# Output folder for the generated Markdown files.
output_folder = "_publications"

# Fixed front-matter fields (can be adjusted as needed)
collection = "publications"
category = "manuscripts"
permalink_prefix = "/publication/"

# ---------------------------
# Helper Functions
# ---------------------------


def get_category(entry):
    if entry.type == "article":
        return "publications"
    elif entry.type == "inproceedings":
        return "conferences"
    else:
        return "other"  


def html_escape(text):
    """Escape HTML characters in text."""
    return html.escape(text, quote=True)


def slugify(text):
    """
    Create a URL-friendly slug from a string:
      - Lowercases the text,
      - Removes problematic characters,
      - Replaces spaces with hyphens.
    """
    text = text.lower().strip()
    # Remove any characters that are not alphanumeric, spaces, or hyphens.
    text = re.sub(r"[^\w\s-]", "", text)
    # Replace any group of whitespace with a single hyphen.
    text = re.sub(r"[\s]+", "-", text)
    return text


def get_date(fields):
    """
    Extract date from the BibTeX fields.
    Uses "year" and optionally "month" and "day".
    Returns a date string in the format YYYY-MM-DD.
    """
    year = fields.get("year", "1900")
    month = fields.get("month", "01")
    day = fields.get("day", "01")

    # Normalize month: if month is a number (as string) or a three-letter abbreviation.
    if month.isdigit():
        month = f"{int(month):02d}"
    else:
        try:
            # Try to parse abbreviated month names (e.g., "Jan", "February", etc.)
            dt = datetime.strptime(month[:3], "%b")
            month = f"{dt.month:02d}"
        except ValueError:
            month = "01"  # fallback

    # Normalize day if necessary.
    if day.isdigit():
        day = f"{int(day):02d}"
    else:
        day = "01"

    return f"{year}-{month}-{day}"

def get_author_list(entry):
    """
    Get a list of authors from the BibTeX entry.
    """
    persons = entry.persons.get("author", [])
    authors = []
    for person in persons:
        # Join first names and last names.
        author_name = " ".join(person.first_names + person.last_names)
        authors.append(author_name)
    return authors


def build_citation(entry):
    """
    Build a simple citation string from the BibTeX entry.
    This example uses the first names and last names of all authors,
    the year, title, and venue. You can expand this to include volume,
    number, pages, etc.
    """
    fields = entry.fields
    persons = entry.persons.get("author", [])

    # # Build authors list.
    # authors = []
    # for person in persons:
    #     # Join first names and last names.
    #     author_name = " ".join(person.first_names + person.last_names)
    #     authors.append(author_name)
    authors = get_author_list(entry)
    authors_str = ", ".join(authors) if authors else "Unknown Author"

    # Get title.
    title = fields.get("title", "No Title").replace("{", "").replace("}", "")
    title_escaped = html_escape(title)

    # Get publication year.
    year = fields.get("year", "1900")

    # Determine the venue: first check for "journal", then "booktitle".
    venue = fields.get("journal", fields.get("booktitle", ""))
    venue_escaped = html_escape(venue)

    # Construct a very simple citation.
    citation = f"{authors_str}. ({year}). &quot;{title_escaped}&quot; <i>{venue_escaped}</i>."
    return citation


def get_doi(entry):
    """
    Get the DOI from the BibTeX entry.
    """
    doi = entry.fields.get("doi", "")
    return doi

def build_markdown(entry):
    """
    Build the Markdown text (front-matter + optional content) from a BibTeX entry.
    """
    fields = entry.fields

    # Title
    title = fields.get("title", "No Title").replace("{", "").replace("}", "")
    title = title.strip()
    title_escaped = html_escape(title)
    
    # authors
    authors = get_author_list(entry)
    author_string = ", ".join(authors)

    # Date (using year, month, day if available)
    pub_date = get_date(fields)

    # Slug for permalink and filename
    slug = slugify(title)
    

    # Permalink
    permalink = f"{permalink_prefix}{pub_date}-{slug}"

    # Excerpt: use "abstract" if available, otherwise "note" (or empty string)
    excerpt = fields.get("abstract", fields.get("note", ""))
    excerpt = excerpt.strip()
    excerpt_escaped = html_escape(excerpt)

    # Venue: check for "journal" first, then "booktitle"
    venue = fields.get("journal", fields.get("booktitle", ""))
    venue = venue.strip()
    venue_escaped = html_escape(venue)

    # Additional URLs: slidesurl and paperurl (if provided)
    slidesurl = fields.get("slidesurl", "").strip()
    paperurl = fields.get("paperurl", "").strip()

    # Build citation string
    citation = build_citation(entry)

    # Build Markdown front-matter
    md = "---\n"
    md += f'title: "{title_escaped}"\n'
    md += f"collection: {collection}\n"
    md += f"category: {get_category(entry)}\n"
    md += f"permalink: {permalink}\n"
    md += f"authors: '{author_string}'\n"
    md += f"doi: '{get_doi(entry)}'\n"
    if excerpt_escaped:
        md += f"excerpt: '{excerpt_escaped}'\n"
    md += f"date: {pub_date}\n"
    md += f"venue: '{venue_escaped}'\n"
    if slidesurl:
        md += f"slidesurl: '{slidesurl}'\n"
    if paperurl:
        md += f"paperurl: '{paperurl}'\n"
    md += f"citation: '{citation}'\n"
    md += "---\n\n"

    # Optionally, you can add more content below the front matter.
    # For now, we leave it blank.

    return md, f"{pub_date}-{slug}.md"


# ---------------------------
# Main Processing
# ---------------------------


def main():
    # Ensure the output folder exists.
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Parse the BibTeX file.
    parser = bibtex.Parser()
    bib_data = parser.parse_file(bib_filename)

    # Process each entry.
    for entry_key, entry in bib_data.entries.items():
        try:
            md_content, filename = build_markdown(entry)
            output_path = os.path.join(output_folder, filename)
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(md_content)
            print(f"Processed {entry_key}: {filename}")
        except Exception as e:
            print(f"Error processing {entry_key}: {e}")


if __name__ == "__main__":
    main()
