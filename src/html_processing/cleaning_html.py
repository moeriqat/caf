from concurrent.futures import ProcessPoolExecutor

from bs4 import BeautifulSoup
import os
from .table_processing import chain

OUTPUT_PATH ="src/data/cleaned_text"
NUM_EXECUTORS = 4

tags_to_remove = [
        'script',       # JavaScript
        'style',        # CSS styles
        'noscript',     # No-script content
        'iframe',       # Embedded frames
        'nav',          # Navigation
        'footer',       # Footer
        'header',       # Header
        'aside',        # Sidebar content
        'form',         # Forms
        'button',       # Buttons
        'input',        # Input fields
        'select',       # Dropdowns
        'textarea',     # Text areas
        'svg',          # SVG graphics
        'canvas',       # Canvas elements
        'audio',        # Audio elements
        'video',        # Video elements
        'embed',        # Embedded objects
        'object',       # Object elements
        'img',          # Images
        'picture',      # Picture elements
        'figure',       # Figure elements (often contain images)
        'figcaption',   # Figure captions
    ]

def read_html(path: str):
    with open(path, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "lxml")
        html_body = soup.find(id="mw-content-text")
        return html_body, soup

def clean_html(html_body):
    for tag in tags_to_remove:
        for element in html_body.find_all(tag):
            element.decompose()

def fetch_tables(html_body):
    tables = html_body.find_all("table")
    return tables

def process_table(table):
    return chain.invoke(table)

def process_tables(tables, html_body, soup):
    for table in tables:
        new_paragraph = soup.new_tag("p")
        processed_table = process_table(table)
        new_paragraph.string = processed_table
        table.replace_with(new_paragraph)

def save_text(text, file_name):
    with open(os.path.join(OUTPUT_PATH, file_name), "w", encoding="utf-8") as f:
        f.write(text)

def process_html_file(html_path):
    html_body, soup = read_html(html_path)
    clean_html(html_body)
    tables = fetch_tables(html_body)
    process_tables(tables, html_body, soup)
    text_html = html_body.get_text()
    output_name = html_path.split("\\")[-1].replace(".html", ".txt")
    save_text(text_html, output_name)

def process_all_html_files(data_path):
    html_paths = [os.path.join(data_path, fname) for fname in os.listdir(data_path) if fname.endswith(".html")]

    with ProcessPoolExecutor(max_workers=NUM_EXECUTORS) as executor:
        executor.map(process_html_file, html_paths)


