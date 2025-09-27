# Obsidian Vault Overview

## Goal
- Maintain a tightly connected knowledge base that turns raw transcripts and supporting material into reusable insights for AI engineering work, content production, and community assets with consistent linking.

## Structure
![[Agents/vault_structure_overview.md]]

## CLI Query Playbook
Run these illustrative commands from the vault root (`/Users/ai-native-engineer/Documents/Vault/Vault`). Treat them as starting points—swap folders, block IDs, or section names to match the note you are auditing. `rg` (ripgrep) handles text searches; `fd` lists files and directories.

- `rg --files -g '*.md' Agents Projects Resources/Hubs Resources/Concepts Resources/Technologies` — inventory the core knowledge hubs before focusing on a subset.
- `fd -t d -d 1` — refresh your mental model of top-level folders prior to a sweep.
- `rg -n "[[Projects/AI_Native_Engineer/Skool_Overview]]"` — surface every CTA and backlink into the Skool program and confirm they still reflect current offers.
- `rg -n '#^model-compare' Resources/Processed_Transcripts` — locate transcripts citing the `model-compare` excerpt; swap the block ID for any other highlight.
- `rg -c '\[\[' Resources/Processed_Transcripts | sort -t: -k2n` — rank transcripts by outbound link count; zeros or ones flag weakly connected notes.
- `rg -n '^type: project' Projects` — list project briefs by front matter (adapt the folder to pull other note types like Areas).
- `rg -n '^type: hub' Resources/Hubs` — confirm every hub note carries canonical front matter.
- `rg -n '^type: technology' Resources/Technologies` — verify new dossiers follow the template.
- `rg -n '^## ' Resources/Concepts/LLM_Streaming_Interfaces.md` — preview a note's section outline; replace the path to inspect any concept/area quickly.
- `rg -n '[[Resources/Concepts/Local_AI_Deployment' Projects` — verify which projects already lean on a concept; reverse the search to find concepts lacking project citations.
- `fd -t f -g '*.md' Projects/AI_Native_Engineer` — group related community assets (About page, ad scripts, overview) for bulk updates.
- `rg -n 'CTA' Projects/Short_Form_Scripts.md` — spot CTA language that may need refreshing before a campaign push.
- `rg -n '^persona:' -g '*.md' Projects Areas` — confirm persona alignment is declared in front matter across execution notes.
- `rg -n 'Professional Seeking AI Mastery' Resources` — sanity-check that supporting notes speak directly to the primary persona.
- `rg -n '[[Resources/Script_Frameworks/' Projects` — ensure project plans embed the latest framework checklists.

### Multi-step investigations
- **Trace block embeds back to source**: `rg -l '#^latency' Resources/Processed_Transcripts | xargs -I{} rg -n '[[Projects/YT_Long_Form_Scripts' {}` — confirm every excerpt feeding long-form scripts resolves; swap in other block IDs and destination folders as needed.
- **Validate hub ↔ technology links**: `rg -n '\[\[Hubs/' Resources/Technologies` — ensure every technology profile references its hubs in the body.
- **Check concept coverage across folders**: `rg -l '[[Resources/Concepts/Cloud_AI_Integration_Strategy' Resources Projects Areas` — verify the cloud strategy concept appears across transcripts, projects, and areas; iterate with other concepts to spot coverage gaps.
- **Audit notes missing outbound links**: `rg -c '\[\[' Projects | awk -F: '$2==0 {print $1}'` — list project notes with no wikilinks so the connectivity agent can patch them immediately; duplicate the pattern for other directories.
- **Front-matter completeness check**: `rg --files-without-match '^---' Projects` — flag markdown files missing front matter (narrow the folder list to focus the pass).
- **Identify embedded callouts for refreshing**: `rg -n '^> ' Resources/Processed_Transcripts` — review callout-heavy transcripts and confirm they match current messaging.

## Guidelines for an AI-Assisted CLI Agent
1. **Enforce naming and metadata:** When creating notes from transcripts, craft descriptive titles and inject standard front matter (category, tags, created date) via templates.
2. **Adopt underscore filenames:** Use underscores (`_`) for every file and directory name, TitleCase each segment, and preserve acronyms (AI, LLM, RAG, etc.); replace any spaces, dashes, or alternative separators the moment you create or touch a note. Exception: raw transcript dumps in `Archives/Transcripts/Raw` may arrive with source-generated dashes—keep them to ensure the video IDs match.
3. **Anchor to the core node:** Ensure every note includes `> Core Node: [[Projects/AI_Native_Engineer]]` (add it when absent).
4. **Validate links:** Search for `[[` patterns, confirm targets exist, and flag link gaps. Track link counts to prioritise connection work.
5. **Keep folders aligned:** Apply PARA/FINVA rules; suggest moves for completed projects and ask the user to confirm before relocating notes.
6. **Refresh MOCs:** Rebuild hub notes from backlinks or folder scans so each project or area has an up-to-date map of content.
7. **Expose dashboards:** Use query blocks or tables to list open tasks, active projects, or notes by tag; refresh them when metadata changes.
8. **Audit tags and states:** Ensure workflow tags (e.g., #todo, #inprogress) are present and consistent; merge duplicates and enforce naming patterns.
9. **Maintain a single vault:** Encourage consolidation so search, linking, and automation operate on the same knowledge base.
10. **Reference the style guide:** Keep naming conventions, tag syntax, and property choices documented; flag deviations during edits.

> Core Node: [[Projects/AI_Native_Engineer]]
