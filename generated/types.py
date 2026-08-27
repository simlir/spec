"""AUTO-GENERATED — do not edit. Source: ../openapi.json."""
# Source SHA-256: ba9e3f55884039e399ac26d0c58257d5b944820d5a3d4afad92b67aca41ed503

from __future__ import annotations
from typing import Any, Literal, NotRequired, TypedDict

MarketCode = Literal["gb", "us", "de", "fr", "es", "it", "au", "ca"]

IdentifierLookupType = Literal["auto", "gtin", "mpn", "sku"]

class ApiProduct(TypedDict):
    id: str
    brand: str
    category: str
    gtin: str | None
    title: str | None
    description: str | None
    product_description: str | None
    spec: dict[str, Any] | None
    cosmetic_features: dict[str, Any] | None
    key_selling_points: list[str] | None
    use_cases: list[str] | None
    image_url: str | None
    images: list[str]
    visual: VisualSummary | None
    certifications: list[str]
    materials: list[str]
    dimensions: Dimensions | None
    weight: Weight | None
    colour: Colour
    release_year: int | None
    country_of_origin: str | None
    compatible_with: list[str]
    included_in_box: list[str]
    model_number: str | None
    retailer_sku: str | None
    product_identifiers: dict[str, Any]
    review_score: float | None
    review_count: int | None
    pricing_model: Literal["one_off", "contract_monthly", "subscription_recurring", "unknown"]
    product_condition: Literal["new", "refurbished", "used", "open_box", "unknown"]
    price: Price
    links: ProductLinks
    market: MarketCode

class VisualSummary(TypedDict):
    summary: str
    labels: list[str]
    detected_text: list[str]
    dominant_colours: list[str]

class Dimensions(TypedDict):
    value: dict[str, float]
    unit: str

class Weight(TypedDict):
    value: float
    unit: str

class Colour(TypedDict):
    primary: str | None
    family: str | None

class Price(TypedDict):
    amount: float | None
    currency: str | None
    retailer: str | None
    as_of: str | None

class ProductLinks(TypedDict):
    buy: str | None
    retailer: str | None

class SearchResult(ApiProduct):
    relevance_score: float | None

class SearchResponse(TypedDict):
    results: list[SearchResult]
    meta: SearchMeta

class SearchMeta(TypedDict):
    query: str
    mode: Literal["semantic"]
    market: MarketCode
    total_results: int
    limit: int
    offset: int
    credits_used: Literal[2]

class ImageSearchRequest(TypedDict):
    image_url: str
    query: NotRequired[str]
    market: NotRequired[MarketCode]
    gl: NotRequired[MarketCode]
    category: NotRequired[str]
    brand: NotRequired[str]
    min_price: NotRequired[float]
    max_price: NotRequired[float]
    limit: NotRequired[int]
    offset: NotRequired[int]

class ImageSearchResponse(TypedDict):
    results: list[SearchResult]
    meta: ImageSearchMeta

class ImageSearchMeta(TypedDict):
    mode: Literal["visual"]
    market: MarketCode
    query: NotRequired[str]
    total_results: int
    limit: int
    offset: int
    credits_used: Literal[3]

class ProductResponse(TypedDict):
    product: ApiProduct
    credits_used: Literal[1]

class LookupResponse(TypedDict):
    results: list[ApiProduct]
    meta: LookupMeta

class LookupMeta(TypedDict):
    identifier: str
    requested_type: IdentifierLookupType
    resolved_type: Literal["gtin", "mpn", "sku", None]
    matched_field: Literal["gtin", "model_number", "retailer_sku", None]
    market: MarketCode
    brand: str | None
    retailer: str | None
    total_results: int
    limit: int
    credits_used: Literal[1]

class Error(TypedDict):
    error: str
    message: str

class RateLimitError(TypedDict):
    error: Literal["rate_limit_exceeded"]
    limit: int
    window: str
    retry_after_seconds: int

class McpRequest(TypedDict):
    jsonrpc: Literal["2.0"]
    method: Literal["initialize", "tools/list", "tools/call"]
    params: NotRequired[dict[str, Any]]
    id: NotRequired[str | int | None]

class McpResponse(TypedDict):
    jsonrpc: Literal["2.0"]
    id: str | int | None
    result: NotRequired[Any]
    error: NotRequired[McpError]

class McpError(TypedDict):
    code: Literal[-32700, -32600, -32601, -32602, -32603, -32001, -32003, -32004]
    message: str
    data: NotRequired[Any]
