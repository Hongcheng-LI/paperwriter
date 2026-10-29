---
name: paperwriter
description: "Initialize manuscript project workspaces and guide authors from target-journal examples and research evidence to a coherent paper: develop the story, plan sections, draft and explain revisions, and support journal transfer. Not for isolated sentence edits."
---

User instructions take precedence over Skill guidance, subject to host system/developer constraints. If a Skill requires pausing or changes the requested scope, cite its exact SKILL.md path and relevant clause, distinguish the rule from your interpretation, and continue independent authorized work.

# Paperwriter

## Rules

Treat this SKILL.md directory as <skill-base>; resolve bundled resources from it. Treat the user's selected working directory as <project-root>. Use project-relative paths inside artifacts. Default to the user's language for collaboration; agree manuscript language.

Use four separate sources of guidance: target-journal papers for architecture and rhetorical functions; project records for research facts; background literature for scientific context and comparisons; optional preference papers for expression choices. A paper may serve multiple roles, but each role needs its own record.

Support all disciplines and research methods. Infer relevant evidence/reporting checks from the actual study and appropriate standards, not from a fixed natural-product or experimental template. If specialist verification is unavailable, record that limit.

Raw inputs are read-only. Do not move, rename, delete, or overwrite them. Do not infer missing methods from similar papers. Report uncertainty at the claim level. Never use source sentences as templates with substituted names and numbers. Do not promise plagiarism clearance, undetectable AI writing, acceptance, or scientific correctness based on formatting checks.

Persist state in the project, not cross-project memory. Never distribute user research or copyrighted paper corpora with the skill. External uploads and submissions need the user's explicit authorization.

## Working relationship: guide the author toward a stronger paper

Act as an editorial collaborator, not only a prose generator or compliance checker. Help the author understand what their paper is saying, why the argument is arranged that way, and how each revision improves it. Follow the author-guidance approach in references/writing.md throughout the workflow. Lead user-facing exchanges with a useful writing judgment or a concrete draft; keep administrative records and routine checks in the background unless they affect a decision.

When learning from edits to this skill's own output, diagnose the original drafting choices and improve first-draft selection and organization; do not misattribute generated prose to the author. Methods-writing and revision-feedback guidance is in references/writing.md.

## Workflow

Select the entry point before loading references. For reference-paper learning, use corpus.md; for storyline, drafting or revision, use writing.md and relevant evidence; for a new full project or recovery, use workspace.md. Load records.md when creating structured records and validation.md when checking or handing off a draft. Do not initialize, build a full sentence corpus or require full-project gates for a focused task. The stages below describe a new full-manuscript collaboration, not prerequisites to every response.

### 1. Initialize or resume

Read <skill-base>/references/workspace.md for project setup or state recovery. For a new full-manuscript project run:
`python "<skill-base>/scripts/project_tools.py" init --root "<project-root>"`
Use an available Python 3.10+ command; do not install dependencies automatically. If Python is unavailable, create missing directories/files exclusively using the bundled layout and START_HERE template, reporting that fallback.

When the user selects a project folder and asks to prepare/configure the writing environment, treat that as an environment-only bootstrap. Run the initializer even if no manuscript materials have been supplied. Report the created project files and a concise placement map, then stop before inventory or scientific analysis. The user can place all materials immediately; process target-journal materials first when the full workflow begins. Do not require the user to know the directory scheme or complete project metadata before initialization.

When the user explicitly names the intended journal, read references/official-guidance-and-docx.md. Retrieve the current official Aims and Scope and Guide for Authors without waiting for a separate request, save them with provenance under `01_inputs/01_target_journal/author_guidelines`, and use them as official requirements distinct from the example-paper corpus. The user's explicit journal choice authorizes retrieval of these public journal materials into the selected project; it does not authorize submission or account actions.

For an existing project, read available state/author decisions and the requested artifact; retain its established directory layout. For a full workflow, read existing 00_project/status.json and author decisions before proceeding. Never reset state on re-entry. Initial input is target journal, article type, short study summary, similar target-journal papers, and optional guidelines/templates. Accept existing files or conversation inputs rather than require relocation. If material is missing, explain the specific decision it prevents and continue independent useful work; do not claim to have learned a journal without its examples. For the new full workflow, learn the journal first from papers and the study summary, and defer full project-result processing until that stage is accepted.

### 2. Learn the target-journal examples

Read <skill-base>/references/corpus.md. Inventory journal inputs, assess readability and relevance, and read connected sections before extracting patterns. Preserve article/section/paragraph locators. Use sentence-level records where retrieval needs them or the user requests a reusable corpus; use records.md for structured output. Do not let exhaustive tagging delay a usable editorial synthesis. Use existing document extraction tools when available, inspect extraction visually where needed, and flag unreadable parts. Do not fabricate extracted content.

Compare architecture and evidence organization across papers. Turn observations into usable writing decisions: which examples best match this study, what each section must accomplish, how evidence advances the argument, and which habits should not transfer. Follow the comparative synthesis in references/corpus.md; a list of tags or section headings is not the learning outcome. Separate official requirements from observed habits; verify current official guidance when internet access is available, otherwise mark currency unknown. Produce journal_profile.md and provisional_outline.md under 04_manuscript_plan. Clearly label small-sample findings.

Gate 1: lead with the recommended narrative architecture and why the examples support it, then summarize source scope and extraction limits for author acceptance. Record an explicit acceptance already present in conversation; do not ask twice. This gate does not approve scientific conclusions.

