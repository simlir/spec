# Simlir public API contract

This directory is the application-repository mirror for the public Simlir REST and hosted MCP contract. The published v1.0.0 contract is maintained in `simlir/spec`; this mirror contains only the public contract, generated language types, and compatibility fixtures. It must never contain application source, database exports, ingestion metadata, embeddings, credentials, or private operational configuration. The public contract artefact scope uses Apache-2.0; API access and returned data remain governed by Simlir's API/Data Licence.

## Publication decision

The recommended V1 canonical publication is a dedicated `simlir/spec` repository with versioned releases. The repository should publish the OpenAPI artifact, generated TypeScript and Python types, and the compatibility fixtures together. A separate npm or PyPI package for the spec is not required for V1; SDK packages consume a pinned spec release instead of copying fields by hand.

The canonical repository is `https://github.com/simlir/spec`. Its first
versioned release is available at
`https://github.com/simlir/spec/releases/tag/v1.0.0`. Consumers should pin that
release or an immutable commit. A separately deployed stable contract URL is not
claimed by this application repository; the repository release is the public
contract publication evidence.

## Contents

- `openapi.json` — OpenAPI 3.1 contract, version `1.0.0`.
- `LICENSE` — Apache-2.0 for the public contract artefact scope; API access and
  returned data remain governed by Simlir's applicable terms.
- `generated/types.ts` and `generated/types.py` — deterministic artifacts generated from `openapi.json`.
- `fixtures/` — representative request, response, error, rate-limit, and MCP examples.
- `release-manifest.json` — source hash, artifact hashes, publication state, and release gates.

## Image search contract

`POST /v1/search/image` always accepts a hosted HTTPS `image_url` and required
shopper market. The optional `query` field carries natural-language context
that the image cannot establish, such as product role, size, capacity,
compatibility, or intended use. Simlir combines the visual and semantic
signals, applies the same product-fit guard used by text search, retrieves up
to 50 valid candidates when available, and then applies the caller's display
limit. Image-only requests remain backward compatible. The response keeps
`meta.mode = "visual"` and echoes `meta.query` only when context was supplied.

The same contract is used by REST, hosted MCP, the SDK/framework adapters, and
the playground. A retailer demo is a hosted salesperson presentation over
that ranked result window: it may show only a small shortlist and query-linked
sales copy, but it does not use a separate image-search algorithm. Exact
identifier lookup is the deliberate exception because it is an exact-match
operation rather than semantic search.

## How this repository stays current

Do not edit this repository by hand. It is a mirror, published automatically
from the `contract/` folder of the product repository (`simlir/simlir-cloudflare`),
which holds the contract, the generator and the validators next to the code
that implements the API. A change to the contract is made there, checked there
(`npm run api:contract:release:check`), and copied here by a workflow when it
reaches `main`. Every day a second workflow compares this repository's
`openapi.json` with the one the live API serves at
<https://simlir.com/api/openapi.json> and raises an issue if they differ, so a
copy that has fallen behind is reported instead of staying quietly wrong.

## Repository verification

From the Simlir application repository, run:

```bash
npm run api:contract:release:check
```

The check verifies generated-artifact freshness, fixture/schema compatibility, release-manifest hashes, allowed package contents, and credential-shaped content. The release manifest is not a substitute for external repository, legal, deployment, or provider evidence.

## Consumer rule

Consumers must pin a versioned release or immutable commit. They must not consume the repository default branch for production builds, and they must not reimplement the contract from copied interfaces. Breaking response-shape changes require a major contract version and coordinated downstream release notes.
