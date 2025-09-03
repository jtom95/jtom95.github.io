import subprocess
import shutil
import tempfile
from pathlib import Path

# Paths
def main():
    root = Path(__file__).parent.parent
    tex_file = root / "list_of_publications.tex"
    output_dir = root / "files"
    output_dir.mkdir(exist_ok=True)

    # Temporary build directory
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)

        # Copy tex and bib files into temp directory
        shutil.copy(tex_file, tmpdir / tex_file.name)
        for bib in root.glob("*.bib"):
            shutil.copy(bib, tmpdir / bib.name)

        # Run LaTeX build (pdflatex -> biber -> pdflatex -> pdflatex)
        cmds = [
            ["pdflatex", "-interaction=nonstopmode", tex_file.name],
            ["biber", tex_file.stem],
            ["pdflatex", "-interaction=nonstopmode", tex_file.name],
            ["pdflatex", "-interaction=nonstopmode", tex_file.name],
        ]

        for cmd in cmds:
            print("Running:", " ".join(cmd))
            subprocess.run(cmd, cwd=tmpdir, check=True)

        # Move final PDF into ./files
        pdf_file = tmpdir / f"{tex_file.stem}.pdf"
        shutil.move(str(pdf_file), str(output_dir / pdf_file.name))
        print(f"✅ Generated PDF saved to {output_dir/pdf_file.name}")

# Temp dir and aux files are automatically cleaned up
if __name__ == "__main__":
    main()