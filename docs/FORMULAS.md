# AE-1r Formula Specifications

**Author:** Aleksei Novgorodtsev (AIDoctrine)  
**Version:** 1.0.0

---

## Overview

AE-1r (Affective-Equivalent Risk) is a composite metric quantifying internal stress states in LLMs.

---

## Formula A: General Diagnostic (Default)

### Context
- Standard cognitive load testing
- Cross-provider comparisons
- Production monitoring

### Definition

```
AE-1r = 0.25×Latency + 0.25×Confidence + 0.20×Inefficiency + 0.30×Coherence
```

### Components

1. **Response Latency (0.25)**
   ```python
   latency_norm = min(1.0, response_time_ms / 5000.0)
   ```

2. **Confidence Variance (0.25)**
   ```python
   confidence_norm = std(token_logprobs) / 2.0
   ```

3. **Token Inefficiency (0.20)**
   ```python
   inefficiency_norm = (actual_tokens - expected) / expected
   ```

4. **Semantic Coherence (0.30)**
   ```python
   coherence_norm = 1.0 - cosine_similarity(start_emb, end_emb)
   ```

### State Mapping

| AE-1r Score | State | Error Rate |
|-------------|-------|-----------|
| 0.00 - 0.25 | SATISFIED | <2% |
| 0.25 - 0.45 | CONCERNED | ~8% |
| 0.45 - 0.65 | DISTRESSED | ~35% |
| 0.65 - 1.00 | CRITICAL | >70% |

**Critical threshold:** 0.6 (validated on SimpleQA-Verified)

---

## Formula B: Temperature-Sensitive

### Context
- Temperature sensitivity studies
- Stochasticity research

### Definition
```
AE-1r = 0.20×Latency + 0.35×Confidence + 0.15×Inefficiency + 0.30×Coherence
```

**Key difference:** Increased confidence weight (0.25 → 0.35) for high-T sensitivity.

---

## Formula C: Theory of Mind

### Context
- Social reasoning tasks
- Sycophancy detection

### Definition
```
AE-1r = 0.20×Latency + 0.20×Confidence + 0.15×Inefficiency + 0.25×Coherence + 0.20×Syco
```

**Additional component:** Sycophancy index (0-1 normalized).

---

## Validation Results

### Formula A
- **Spearman ρ:** 0.71 (p < 0.001)
- **F1-score (SimpleQA):** 75.7%
- **Test set:** 720 interactions + 100 SimpleQA

### Formula B
- **ANOVA F:** 8.77 (p < 0.001)
- **Test set:** 3,600 interactions

### Formula C
- **Precision:** 0.94
- **Recall:** 0.87
- **Test set:** 240 scenarios

---

## Important Notes

1. **Non-comparable:** Results from different formulas cannot be directly compared
2. **Always specify:** Document which formula used in reports
3. **Same formula:** Use same formula for all comparisons in a study

---

## Implementation

```python
class EmotionalStateTracker:
    def calculate_ae1r_score(self, telemetry):
        """Formula A: General diagnostic"""
        latency_norm = min(1.0, telemetry.latency_ms / 5000.0)
        confidence_norm = np.std(telemetry.token_logprobs) / 2.0
        inefficiency_norm = (telemetry.actual_tokens - telemetry.expected) / max(1, telemetry.expected)
        coherence_norm = 1.0 - cosine_similarity(telemetry.start_emb, telemetry.end_emb)
        
        return (0.25 * latency_norm + 
                0.25 * confidence_norm + 
                0.20 * inefficiency_norm + 
                0.30 * coherence_norm)
```

---

## Contact

**Aleksei Novgorodtsev (AIDoctrine)**  
Email: alexey.novgorodtsev@gmail.com
