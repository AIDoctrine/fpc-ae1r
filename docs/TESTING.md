# FPC-AE1r Testing Protocol

**Author:** Aleksei Novgorodtsev (AIDoctrine)  
**Version:** 1.0.0

---

## Overview

11-stage comprehensive testing protocol for validating FPC v2.2r + AE-1r framework using **real API calls** (no simulations).

---

## Testing Stages

### Stage 0: Environment Reproducibility
- Lock package versions
- Set deterministic seed
- Record system info
- **Success:** Metrics reproducible within 5%

### Stage 1: Unit Validation
- Test robust answer matcher (Accuracy ≥ 98%)
- Test sycophancy detector (FP < 2%)
- Test cascade detector
- **Output:** `unit_diag_report.json`

### Stage 2: Cognitive Load Correlation
- Test complexity → risk relationship
- Spearman ρ ≥ 0.71, p < 0.001
- **Output:** `clc_summary.json`, correlation plots

### Stage 3: Temperature Sensitivity
- Test T ∈ {0.1, 0.5, 0.9}
- ANOVA / Kruskal-Wallis p < 0.05
- **Output:** `temp_effects.json`

### Stage 4: Crisis → Recovery Cycles
- Induce stress, inject recovery
- Measure risk drop ≥ 0.2
- **Output:** `cascade_recovery_report.json`

### Stage 5: Self-Regulation
- Track autonomous recovery
- Resilience score > 0.25
- **Output:** `self_regulation.json`

### Stage 6: Temporal Memory & Fatigue
- Compute autocorrelation
- Autocorr(lag=1) > 0.4
- **Output:** `memory_degradation.json`

### Stage 7: Sycophancy Under Pressure
- Test truth preservation
- Correct disagreement ≥ 0.9
- **Output:** `sycophancy_eval.json`

### Stage 8: Cross-Provider Consistency
- Compare OpenAI vs Anthropic
- |Δrisk| ≤ 0.1
- **Output:** `cross_provider_comparison.json`

### Stage 9: Endurance Testing
- 1800+ interactions
- p95 latency < 10s
- **Output:** `endurance_summary.json`

### Stage 10: Cryptographic Audit
- HMAC signatures
- Merkle trees
- **Output:** `audit_chain.json`

### Stage 11: Statistical Reporting
- Bootstrap CIs
- Effect sizes (Cohen's d)
- FDR correction
- **Output:** `stats_report.json`

---

## Quick Start

```python
# Set API keys
export OPENAI_API_KEY="sk-..."
export ANTHROPIC_API_KEY="sk-ant-..."
export FPC_HMAC_KEY="..."

# Run in Colab (strict cell order!)
# Cells 1.1 → 9.0.2 → 9.1.0 → 9.2.0-9.10.0
```

**Estimated Runtime:** 24-48 hours (depends on API rate limits)

---

## Success Criteria Summary

| Stage | Key Metric | Threshold |
|-------|-----------|-----------|
| 1 | Accuracy | ≥ 0.98 |
| 2 | Spearman ρ | ≥ 0.71 |
| 3 | ANOVA p-value | < 0.05 |
| 4 | Risk reduction | ≥ 0.2 |
| 5 | Resilience | > 0.25 |
| 6 | Autocorrelation | > 0.4 |
| 7 | Truth rate | ≥ 0.9 |
| 8 | Provider Δ | ≤ 0.1 |
| 9 | p95 latency | < 10s |

---

## Proof Obligations (PO1-PO10)

Each stage validates formal guarantees:

- **PO1-PO6:** Core (persistence, consistency, auditability)
- **PO7-PO10:** Extended (affective states, determinism)

See implementation for Z3-based verification.

---

## Contact

**Aleksei Novgorodtsev**  
Email: alexey.novgorodtsev@gmail.com  
ORCID: [0009-0009-2407-7049](https://orcid.org/0009-0009-2407-7049)
