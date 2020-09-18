import os
import re
import sys
import time

from PyPDF2 import PdfFileMerger

_path = os.path.realpath(os.path.abspath(__file__))
ROOT = os.path.dirname(_path)
sys.path.insert(0, ROOT)

from build_pdf import main as main_build_pdf


def get_chunk(marker, content):
    "Get chunk of content in Markdown"
    chunk = ""
    r = re.compile(
        r"<!\-\- {} starts \-\->(?P<{}>.*)<!\-\- {} ends \-\->".format(
            marker, marker, marker
        ),
        re.DOTALL,
    )
    m = r.search(content)
    if m:
        chunk = m.group(marker)
    return chunk


def get_links(content):
    "Get list[dict] Markdown links from content"
    name_regex = "[^]]+"
    url_regex = 'https[s]?://.+[^\)"]'
    link_regex = '\[(?P<text>{0})\]\(\s*(?P<url>{1})(?:(?P<title>\s*".+"))?\)'.format(
        name_regex, url_regex
    )
    r = re.compile(link_regex)
    links = [
        {"text": link[0], "url": link[1].strip(" "), "title": link[2].strip('"')}
        for link in r.findall(content)
    ]
    return links


if __name__ == "__main__":  # pragma: no cover
    pdf_list = []
    pdf_merger = PdfFileMerger()
    pdf_dir = os.sep.join([ROOT, "pdfs"])

    with open("README.md", "r") as _file:
        content = _file.read()

    toc_content = get_chunk("toc", content)
    links = get_links(toc_content)

    for link in links:
        url = link["url"]
        try:
            pdf_name = main_build_pdf(url)
            pdf_merger.append(
                os.sep.join([pdf_dir, pdf_name]),
                bookmark=link["text"],
                import_bookmarks=False,
            )
        except Exception as err:
            print("Error building PDF from: %s\n" % url)
            print(err + "\n")
            continue
        time.sleep(1)

    pdf_out = "Real_Python.pdf"

    with open(file=os.sep.join([ROOT, pdf_out]), mode="wb") as output_file:
        pdf_merger.write(output_file)

    pdf_merger.close()
    print("Done. 📖 Enjoy %s 🤓" % pdf_out)
