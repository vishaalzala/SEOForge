# SEOForge

**Evidence-based SEO audits, content planning and practical fixes for ChatGPT-compatible skill environments.**

SEOForge is an open-source, skills-only plugin with 20 focused workflows. Use it with accessible website evidence, uploaded exports or a connected source repository to turn SEO observations into a prioritised plan.

## What is included

- `seo-audit`: Website SEO Audit.
- `seo-page`: Single Page SEO.
- `seo-technical`: Technical SEO.
- `seo-on-page`: On-page SEO.
- `seo-sitemaps`: Sitemaps and Robots.
- `seo-performance`: SEO Performance.
- `seo-content`: Content Quality.
- `seo-keywords`: Keywords and Topic Clusters.
- `seo-content-plan`: SEO Content Planning.
- `seo-schema`: Structured Data.
- `seo-local`: Local Business SEO.
- `seo-ecommerce`: E-commerce SEO.
- `seo-international`: International SEO.
- `seo-media`: Image and Video SEO.
- `seo-competitors`: Competitors and Backlinks.
- `seo-ai-search`: AI Search Visibility.
- `seo-migration`: SEO Migration and Changes.
- `seo-github`: SEO Code Implementation.
- `seo-reporting`: SEO Reports.

The `seo` router selects the appropriate workflow. Supporting files include a finding JSON schema, report template, offline HTML inventory script, package validator and evaluation scenarios.

## Example prompts

- Audit this website and state exactly which pages you checked.
- Review this uploaded HTML for technical and on-page SEO issues.
- Create a content brief from this keyword export without inventing metrics.
- Check this JSON-LD against the visible product information.
- Inspect my connected GitHub repository and prepare fixes for confirmed SEO issues.
- Build a migration checklist from these old and new URL lists.

## Installation and packaging

This repository contains `plugin.json` and portable skills in `skills/<name>/SKILL.md`. Where your ChatGPT account provides a custom-plugin archive import, create an archive using `python scripts/package.py` and import that package. Account and client support varies. Otherwise, use the skill files in a compatible environment following that client's documented installation workflow. Uploading to GitHub alone does not install or update a ChatGPT plugin.

This source export is not a public plugin-directory submission and has not been installed in a ChatGPT account. Public-directory listing requirements, publisher verification and review are separate.

## Capabilities and limits

No MCP server, third-party app binding, API credentials, hosted crawler, keyword database or scheduler is bundled. The skills use tools already available in the session. Website access, rendered-page inspection and GitHub writes require corresponding tools and permissions. Search Console, analytics, backlink and keyword metrics require supplied exports or separately connected services. Paid providers may charge independently.

Unavailable checks must be reported as not checked. Reports distinguish observed evidence from assumptions. No ranking, traffic, rich-result or AI-citation guarantees are made. AI access experiments are separate from established SEO recommendations.

## Offline helper

`python scripts/inspect_html.py path/to/page.html` extracts title, headings, meta directives, canonical links, images, links and JSON-LD syntax results as JSON. It performs no network requests, does not execute JavaScript and is not a complete SEO audit or rich-results validator.

## Development

Use Python 3.10+ and install the development dependencies with `python -m pip install -r requirements-dev.txt`. Run `python scripts/validate_package.py`, `python -m unittest discover -s tests`, and `python scripts/package.py`. The generated plugin archive excludes repository documentation and development files.

See `docs/EVALUATION.md` for manual scenarios. Automated checks verify structure and the offline helper; they do not prove end-to-end ChatGPT installation or live SEO performance.

## Publishing this repository

Unzip the source archive, create your desired GitHub repository and upload the contents of the `seoforge` folder at the repository root, including `.github`. Keep `plugin.json` and `skills/` at the root. Update the name and release notes if you choose another brand, then regenerate the plugin archive. No GitHub repository has been created by this export.

## Licence and inspiration

MIT licensed. See LICENSE. Inspired by the modular workflow idea in [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo). This package contains independently written workflows and helper code; it does not bundle that project's code, prompts, assets or runtime. No affiliation or endorsement is implied.
