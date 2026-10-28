# Official journal guidance and Word manuscript delivery

Use this reference after the author explicitly names a target journal and when creating or updating the full manuscript DOCX.

## Retrieve official journal requirements

An explicit target-journal choice authorizes retrieval of publicly available journal guidance into the selected manuscript project. Do this proactively after workspace initialization or when the journal is later specified.

1. Resolve the journal identity and publisher from an official journal or publisher domain. Guard against similarly named journals. Record the journal name as displayed by the official source.
2. Locate the current official **Aims and Scope** and **Guide for Authors**. Prefer journal-specific pages. A publisher-wide guide is acceptable only when the official journal page directs authors to it; record that scope.
3. Save the materials under `01_inputs/01_target_journal/author_guidelines`:
   - preserve an official PDF unchanged when one is offered;
   - for HTML-only guidance, save a readable dated PDF or HTML snapshot when available and a UTF-8 text/Markdown extraction for analysis;
   - use clear dated names such as `aims_and_scope_YYYY-MM-DD` and `guide_for_authors_YYYY-MM-DD`;
   - do not overwrite an older snapshot when the journal or guidance changes.
4. Create or update `official_guidance_manifest.json` in the same folder. For each item record: `document_role`, `journal`, `publisher`, `official_url`, `accessed_at`, `retrieved_file`, `extracted_text_file` when created, `sha256`, `retrieval_status`, and a short `scope_note`.
5. Open and inspect the saved artifact. Confirm that it contains the expected journal identity and relevant content rather than a login page, cookie wall, error response or generic publisher landing page.
6. If the official site blocks saving, record the official URL, access date, failure mode and any readable official content in the manifest. Report the gap and continue with other available work. Do not silently substitute third-party instructions as authoritative.
7. If the official site supplies a manuscript Word template or checklist, save it unchanged under `01_inputs/01_target_journal/journal_templates` and record its source in the manifest.

Extract actionable requirements into `04_manuscript_plan/journal_profile.md` with the official source and verification date. Keep formal requirements separate from patterns observed in published papers. Recheck current official guidance when the target journal changes, at journal transfer, or before final submission if the saved snapshot may be stale.

## Create and maintain the Word manuscript

- New projects use `05_drafts/merged_manuscript/manuscript.docx` as the default canonical manuscript. Record that path in `00_project/project.json`.
- Create a real DOCX with available document tooling; never rename Markdown or plain text to `.docx`. Use the official journal template when it is required and compatible. Otherwise use a restrained editable manuscript layout.
- Keep headings, paragraphs, tables, captions, references and equations editable. Insert figures at review resolution while retaining the separate source figures in the project.
- Put Chinese editorial explanations and evidence notes in `05_drafts/revision_notes`, not in the clean manuscript. Provide comments or tracked changes only when the author requests that review mode.
- Before each DOCX handoff, verify the current canonical path, extract its text for factual and placeholder checks, render it, and visually inspect pagination, tables, figures, symbols, references and cross-references. Document validation alone is insufficient.
- When the author or a collaborator returns an edited Word file, treat that latest file as the candidate canonical version. Compare and reconcile it before further generation; preserve their edits and archive the superseded version under `05_drafts/history`. Do not regenerate from an older Markdown draft.
- Create versioned submission copies under `06_submission/manuscript` only after the scientific content and intended version are identified. A submission copy does not replace the working canonical file unless the author explicitly adopts it.

If DOCX creation is temporarily unavailable, continue evidence mapping and drafting in review records, report the unavailable export, and create the Word manuscript when document tooling becomes available. Do not describe a text draft as the requested Word deliverable.

## Preserve the source when transferring journals

Prefer editing a derived copy of the latest supplied DOCX over extracting plain text and rebuilding it. Rebuilding can discard equations, superscripts/subscripts, semantic emphasis, hyperlinks, citations and author edits. When rebuilding is necessary, disclose that choice and verify both content and formatting against the source; unchanged tables and image hashes alone do not establish full-manuscript fidelity.

Establish the baseline by path, date and optional hash before editing. Inspect tracked changes and equations through DOCX-aware tooling or the application's final view; plain paragraph extraction can omit them. Do not interpret a mismatch between an author's recollection and a saved file as permission to invent a third version. Give the exact conflicting passage and record the author's correction; propagate it only to the affected outputs.

Separate format adaptation, language compression and scientific reinterpretation. A journal transfer does not itself authorize dropping measured values, changing experimental provenance or adding a new spectral interpretation. Preserve ambiguous measurements and flag their missing definition outside clean prose rather than silently deleting them or assigning a conventional unit. Make changes to configuration confidence, causal claims, method conditions or assay endpoints traceable and visible for scientific review.

Check paragraph alignment, headings, species italics, semantic emphasis and mathematical typography in the actual output. Apply the author's or journal's conventions by meaning: an emphasized compound identifier is distinct from an atom label, figure number, fraction label, quantity or citation. Preserve run properties and native equations when changing a nearby reference. Verify scientific notation after a text replacement, especially when a previously superscripted exponent becomes ordinary text.
