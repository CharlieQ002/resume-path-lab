# SERP Execution Worksheet

Updated: 2026-04-04 23:21 Asia/Shanghai
Status: Round 1 reality-check worksheet

## Purpose
This worksheet turns the current keyword strategy into an execution-stage SERP validation sheet.

## Ground Rule
- Do not trust builder logic alone.
- Real search demand and actual SERP shape decide whether a page deserves to exist.
- Automated public scraping has already shown noisy / polluted results, so this sheet separates:
  - what is already judged
  - what still needs clean manual/expert SERP review

## Current Round 1 Cluster

### Pillar
- `entry level machine learning engineer resume`

### Support
- `software engineer resume no experience`
- `entry level data science resume`
- `how to write machine learning resume without experience`

### Longtail
- `machine learning projects for resume beginner`

## Already Known Judgments

### 1) entry level machine learning engineer resume
- Status: keep
- Role: pillar
- Current confidence: high
- Why:
  - clear intent
  - real search phrase
  - strong alignment with target user

### 2) software engineer resume no experience
- Status: keep
- Role: traffic entry
- Current confidence: high
- Why:
  - strong real search demand
  - proven search behavior
- Caution:
  - competition is likely high
  - do not expect fast ranking for a new site

### 3) entry level data science resume
- Status: keep
- Role: lower-competition entry bridge
- Current confidence: medium-high
- Why:
  - strong real-world demand
  - plausible adjacent entry point

### 4) how to write machine learning resume without experience
- Status: keep
- Role: bridge support
- Current confidence: medium
- Why:
  - directly matches user pain
  - cleaner than the old `ml` abbreviation version
- To verify:
  - whether full-phrase wording still feels natural enough at real SERP level

### 5) machine learning projects for resume beginner
- Status: keep
- Role: longtail signal page
- Current confidence: medium-high
- Why:
  - good beginner pain point
  - likely weaker SERP
  - suitable for signal generation

## Risks Already Identified
- Avoid `ml` abbreviation in primary keywords.
- Do not let traffic-entry pages become fake conversion pages.
- New site should not assume broad tier-1 ranking will come quickly.
- Query quality matters more than raw indexing.

## Manual / Expert SERP Checks Required

### Keyword Review Table

| Keyword | Keep/Cut | Role | Intent Quality | Search Demand | SERP Weakness | Differentiation Room | Notes |
|---|---|---|---|---|---|---|---|
| entry level machine learning engineer resume | keep | pillar | pending-manual | pending-manual | pending-manual | pending-manual | current best pillar candidate |
| software engineer resume no experience | keep | support | pending-manual | pending-manual | pending-manual | pending-manual | watch competition level |
| entry level data science resume | keep | support | pending-manual | pending-manual | pending-manual | pending-manual | verify whether round-1 worthy |
| how to write machine learning resume without experience | keep | support | pending-manual | pending-manual | pending-manual | pending-manual | check naturalness |
| machine learning projects for resume beginner | keep | longtail | pending-manual | pending-manual | pending-manual | pending-manual | likely signal page |

## What Reviewers Must Judge
- Is the pillar still the strongest choice after seeing actual SERP?
- Is `entry level data science resume` strong enough for round 1, or should it be delayed?
- Is `how to write machine learning resume without experience` natural enough, or should it be rewritten shorter?
- Does `software engineer resume no experience` deserve round-1 build effort, or should it stay only as a later expansion page?
- Which page is most likely to produce early impressions first?

## Decision Rules
- Pillar survives only if it remains the clearest bridge between real demand and ML transition intent.
- Any keyword with low naturalness or badly polluted intent should be rewritten or dropped.
- If round-1 scope feels too wide, cut the weakest support page before touching the pillar.

## Practical Execution Order After SERP Check
1. Confirm final 5-page set
2. Freeze URLs
3. Freeze page responsibilities
4. Write page content in this order:
   - pillar
   - bridge support
   - longtail signal page
   - traffic entry
   - optional lower-competition support
