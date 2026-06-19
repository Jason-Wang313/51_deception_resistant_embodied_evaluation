# Paper 51 VLA Highlight Hardening Plan

Date: 2026-06-20

## Objective

Harden the visual highlight/link-box styling in Paper 51 so it matches the VLA-v4 role-model PDF's professional red and green boxed callouts while preserving the final full-scale deception-resistant embodied evaluation manuscript, results, page count, and scientific claims.

## Current Evidence

- Canonical PDF: `C:/Users/wangz/Downloads/51.pdf`.
- Current page count: 25.
- Current affected link pages: 2, 3, 4, and 5.
- Current link annotations: 4 red internal-reference links.
- Current border state: all 4 link annotations use border `(0, 0, 0)`, so the boxes are invisible.
- Current LaTeX source uses `\hypersetup{colorlinks=true,linkcolor=black,citecolor=black,urlcolor=black}` in `paper/main.tex`.
- Current final result remains the full-scale deception-resistant evaluation benchmark: 302,400 compact condition rows, 23,030,784,000 represented policy evaluations, and 2,210,955,264,000 represented frame decisions.

## Role-Model Style Target

Match the VLA-v4 role model's link annotation style:

```tex
\hypersetup{
  colorlinks=false,
  pdfborder={0 0 1},
  citebordercolor={0 1 0},
  linkbordercolor={1 0 0},
  urlbordercolor={0 1 0}
}
```

Expected Paper 51 result after rebuild:

- Page count remains 25.
- All 4 internal-reference link annotations remain red.
- All 4 link annotations use border `(0, 0, 1)`.
- No scientific content, benchmark data, or claim is changed.

## Execution Plan

1. Render the affected pre-change pages to `C:/Users/wangz/highlight_box_hardening/tmp/pdfs/paper51_before` for baseline visual comparison.
2. Replace the current black color-link `\hypersetup` in `paper/main.tex` with the VLA-v4 hyperref settings above.
3. Rebuild using `scripts/build_pdf.ps1`, which exports only the canonical PDF to Downloads, records build metadata, and removes `paper/main.pdf`.
4. Verify with `pypdf` that the rebuilt PDF has 25 pages, 4 red link annotations, and 4 `(0, 0, 1)` borders.
5. Render the affected post-change pages to `C:/Users/wangz/highlight_box_hardening/tmp/pdfs/paper51_after` and visually inspect the highlight pages for professional box weight, alignment, spacing, and legibility.
6. Update README, child status, and tracked audit metadata if needed so the canonical PDF hash and visual hardening evidence match the actual output.
7. Remove Paper 51 temporary render folders after QA.
8. Commit and push the clean repo before moving to the next paper.

## Non-Goals

- Do not rerun the benchmark.
- Do not pad content or alter the 25-page manuscript to chase page count.
- Do not revise claims, tables, captions, or results unless a visual/layout defect requires a tiny local wording adjustment.
