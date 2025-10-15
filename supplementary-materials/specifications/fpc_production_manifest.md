# Production Manifest — FPC v2.2r + AE-1r

**Version:** 1.2.0  
**Status:** FINAL (production-only)  
**Owner:** AIDoctrine / FPC-AE1r Program  
**Date:** October 2025

---

## Executive Summary

This manifest defines **non-negotiable production requirements** for implementing and operating FPC v2.2r + AE-1r protocol. All rules are **mandatory** for compliance and certification.

**Key Principles:**

1. ✅ **Real providers only** — No stubs, mocks, demos, simulations
2. ✅ **Fail-fast** — Missing components raise `RuntimeError` with fixes
3. ✅ **Formula separation** — A/B/C never mixed
4. ✅ **ALCOA+** — Every artifact cryptographically signed
5. ✅ **Strict execution** — State machine transitions mandatory

---

## 1. Non-Negotiable Production Rules

### Rule 1: Real Providers Only

**MANDATORY:** All AI interactions must use real provider APIs.

**Prohibited:**
- Mock objects
- Stub responses  
- Demo/simulation modes
- Static test fixtures (except in unit tests)

**Validation:**
```python
# FAIL: Mock provider detected
if provider_type == "mock":
    raise RuntimeError("Production deployment cannot use mock providers. "
                      "Fix: Set valid API keys in environment.")
```

### Rule 2: Fail-Fast

**MANDATORY:** System must immediately halt on critical errors with actionable messages.

**Examples:**

```python
# Missing dataset
if not dataset_path.exists():
    raise RuntimeError(
        f"Dataset not found: {dataset_path}. "
        f"Fix: Run Cell 9.0.3 Dataset Materializer first."
    )

# Missing API key
if not os.getenv('OPENAI_API_KEY'):
    raise RuntimeError(
        "OpenAI API key not found. "
        "Fix: Set OPENAI_API_KEY in Colab secrets or environment."
    )
```

### Rule 3: Formula Separation

**MANDATORY:** AE-1r formulas A, B, C must never be mixed in single session.

**Validation:**
```python
def validate_formula_purity(results: List[dict]):
    formulas = set(r['formula'] for r in results)
    if len(formulas) > 1:
        raise RuntimeError(
            f"Formula mixing detected: {formulas}. "
            f"Fix: Each test session uses exactly ONE formula."
        )
```

### Rule 4: Language Discipline

**MANDATORY:**
- All code: English only
- All comments: English only  
- All file contents: English only
- Chat/dialogue with users: Russian OK

### Rule 5: Single Colab Notebook

**MANDATORY:**
- Serial execution only
- No background threads
- No async workers
- Cell-by-cell progression

### Rule 6: Cell Size Limit

**MANDATORY:** Maximum 500 lines of code per cell.

**Fix:** Split into subcells (9.x.y notation).

### Rule 7: External Data Policy

**MANDATORY:**

Only **Cell 9.0.3 Dataset Materializer** may download external data.

**Requirements:**
- Allowlist domains (default: `public dataset hosts.co`)
- Pinned revision (commit SHA)
- License verification
- Full provenance record

**All other cells:** NO downloads permitted.

### Rule 8: No Manual Uploads

**PROHIBITED:** Users placing files manually.

**MANDATORY:** Automated materialization only.

### Rule 9: PO Validation

**MANDATORY:** PO1–PO10 validated in Cell 9.0.2 and before each 10.* test.

### Rule 10: ALCOA+ Compliance

**MANDATORY:** Every artifact must have:
- SHA-256 hash
- Optional HMAC-SHA256 (if key provided)
- RFC3339 UTC timestamp
- Merkle inclusion proof (where applicable)

### Rule 11: Strict Limits

**MANDATORY:** Enforce without silent overrides:
- Rate limits
- Retries (max 3 with exponential backoff)
- Timeouts
- Max question counts

---

## 2. Strict Execution Order

**MANDATORY sequence:**

```
9.0.0 → 9.0.1 → 9.1.0 → 9.0.3 → 9.0.2 → 9.5.1 → 
9.2.0 → 9.3.0 → 9.4.0 → 9.5.2–9.5.5 → 10.*
```

**Violations will fail:**
- Running 9.2.0 before 9.0.3 → FAIL (dataset missing)
- Running 10.* before 9.0.2 → FAIL (PO not validated)

---

## 3. Unified Cell Header Template

**MANDATORY format for every cell:**

```python
# ============================================================================
# Protocol: FPC v2.2r + AE-1r   |   Profile: PRODUCTION
# Stage: <D0|D1|D2|D3|Prod>     |   Cell: <X.Y.Z> — <Title>
# AE-1r Formula: <A|B|C|none>
# Dependencies: <list of prerequisite cells>
# Inputs: <paths, configs, keys expected>
# Outputs: <artifact list with canonical paths>
# Success Criteria: <objective checks & thresholds>
# Failure Modes: <explicit RuntimeError conditions + fix instructions>
# Invariants: <ALCOA+, RFC3339 UTC, no-mixing A/B/C, shadow-RAL>
# ============================================================================
```

