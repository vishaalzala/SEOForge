---
name: seo
description: "Use when the user asks generally for SEO help and the specific audit, content, technical or implementation workflow is unclear."
---

# SEOForge workflow router

Identify the requested outcome from the user's prompt and available evidence. If the request names a specific workflow, use its matching skill directly. For a broad audit start with seo-audit; for fixing a source repository use seo-github after confirming the findings. Read only the relevant skills. Each module is a sibling under skills/.

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

Use the specialised skill's evidence rules. Do not claim that unavailable connectors, browsers or APIs exist. If live access is missing, work from uploaded HTML, crawl exports, analytics files or repository source and state the limits. No mandatory external service or subagent runtime is required. The package does not install services or run background tasks.
