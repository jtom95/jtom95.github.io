from _bib_to_markdown import main as md_main
from _build_list_of_pubs import main as pdf_main


def main():
    print("\n▶ Generating Markdown from BibTeX...")
    md_main()
    print("✅ Markdown updated.")

    print("\n▶ Building PDF from LaTeX...")
    pdf_main()
    print("✅ PDF updated.")

    print("\n🎉 All publications updated successfully!")


if __name__ == "__main__":
    main()
