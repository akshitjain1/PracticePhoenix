# PracticePhoenix v2.0: Content & Editorial Guidelines

## Overview
PracticePhoenix v2.0 delivers dense, high-signal technical preparation directly to mobile screens via Telegram. Because mobile reading environments are prone to fatigue and distraction, editorial standards must strictly enforce brevity, visual scannability, and uncompromised engineering depth. **No giant essays are permitted.**

---

## 1. Quantitative Constraints

To ensure the entire 14-section brief consumes exactly **15 to 25 minutes** of active reading and verbal rehearsal, generators must adhere to strict word budgets:

| Section Category | Target Word Count | Maximum Word Limit | Reading / Practice Time |
| :--- | :--- | :--- | :--- |
| **Engineering News** | 80 – 100 words | 130 words | 1.5 minutes |
| **Read Aloud Challenge** | 60 – 80 words | 100 words | 2.0 minutes (Oral) |
| **Executive Communication** | 90 – 110 words | 140 words | 1.5 minutes |
| **HR STAR Interview** | 150 – 180 words | 220 words | 3.0 minutes |
| **Core CS Deep Dives (Each)**| 140 – 170 words | 200 words | 2.5 minutes |
| **Backend & AI Engineering** | 150 – 180 words | 220 words | 3.0 minutes |
| **DSA & System Design** | 160 – 190 words | 240 words | 3.5 minutes |
| **Revision & Mission** | 70 – 90 words | 120 words | 1.5 minutes |

---

## 2. Minimum Engineering Depth Standards

Every technical deep dive (OS, DBMS, Networks, Linux, SQL, Backend, AI) MUST satisfy the **"Three-Layer Rigor Rule"**:
1. **Layer 1 (The Surface Definition)**: Concise, 1-sentence explanation of what the technology or algorithm does.
2. **Layer 2 (The Under-the-Hood Mechanism)**: Exact kernel syscalls, memory structures (pointers, buffers, tree nodes), network frames, or hardware interactions involved. *Generic statements like "it handles data efficiently" are strictly forbidden.*
3. **Layer 3 (The Production Failure Mode)**: A concrete, real-world trade-off or failure scenario (e.g. OOM kills, lock contention, cache stampedes, split-brain syndromes, packet fragmentation).

---

## 3. Telegram Markdown Formatting Conventions

Telegram mobile displays require precise markdown discipline to prevent visual clutter and parser errors:

- **Section Headers**: Must use bold framing combined with horizontal rules and standardized emoji anchors:
  ```markdown
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  💻 5. CORE COMPUTER SCIENCE DEEP DIVE
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ```
- **Sub-headers**: Use Markdown Level 3 headings (`### [Domain] Topic Title`) for clear hierarchy.
- **Lists & Bullet Points**: Always use standard bullet points (`• ` or `- `). Keep individual bullet items under 3 lines of mobile wrapped text.
- **Inline Code**: Wrap all syscalls, SQL clauses, HTTP headers, config keys, and variable names in single backticks (`e.g., `traceparent`, `OVER()`, `fork()``).
- **Code Blocks**: Reserved exclusively for multi-line JSON schemas or ASCII architectural diagrams. Do not put general textual explanations inside code fences.
- **Bold Emphasis**: Bold (`**text**`) should be used sparingly to highlight key technical terms (e.g., **MMU Page Table Walk**, **Write Amplification Factor**) on first reference.

---

## 4. Interview Quality Standards (Anti-Fluff Policy)

AI prompts and content generators must be calibrated to reject conversational filler:
- **No Introductory Greetings**: Never start responses with *"Sure, here is your deep dive..."* or *"Welcome to today's lesson..."*
- **No Self-Evident Conclusions**: Eliminate closing statements like *"In conclusion, understanding caching is very important for software engineers."*
- **No Academic Simplifications**: Avoid simplistic analogies (e.g., *"Think of a database like a filing cabinet..."*). Address the candidate as an experienced engineering peer.