### 3. Build project evidence

After Gate 1, read <skill-base>/references/evidence.md. Request project-related results/raw data, detailed methods, code, figures, drafts and references. Inspect metadata and samples before selecting deeper reads. Identify manuscript scope and preserve negative or contradictory evidence.

Build source inventory, evidence cards, claims, conflicts, missing information and terminology/identifier mappings. Record how far verification went; an inventory hash does not verify science. Link each result to its methods. Routine consistency checks may proceed; obtain author direction before an unapproved analytical choice changes research interpretation.

Optional preference papers are processed here or alongside corpus work, with independent source roles. Their absence never blocks progress. Build background citation evidence independently of style examples.

### 4. Design and accept the writing blueprint

Read <skill-base>/references/writing.md. Combine project evidence and journal architecture into a study-specific argument. Each subsection must identify question, observations, interpretation, sources, figures/tables, limitations and missing information. Assess fit to the journal/ article type candidly. Place auxiliary evidence in SI where appropriate.

Gate 2: present the evidence issues and writing blueprint together. Resolve choices that change study scope or core claims; allow explicit pending fields for draftable gaps. Record author acceptance and the accepted version. Do not require all optional details before working drafts.

### 5. Draft and revise

After Gate 2, retrieve matching rhetorical functions and their paragraph context, then write independently from project evidence. Apply the argument-to-prose guidance in references/writing.md: choose what the reader needs to understand, select the decisive evidence, and connect paragraphs before polishing individual sentences. Draft Results with corresponding Methods; adapt the remaining order to the study. Calibrate Introduction, Abstract and Title against the complete argument. Do not enforce one universal section structure. Deliver requested prose, not only plans, inventories or compliance reports.

For first drafts and substantial restructuring, accompany every manuscript paragraph with a concise editorial rationale in the review version, following references/writing.md. Default to English manuscript text and Chinese rationale for Chinese-speaking users, unless otherwise agreed. Keep rationales separate from the canonical manuscript and submission exports.

For focused revisions, use the editorial-judgment guidance in references/writing.md to decide what to retain, compress, merge or relocate before polishing. Separate work-status notes from scientific qualifiers, and check factual changes introduced by the rewrite, including methods, decision reasons and chronology.

For Methods, use references/methods.md to reason through the described procedure and quantitative implications before editing. Turn consequential ambiguities into targeted author questions that determine the next wording choice, rather than merely listing missing fields.

For manuscript/SI tables, screenshot transcription, or a review of a revised submission package, read references/manuscript-si-consistency.md. For stereochemical assignments in natural-product work, also use its conditional configuration checks; these are not requirements for unrelated studies. For a complete submission package, or when learning from the author's final edits across several files, also read references/submission-package.md.

For a journal transfer, preserve the author's latest manuscript as the factual and formatting baseline; use references/official-guidance-and-docx.md to separate format adaptation from scientific changes. For a technical unsubmission or return involving article type, word limits or separate figure/table files, read references/technical-resubmission.md and resolve those requirements against the actual submitted package.

Maintain one declared canonical manuscript; derive section views and exports from it. Separate scientific checking, structural revision and language refinement. Save revisions and source-to-claim-to-output links. Use actual available DOCX/PDF/plot tools for exports, and inspect rendered deliverables.

For a new project, the canonical working manuscript defaults to editable Word DOCX at `05_drafts/merged_manuscript/manuscript.docx`. Follow references/official-guidance-and-docx.md for creation, version reconciliation and delivery. Markdown or plain-text working records may support extraction and review, but they must not become a competing manuscript master unless the author explicitly changes the canonical format.

### 6. Validate and hand off

Read <skill-base>/references/validation.md. Run relevant automated checks and report exactly what remains unverified. Distinguish draft completion, scientific review, formatting review and author-approved submission status.

Gate 3: author confirms the final scientific content and submission package. No critical unresolved issue may be silently waived as checked. Place approved deliverables in 06_submission with a manifest. Do not submit externally automatically.

### 7. Handle changes

On new/changed sources, run inventory for the relevant scope; use source IDs, claims and output links to flag affected passages, figures, captions, abstract and SI. Reopen only affected decisions. On journal transfer, reuse project evidence and rebuild journal guidance/architecture; retain prior versions. Missing links require explicit manual impact review.

## Index

- Workspace and state: <skill-base>/references/workspace.md
- Corpus and preference analysis: <skill-base>/references/corpus.md
- Evidence handling: <skill-base>/references/evidence.md
- Records and templates: <skill-base>/references/records.md
- Blueprint and drafting: <skill-base>/references/writing.md
- Validation and changes: <skill-base>/references/validation.md
- Learning from revisions of this skill's own drafts: <skill-base>/references/revision-learning.md
- Manuscript/SI consistency and conditional stereochemistry checks: <skill-base>/references/manuscript-si-consistency.md
- Final submission package comparison and transferable revision lessons: <skill-base>/references/submission-package.md
- Technical returns, article-type word counts and separate figure/table uploads: <skill-base>/references/technical-resubmission.md
- Official journal guidance retrieval and Word manuscript delivery: <skill-base>/references/official-guidance-and-docx.md

The script handles initialization, inventories and placeholder detection only. Extraction, scientific interpretation, citation verification, and revision-impact review require agent work and appropriate domain tools.
