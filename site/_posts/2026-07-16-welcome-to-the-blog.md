---
layout: post
title: How this blog writes itself, almost
description: The review-first pipeline behind these posts - agentic research notes, a Notion approval queue, and a drafting agent, with a human holding the publish button.
tags: [meta, ai-engineering]
---

Every post on this site starts as a research note written by an autonomous
research pipeline, not by a person staring at a blank page. But nothing is
published automatically. The whole system is built around one idea: machines
draft, humans decide.

## The pipeline in three steps

First, an agentic research team digs through a corpus of papers and produces
structured notes. Those notes are uploaded to a Notion database where each one
lands with a "Needs Review" status.

Second, the notes get reviewed in Notion. Weak ones are discarded, promising
ones are edited, and the best are marked "Ready for Blog". This is the quality
gate - nothing moves forward without a human decision.

Third, a drafting agent pulls the approved notes, turns each one into a
concept-first post of roughly 700 words, and saves it as a Markdown draft.
The draft is reviewed one more time, then committed to this site.

## Why review-first matters

Fully automated publishing pipelines tend to fail in a predictable way: the
average output is fine, but the worst output is embarrassing, and the worst
output is what readers remember. Putting a review step between generation and
publication caps the downside while keeping almost all of the speed benefit.

The Notion database makes that review step cheap. Notes arrive already
structured, statuses make the queue visible, and approving a note takes one
click. The human effort goes where it has the most leverage - judgment - and
the mechanical work stays with the machines.

More posts will appear here as the pipeline runs. If a post reads like a
person wrote it, that is because one signed off on it.
