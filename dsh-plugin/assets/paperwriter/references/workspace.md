# Workspace

For a new full-manuscript project use the directory layout defined in assets/layout.json. Existing projects retain their established layout; focused review or editing does not require a new scaffold. Initialize in the user's selected root, never the skill directory. Existing files are retained byte-for-byte. A collision with a required directory or redirected path is an error; explain it without relocating user data.

An environment-only bootstrap is a complete, useful first action. It needs only the selected project root and the user's intent to use this skill. Target journal, article type and study summary may remain null until the user supplies them. Initialization does not authorize reading unrelated files elsewhere, moving source materials, analyzing empty folders or creating a manuscript from assumptions.

The initializer creates directories and only three starter files: START_HERE.md, project.json, status.json in 00_project. Generate other records only when their phase needs them. Do not copy papers into the installed skill.

Status stages: awaiting_journal_materials, journal_corpus_review, awaiting_project_materials, evidence_mapping, blueprint_review, drafting, validation, author_review, submission_ready. Store gate acceptance with scope, artifact version, date and author message reference. A completed command never counts as author acceptance. Existing acceptance persists unless affected inputs change.

project.json holds journal, article type, study summary, manuscript language and canonical_manuscript. For a new project, `canonical_manuscript` defaults to `05_drafts/merged_manuscript/manuscript.docx`. Status holds pending issues and gate records. User-confirmed decisions belong in 00_project/author_decisions.md; they are project decisions, not universal skill rules.

A normal analysis start requires source papers and a short project summary; workspace bootstrap does not. Do not demand an arbitrary minimum if fewer useful papers exist: explain limited representativeness. Gather journal materials before opening full project results. All inputs can already be present; the user need not move them again.

After bootstrap, give the author this short placement map in their collaboration language:

- target-journal example papers → `01_inputs/01_target_journal/reference_articles`
- official Aims and Scope and Guide for Authors → retrieved by the assistant into `01_inputs/01_target_journal/author_guidelines` after the journal is named
- journal templates → `01_inputs/01_target_journal/journal_templates`, including an official Word template when available
- raw results, methods, code, figures/tables, existing drafts and project references → their matching folders under `01_inputs/02_research_materials`
- optional supervisor/preference papers → `01_inputs/03_preference_papers`

Tell the author to return with “期刊材料已放好” when the journal examples are ready. They may place all research materials at the same time, but journal-pattern analysis remains the first full-workflow stage. If materials do not fit a category, leave them in their author-chosen location and record a path manifest later; do not silently reorganize them.

For resumed work read available state, relevant decisions and the requested artifact, then proceed. Do not require missing new-format state files in a legacy project. Avoid asking the author to approve routine extraction, file naming or check execution.

When an author reports sending a version to a supervisor, treat it as an author-review milestone, not scientific approval or journal submission. Preserve the identity of the sent version when known; do not silently regenerate it while preparing later revisions.

For a second manuscript, reuse the workflow and relevant journal-pattern records with their provenance. Start a separate project evidence scope and identifier mapping. Reassess journal/article-type fit and any overlap with prior papers; do not inherit compounds, parameters, conclusions, unresolved questions, or gate approvals from the first manuscript. Existing source papers can be reused without rebuilding the corpus when they remain relevant.