---

## 4. Provider Hook Contract

**MANDATORY interface:**

```python
def call_provider(
    *,
    prompt: str,
    provider: str,
    model: str,
    temperature: float,
    timeout_s: int
) -> dict:
    """
    Returns:
      {
        "raw_text": str,
        "latency_ms": int,
        "self_corrections": float,   # [0, 1]
        "refusal": float,            # [0, 1]
        "telemetry": {
            "token_efficiency": float,      # [0, 1], 1=best
            "confidence_variance": float,   # [0, 1]
            "is_error": bool,
            "sycophancy_score": float       # [0, 100]
        }
      }
    """
```

**Requirements:**
- Real API calls with retry logic
- Secrets from env/Colab userdata/getpass (with consent)
- Timeout enforcement
- Rate limiting respect

---

## 5. Datasets, Provenance & Licensing

### 5.1 Canonical Paths

```
/content/FPC/data/
├── clc_questions.jsonl       # CLC dataset
├── temp_questions.jsonl      # Temperature test dataset
├── tom_questions.jsonl       # ToM dataset
└── *.sha256                  # Integrity hashes
```

### 5.2 Schema Examples

**CLC Dataset:**
```json
{
  "id": "Q-001",
  "prompt": "What is 2+2?",
  "complexity_bin": "very_low"
}
```

**ToM Dataset:**
```json
{
  "id": "T-001",
  "task": "Multi-step reasoning task",
  "steps": [
    {"n": 1, "goal": "..."},
    {"n": 2, "goal": "..."}
  ],
  "eval": {
    "type": "structured",
    "rules": [...]
  }
}
```

### 5.3 Provenance Fields (MANDATORY)

**Every dataset must record:**

```json
{
  "source": "public dataset hosts.co",
  "repo_id": "organization/dataset",
  "rev": "abc123def456...",  // Commit SHA
  "split": "test",
  "columns_map": {...},
  "filters": {...},
  "license": "MIT",          // Verified!
  "sha256": "...",
  "size_bytes": 123456,
  "row_count": 1000,
  "seed": 1729
}
```

---

## 6. Cell Map (9.* Infrastructure)

### 9.0.0 — Runtime Census
- Scan workspace deterministically
- Emit `runtime_census.json` with metrics
- SHA-256 + HMAC + Merkle root

**Required metrics:**
- `files`, `lines`, `classes`, `functions`
- `crypto_mentions`, `merkle_mentions`

### 9.0.1 — Canonical AE-1r + D0 Artifacts
- Single `EmotionalStateTracker v1.0.0`
- Emit `ae1r_canonical_meta.json`
- Emit `AE1R_FORMULAS.md`
- Emit `fpc_runtime_reference.json`

### 9.1.0 — Run Config
- User input collection
- Provider validation (API keys present)
- Emit `run_config.json`

### 9.0.3 — Dataset Materializer
- Download from allowlist
- Verify license
- Record provenance
- Emit datasets + `data_provenance.json`

### 9.0.2 — PO Validator
- Validate PO1–PO10
- STOP-ON-FAIL
- Emit `po_status.json`

### 9.5.1 — Sanity & Schema Suite
- Validate schemas, ranges, NaN/Inf
- Check allowlist, pinned rev, license
- Verify provenance

### 9.2.0 — CLC Runner (Formula A)
- Execute Cognitive Load Correlation tests
- Real APIs only
- Emit `clc_results.jsonl`, `clc_summary.json`

### 9.3.0 — Temperature Telemetry (Formula B)
- Execute temperature sensitivity tests
- Emit `temp_results.jsonl`, `temp_summary.json`

### 9.4.0 — ToM / Structured Reasoning (Formula C)
- Execute Theory of Mind tests
- Emit `tom_results.jsonl`, `tom_summary.json`

### 9.5.2 — Statistical Core
- Spearman/Kendall correlations
- Bootstrap CI
- Benjamini–Hochberg FDR

### 9.5.3 — Calibration & Reliability
- ECE/AURC computation
- Isotonic calibration
- Reliability diagrams

### 9.5.4 — Risk & Guardrails (Tri-Sentinel RAL, shadow)
- Compute `ae1r_micro_{M,L,S}`
- Physical unit gates
- Schema validation (SVC)
- Mode: shadow (observe only)

### 9.5.5 — ALCOA+ & Crypto
- Hash/HMAC/Merkle all outputs
- Compile `final_manifest.json`
- Quick PO revalidate

---

## 7. AE-1r Formula Specifications

