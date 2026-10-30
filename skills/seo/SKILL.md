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

- `seo-search-console`: Use for Search Console exports or authorised property data, indexing, URL Inspection, CTR and query opportunities.
- `seo-traffic-diagnosis`: Use for unexplained SEO traffic drops, ranking declines or algorithm-update concerns.
- `seo-analytics-tracking`: Use for auditing GA4 or other website analytics setup and organic search measurement.
- `seo-conversion-tracking`: Use to implement or diagnose form, booking, signup or purchase measurement tied to organic search.
- `seo-site-architecture`: Use when planning site hierarchy, navigation, URL taxonomy or topic hubs before launch or a restructure.
- `seo-log-analysis`: Use for search or AI crawler behaviour in Apache, Nginx or CDN access logs.
- `seo-serp-analysis`: Use for current search results, search intent, SERP features and competing page formats.
- `seo-experiments`: Use to design and evaluate controlled SEO changes and template-wide tests.
- `seo-foundation`: Use to establish reusable business, audience and SEO context for a project.
- `seo-content-writing`: Use to draft complete SEO pages or refresh existing page copy.
- `seo-news-discover`: Use for news, publishing, Google Discover or fast-changing editorial sites.
- `seo-bing`: Use for Bing Webmaster Tools exports, Bing indexing or IndexNow planning.

Use the specialised skill's evidence rules. Do not claim that unavailable connectors, browsers or APIs exist. If live access is missing, work from uploaded HTML, crawl exports, analytics files or repository source and state the limits. No mandatory external service or subagent runtime is required. The package does not install services or run background tasks.
