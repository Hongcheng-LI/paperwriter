# Validation and change handling

For a canonical Markdown/TXT/TEX draft, run `python "<skill-base>/scripts/project_tools.py" placeholders --root "<project-root>" --file "<canonical-relative-path>"`. Exit 1 means markers found, 2 means an error. For the default canonical DOCX, extract current text and inspect the document with DOCX-aware checks; the placeholder script does not read DOCX. It detects a limited marker set only, and zero matches never means ready to submit.

Verify in proportion to study:

- Writing quality: state the central takeaway; check that the Introduction establishes its rationale, Results show the decisive evidence, Discussion interprets rather than repeats, and Abstract/Title/Conclusion agree on scope. Check paragraph roles, transitions, repetition, main-text/SI allocation and methods readability. Fix unclear prose rather than defend it in a rationale.
- Source and version correspondence; numerical, identifier and unit consistency.
- Methods sufficiently report what actually produced each result.
- Figure/table numbering, captions, raw-to-derived mapping and SI references.
- Citation identity and passage support; official journal requirements with verification date.
- Official Aims and Scope and Guide for Authors saved from official sources, opened successfully, recorded in the guidance manifest, and reflected in the manuscript plan.
- Limitations and observation/interpretation/hypothesis wording.
- Author edits preserved and canonical/derived outputs reconciled.
- For journal transfer, source-to-output paragraph changes classified and checked for lost measurements, equations, experimental provenance and semantic formatting; a matching data table does not establish prose fidelity.
- For a technical resubmission, the applicable article type and counted ranges recorded, actual word counts measured, figure/table upload multiplicity checked, and all main-text/SI references resolved against the current files; see references/technical-resubmission.md.
- Canonical and submission DOCX files visually inspected after rendering; confirm that collaborator edits were reconciled from the latest Word version.

Continuous-word overlap can be checked against the authorized corpus using a transparent normalization/window method. Report corpus coverage, exclusions and thresholds. This is not plagiarism certification; low overlap is not evidence of originality, and common technical phrases need contextual review.

Readiness fields: draft_complete, scientific_review_complete, formatting_review_complete, author_approved_submission. Record scope and unresolved items for each. Do not turn any field true merely because files exist. Final human acceptance covers content, authorship and declarations; never invent author approvals or ethics/registration/data availability details.

For a full-manuscript handoff deliver 07_quality_control/final_report.md from its template, or the equivalent in the established layout. A focused section task needs only scoped checks and a concise handoff, not a submission package. Critical unresolved items prevent submission_ready. Approved packaging includes a manifest of canonical version, included files and remaining noncritical notes.

Changes:
- Give each actionable review finding a version-specific locator: file, section, paragraph opening or searchable quotation, and figure/table/panel/row where relevant. Add a rendered page number when available, but never rely on page number alone. Explain the issue, its evidence, and the replacement or concrete action; distinguish confirmed errors from questions requiring evidence. Do not invent line numbers for Word files.
- Recheck the actual latest saved artifact before calling an issue unresolved. A prior review list is a retrieval aid, not current evidence. Retire resolved questions and report only remaining or newly introduced issues.
- Re-inventory changed sources and compare snapshot revisions.
- Traverse source_id → claim_id → output_links to mark affected text, abstract, figures, captions and SI.
- Report added/changed/missing files and unresolved renames.
- Where links are absent, perform manual review; never claim exhaustive impact detection.
- Reopen only affected gate reservations. Journal transfer preserves project evidence and old journal versions, refreshes official guidance, corpus role and writing blueprint.

The bundled tools do not interpret science, verify external citations, split PDFs reliably, update manuscript claims automatically, or approve submission. State these boundaries in handoff.