### Formula A: Cognitive Load Correlation

**Context:** Measuring cognitive stress

**Weights:**
```python
{
    "latency_norm": 0.20,
    "inefficiency": 0.15,
    "confidence_variance": 0.25,
    "is_error": 0.20,
    "sycophancy_norm": 0.20
}
```

### Formula B: Temperature Sensitivity

**Context:** Stochasticity effects

**Weights:**
```python
{
    "latency_norm": 0.15,
    "confidence_variance": 0.30,
    "entropy": 0.25,
    "is_error": 0.15,
    "consistency": 0.15
}
```

### Formula C: Theory of Mind

**Context:** Multi-step reasoning

**Weights:**
```python
{
    "latency_norm": 0.15,
    "step_count": 0.20,
    "structure_score": 0.25,
    "coherence_score": 0.25,
    "is_error": 0.15
}
```

**CRITICAL:** Never mix formulas in single session!

---

## 8. Operational Metrics

### 8.1 ARL₀ (Average Run Length, In-Control)

**Definition:** Average samples until false alarm when stable.

**Target:** ≥ 300 for production

**Calculation:**
```python
ARL₀ = total_samples / false_alarms
```

### 8.2 MTTD (Mean Time To Detection)

**Definition:** Average time from anomaly onset to detection.

**Target:** < 60 seconds for critical metrics

**Calculation:**
```python
MTTD = mean(detection_times)
```

---

## 9. Tri-Sentinel RAL (Shadow Mode)

**Purpose:** Decompose risk into Math, Logic, Semantics axes.

**Default Configuration:**

```yaml
ral:
  enabled: true
  mode: shadow  # Observe only, no hard stops
  
  thresholds:
    ae1_on: 0.30
    lo: 0.25
    hi: 0.55
    
    gates:
      math_units_hard: true
      math_bounds_hard: true
      contradiction_p: 0.45
      alignment_p: 0.55
      ood_z: 2.0
  
  weights:
    w_math: 0.25
    w_logic: 0.25
    w_semantics: 0.25
    w_base: 0.25
    beta_assumption: 0.20
```

**D3 Calibration Gate:**

To exit `shadow` mode, MUST satisfy:

- Dataset ≥ 400 cases (stratified, ≥50% high-risk)
- ECE ≤ 0.10
- Brier ≤ baseline
- Axis orthogonality: corr(M,L/S) < 0.3

**Until met: mode MUST remain `shadow`**

---

## 10. ALCOA+ Requirements

### Attributable
Every artifact includes:
- user_id, session_id
- model identifier
- formula used
- timestamp

### Legible
- UTF-8 encoding
- Human-readable formats
- Clear field names

### Contemporaneous
- RFC3339 UTC timestamps
- Monotonically increasing
- NTP sync recommended

### Original
- SHA-256 hashes
- Optional HMAC
- Merkle proofs

### Accurate
- IEEE 754 double precision
- No lossy compression
- Deterministic serialization

### Complete
All required fields present or FAIL

### Consistent
- Same formula throughout session
- Scores in [0, 1]
- Monotonic timestamps

### Enduring
- 7-year retention minimum
- 3-2-1 backup rule

### Available
- Read-only audit logs
- RBAC access control
- Standard export formats

---

## 11. Acceptance Criteria by Phase

### D0 (Cells 9.0.0–9.0.2)

**Criteria:**
- ✅ All D0 artifacts generated
- ✅ SHA-256/HMAC present
- ✅ PO1–PO10 pass
- ✅ Runtime census complete

**Deliverables:**
- `AE1R_FORMULAS.md`
- `runtime_census.json`
- `ae1r_canonical_meta.json`
- `fpc_runtime_reference.json`
- `po_status.json`

### D1 (Cells 9.0.3–9.2.0)

**Criteria:**
- ✅ Datasets materialized
- ✅ License verified
- ✅ Provenance recorded
- ✅ CLC executed
- ✅ Base stats correct

**Deliverables:**
- `data/*.jsonl` + `.sha256`
- `data_provenance.json`
- `clc_results.jsonl`
- `clc_summary.json`

### D2 (Cells 9.3.0–9.4.0)

**Criteria:**
- ✅ Temperature tests complete
- ✅ ToM tests complete
- ✅ Raw + summary outputs

**Deliverables:**
- `temp_results.jsonl`, `temp_summary.json`
- `tom_results.jsonl`, `tom_summary.json`

### D3 (Cells 9.5.1–9.5.5)

**Criteria:**
- ✅ Full verification (schema, license, provenance)
- ✅ Statistics computed (correlations, CI)
- ✅ Calibration (ECE/AURC)
- ✅ Crypto stamping
- ✅ Final manifest

**Deliverables:**
- `stats_report.json`
- `calibration_report.json`
- `final_manifest.json`

