# Reproducibility Checklist

- Main diagnostic generator: `scripts/recover_paper51.py`.
- V2 hardening generator: `scripts/v2_probe_coverage_stress.py`.
- V2 outputs: `docs/v2_probe_coverage_stress.json`, `docs/v2_probe_coverage_stress.csv`, and `paper/v2_probe_coverage_table.tex`.
- Manuscript source: `paper/main.tex`.
- Build command: `powershell -ExecutionPolicy Bypass -File scripts/build_pdf.ps1`.
- Canonical PDF: `C:/Users/wangz/Downloads/51.pdf`.
- Local generated PDF policy: `paper/main.pdf` is ignored and removed after build.
- Desktop PDF copy: absent.
