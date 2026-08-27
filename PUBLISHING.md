# Public contract publication controls

This is the release control record for the `simlir/spec` repository. It is
intentionally explicit about gates that cannot be proven from the private
application repository. The role and licensing boundary is defined by
Simlir's release process and the applicable public API and website terms at
<https://simlir.com/terms>.

## Required before publication

1. Confirm the canonical repository, assigned product/engineering/release/support/legal/platform roles, branch protection, release permissions, support route, and package/repository names.
2. The selected public contract/spec artefact scope is intended to use
   Apache-2.0, subject to final legal scope review. This does not license
   Simlir marks, API access, returned data, ingestion methods, backend code, or
   customer data; those remain governed by their applicable terms.
3. Run `npm run api:contract:release:check` from the exact source revision intended for release.
4. Run repository CI from a clean checkout, including contract tests, generated-artifact freshness, fixture validation, secret scanning, dependency checks, and package-content review.
5. Publish an immutable version tag and release notes that state the contract version, supported operations, markets, limits, image-search context behaviour, compatibility impact, and known external boundaries.
6. Deploy and verify the stable public spec URL from the exact release revision. Record the URL, revision, smoke result, and rollback/edit path.
7. Update downstream SDK, MCP, documentation, and integration work only after the release evidence is complete.

## Release integrity

The release must contain only the files listed in `release-manifest.json`. The manifest binds the OpenAPI source hash to generated types and fixture hashes. The validator rejects unexpected files, path traversal, symlinks, credential-shaped content, stale generated artifacts, and fixture/schema mismatches.

## Change management

- Patch: documentation, examples, or non-contract corrections that preserve the public shape.
- Minor: additive operations, optional fields, or non-breaking enum/documentation changes after consumer review.
- Major: removed or renamed fields, changed requiredness/nullability, changed envelopes, or incompatible operation semantics.

Every release must link back to the exact source revision and carry a short compatibility note. A failed or withdrawn release is recorded as an incident/release event; consumers are directed to the previous verified release rather than the default branch.