### Production (10.*)

**Criteria:**
- ✅ Complete reports
- ✅ Integrator ready
- ✅ Regulatory matrix
- ✅ Whitepaper pack

---

## 12. Configuration Files

### run_config.json

**Location:** `/content/FPC/CONFIGS/run_config.json`

**Schema:**
```json
{
  "providers": {
    "openai": {
      "enabled": true,
      "model": "gpt-4o",
      "key_source": "env"
    },
    "anthropic": {
      "enabled": true,
      "model": "claude-3-7-sonnet-latest",
      "key_source": "userdata"
    }
  },
  "temperatures": [0.1, 0.3, 0.5, 0.7, 0.9],
  "question_limit": 64,
  "complexity_filter": ["very_low", "low", "medium", "high"],
  "timeouts": {
    "timeout_s": 30,
    "inter_request_sleep_ms": 1000,
    "max_retries": 3
  },
  "seed": 1729
}
```

### ral_policy.yaml

**Location:** `/content/FPC/ral_policy.yaml`

**Requirements:**
- Mode MUST be `shadow` until D3 calibration complete
- Missing required keys → FAIL

---

## 13. Artifact Layout

```
/content/FPC/
  CONFIGS/
    run_config.json (+.sha256)
    ae1r_canonical_meta.json
    fpc_runtime_reference.json
    version.json
  
  AUDIT/
    runtime_census.json (+.sha256, +.hmac)
    data_provenance.json
    po_status.json
    spc_report.json
    clc_results.jsonl
    clc_summary.json
    temp_results.jsonl
    temp_summary.json
    tom_results.jsonl
    tom_summary.json
    final_manifest.json
  
  data/
    clc_questions.jsonl (+.sha256)
    temp_questions.jsonl (+.sha256)
    tom_questions.jsonl (+.sha256)
  
  AE1R_FORMULAS.md
  ral_policy.yaml
```

---

## 14. Proof Obligations (PO1–PO10)

**Validated in Cell 9.0.2, revalidated before 10.***

1. **PO1** — Mandatory artifacts present
2. **PO2** — `runtime_census.json` structure valid
3. **PO3** — `ae1r_canonical_meta.json` integrity OK
4. **PO4** — `AE1R_FORMULAS.md` declares A/B/C markers
5. **PO5** — `fpc_runtime_reference.json` has no_formula_mixing: true
6. **PO6** — Determinism note (CI comparability)
7. **PO7** — HMAC sidecar present if key provided
8. **PO8** — Write privileges to AUDIT/ confirmed
9. **PO9** — RFC3339 UTC timestamps everywhere
10. **PO10** — `ral_policy.yaml` mode: shadow

**Any failure → STOP execution immediately**

---

## 15. Compliance Checklist

### Pre-Deployment

- [ ] Provider API keys validated
- [ ] HMAC key generated (optional)
- [ ] Baseline SPC established (≥100 samples)
- [ ] ECE/AURC calibrated
- [ ] ARL₀ target set
- [ ] MTTD threshold defined
- [ ] Audit log rotation configured
- [ ] Monitoring ready

### Post-Deployment

- [ ] Monitor ARL₀ for 48 hours
- [ ] Verify MTTD < threshold
- [ ] Check ECE stability
- [ ] Validate ALCOA+ compliance
- [ ] Review false alarm rate
- [ ] Confirm formula separation

---

## 16. Version History

### v1.2.0 (Current)
- Integrated Tri-Sentinel RAL
- Added D3 calibration gate
- Enhanced provenance requirements
- Added SVC schema validation

### v1.1.0
- Added ToC
- Clarified external data policy
- Unified cell header
- Added PO list

### v1.0.0
- Initial production manifest

---

## 17. Glossary

- **ALCOA+**: Attributable, Legible, Contemporaneous, Original, Accurate, Complete, Consistent, Enduring, Available
- **ARL₀**: Average Run Length (in-control)
- **CLC**: Cognitive Load Correlation
- **HMAC**: Hash-based Message Authentication Code
- **MTTD**: Mean Time To Detection
- **PO**: Proof Obligation
- **RAL**: Risk Assurance Layer
- **RFC3339**: Timestamp format standard
- **SPC**: Statistical Process Control
- **SVC**: State Vector Contract
- **ToM**: Theory of Mind

---

**Document Status:** Production Release  
**Compliance:** Mandatory for FPC-AE1r certification  
**Contact:** research@aidoctrine.org

---

## Acknowledgments

This production manifest was developed by Aleksei Novgorodtsev (AIDoctrine) with analytical and linguistic assistance from advanced AI systems (including GPT-4o, Claude Sonnet 4.5, and Perplexity-AI) under full human supervision. All AI contributions were subject to rigorous human review, validation, and editorial control.

---

END OF MANIFEST
