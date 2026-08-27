/* AUTO-GENERATED — do not edit. Source: ../openapi.json */
/* Source SHA-256: ba9e3f55884039e399ac26d0c58257d5b944820d5a3d4afad92b67aca41ed503 */

export type MarketCode = "gb" | "us" | "de" | "fr" | "es" | "it" | "au" | "ca";

export type IdentifierLookupType = "auto" | "gtin" | "mpn" | "sku";

export type ApiProduct = {
  id: string;
  brand: string;
  category: string;
  gtin: string | null;
  title: string | null;
  description: string | null;
  product_description: string | null;
  spec: Record<string, unknown> | null;
  cosmetic_features: Record<string, unknown> | null;
  key_selling_points: string[] | null;
  use_cases: string[] | null;
  image_url: string | null;
  images: string[];
  visual: VisualSummary | null;
  certifications: string[];
  materials: string[];
  dimensions: Dimensions | null;
  weight: Weight | null;
  colour: Colour;
  release_year: number | null;
  country_of_origin: string | null;
  compatible_with: string[];
  included_in_box: string[];
  model_number: string | null;
  retailer_sku: string | null;
  product_identifiers: Record<string, unknown>;
  review_score: number | null;
  review_count: number | null;
  pricing_model: "one_off" | "contract_monthly" | "subscription_recurring" | "unknown";
  product_condition: "new" | "refurbished" | "used" | "open_box" | "unknown";
  price: Price;
  links: ProductLinks;
  market: MarketCode;
};

export type VisualSummary = {
  summary: string;
  labels: string[];
  detected_text: string[];
  dominant_colours: string[];
};

export type Dimensions = {
  value: Record<string, number>;
  unit: string;
};

export type Weight = {
  value: number;
  unit: string;
};

export type Colour = {
  primary: string | null;
  family: string | null;
};

export type Price = {
  amount: number | null;
  currency: string | null;
  retailer: string | null;
  as_of: string | null;
};

export type ProductLinks = {
  buy: string | null;
  retailer: string | null;
};

export type SearchResult = ApiProduct & {
  relevance_score: number | null;
};

export type SearchResponse = {
  results: SearchResult[];
  meta: SearchMeta;
};

export type SearchMeta = {
  query: string;
  mode: "semantic";
  market: MarketCode;
  total_results: number;
  limit: number;
  offset: number;
  credits_used: 2;
};

// JSON Schema requires one of the declared alternatives.
export type ImageSearchRequest = {
  image_url: string;
  query?: string;
  market?: MarketCode;
  gl?: MarketCode;
  category?: string;
  brand?: string;
  min_price?: number;
  max_price?: number;
  limit?: number;
  offset?: number;
};

export type ImageSearchResponse = {
  results: SearchResult[];
  meta: ImageSearchMeta;
};

export type ImageSearchMeta = {
  mode: "visual";
  market: MarketCode;
  query?: string;
  total_results: number;
  limit: number;
  offset: number;
  credits_used: 3;
};

export type ProductResponse = {
  product: ApiProduct;
  credits_used: 1;
};

export type LookupResponse = {
  results: ApiProduct[];
  meta: LookupMeta;
};

export type LookupMeta = {
  identifier: string;
  requested_type: IdentifierLookupType;
  resolved_type: "gtin" | "mpn" | "sku" | null;
  matched_field: "gtin" | "model_number" | "retailer_sku" | null;
  market: MarketCode;
  brand: string | null;
  retailer: string | null;
  total_results: number;
  limit: number;
  credits_used: 1;
};

export type Error = {
  error: string;
  message: string;
};

export type RateLimitError = {
  error: "rate_limit_exceeded";
  limit: number;
  window: string;
  retry_after_seconds: number;
};

export type McpRequest = {
  jsonrpc: "2.0";
  method: "initialize" | "tools/list" | "tools/call";
  params?: Record<string, unknown>;
  id?: string | number | null;
};

export type McpResponse = {
  jsonrpc: "2.0";
  id: string | number | null;
  result?: unknown;
  error?: McpError;
};

export type McpError = {
  code: -32700 | -32600 | -32601 | -32602 | -32603 | -32001 | -32003 | -32004;
  message: string;
  data?: unknown;
};
