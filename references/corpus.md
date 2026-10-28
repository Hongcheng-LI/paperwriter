# Corpus

Match extraction depth to the task. Start with connected reading and a source-located comparative synthesis; maintain full article/section/paragraph/sentence JSONL when requested or useful for sustained retrieval. For a focused writing decision, paragraph locators and a small pattern record suffice. Do not rebuild an existing corpus without authorization.

Input roles: target_journal, preference, background. Inspect actual content, not just filenames. Identify duplicate versions by DOI/content and retain source records; do not delete duplicates. Mark source-specific strengths: whole architecture, methods, result presentation, discussion or figure design. A different article type may be an auxiliary example, not a core model.

Use lawful local full texts, with available PDF/DOCX/OCR tools. Preserve source file, locator/page, original heading, paragraph order and sentence order. Tables, captions, footnotes and bibliography must be distinguishable from narrative. Normalize extraction artifacts conservatively and keep raw extraction alongside normalized records. Check chemical notation, math, abbreviations, hyphens and reading order using original pages. Never let automatic PASS imply scientific verification.

Records follow records.md. Functional tags are extensible: background, gap, purpose, method, observation, interpretation, comparison, limitation, hypothesis, conclusion, transition. A sentence may have several. Retrieve paragraph context and neighboring reasoning, not only matching phrases.

Extract article architecture and paragraph argument sequence before deriving reusable rhetorical patterns. Patterns describe information order, tense, degree of detail and qualification; do not produce fill-in sentence templates. Show source support and exceptions. Do not claim a whole journal has one voice based on a handful of examples.

journal_profile.md records:
- Official requirements with source and verification date, distinguished from preferences.
- Corpus scope, article types, sample limitations.
- Architecture alternatives and why one may fit the study.
- Section functions, evidence density, figures/SI practices.
- Expression patterns with article/paragraph IDs and counterexamples.
- Unverified matters and provisional_outline.md.

Preference corpus: analyze only when supplied. Identify concrete, section-specific habits; compare with journal examples so journal conventions are not mislabeled individual style. Do not use numerical style-blending weights. Skip incompatible habits and explain material conflicts. No preference input means continue with journal guidance.

## Comparative synthesis that changes the writing

The author-facing outcome is an editorial reading of the examples, not an extraction report. Organize it around the manuscript's actual sections. For each relevant section explain its reader-facing job, the recurring information sequence, a concrete source example with a locator, meaningful variation, and the resulting writing choice for this study. Keep the source audit available without letting it dominate the explanation. If project results have not yet been reviewed, make the proposed transfer conditional.

Identify a small set of primary comparators when the corpus supports this. Explain their fit by study design, contribution type and evidence organization, not merely journal, organism or topic. Different papers can model different sections. Name alternatives when their narrative differs; do not average incompatible structures into a generic outline.

Distinguish three levels: what a paper actually does; what recurs in this limited corpus; what is recommended for the current manuscript. A supplied analysis or chat transcript is useful editorial input, but is not proof that the underlying articles contain its quoted numbers, methods or claims. Label unverified examples and read original sources before treating them as verified corpus findings.

Translate habits into decisions, rather than vocabulary lists. For example, ask whether an Abstract leads with a problem or a discovery; whether an Introduction earns its rationale through a knowledge gap, a structural question or a documented extension of prior work; whether Results establish a representative case before comparing related cases; and which evidence belongs in SI. Learn clarity and reasoning from published prose without reproducing its grammatical defects.

Conditional natural-product example: where the actual papers support it, distinguish full de novo elucidation from differential comparison with an established analogue. Identify which observations establish composition, connectivity and configuration, and which differences need explicit proof. Do not turn an observed sequence of MS/NMR/correlation/configuration methods into a checklist of experiments the project must have performed. Likewise, a mechanism-rich activity paper is not an appropriate argument model for a study containing only endpoint screening.

Background papers require independently verified claim support. A stylistic example's DOI does not automatically validate any background assertion.

When the target journal is explicitly named, retrieve and preserve its official guidance according to [official-guidance-and-docx.md](official-guidance-and-docx.md) before treating submission requirements as current. Published examples inform rhetoric and architecture; they do not replace the official Aims and Scope or Guide for Authors.
