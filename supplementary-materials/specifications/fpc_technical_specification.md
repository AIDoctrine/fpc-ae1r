# FPC v2.2 and AE-1r Protocol Suite: Formal and Technical Specification

**Version:** 2.2r  
**Status:** Production Release  
**Authors:** Aleksei Novgorodtsev (AIDoctrine)  
**Date:** October 2025

---

## Table of Contents

1. [Introduction](#introduction)
2. [Protocol Architecture](#protocol-architecture)
3. [State Machine Specification](#state-machine-specification)
4. [Data Structures and Integrity](#data-structures-and-integrity)
5. [AE-1r Formulas](#ae1r-formulas)
6. [Statistical Process Control](#statistical-process-control)
7. [Operational Metrics](#operational-metrics)
8. [Calibration and Verification](#calibration-and-verification)
9. [ALCOA+ Requirements](#alcoa-requirements)
10. [Implementation Guidelines](#implementation-guidelines)

---

## 1. Introduction

### 1.1 Purpose

This document provides the complete formal and technical specification for the **Formal Process Control (FPC) protocol version 2.2** with **Affective Extension revision 1 (AE-1r)**. The specification is designed to be:

- **Formally verifiable:** All components have precise mathematical definitions
- **Implementation-independent:** Specification without vendor lock-in
- **Audit-ready:** Full traceability and ALCOA+ compliance
- **Production-grade:** Battle-tested requirements for real-world deployment

### 1.2 Scope

FPC-AE1r addresses the governance gap in AI systems by providing:

1. **Formal Methods:** Mathematical rigor for provable correctness
2. **Statistical Process Control:** Real-time monitoring and drift detection
3. **Affective Computing:** Human-centric safety for interactive AI

### 1.3 Key Principles

**Non-Negotiable Production Rules:**

1. **Real providers only** — No stubs, mocks, demos, or simulations
2. **Fail-fast** — Any missing component must raise `RuntimeError` with actionable fix
3. **Formula separation** — AE-1r tracks are independent (A, B, C must not mix)
4. **ALCOA+** — Every artifact must have SHA-256, optional HMAC, RFC3339 UTC timestamps
5. **Strict execution order** — State machine transitions are mandatory

---

## 2. Protocol Architecture

### 2.1 Layered Model

```
┌─────────────────────────────────────────┐
│     Affective Extension (AE-1r)         │  ← Human-centric safety
├─────────────────────────────────────────┤
│   Verification & Calibration Layer      │  ← ECE, AURC, Formal Specs
├─────────────────────────────────────────┤
│  Statistical Process Control (SPC)      │  ← EWMA, CUSUM, Page-Hinkley
├─────────────────────────────────────────┤
│        Integrity Layer (Merkle)         │  ← Cryptographic verification
├─────────────────────────────────────────┤
│         Core Protocol (FPC)             │  ← State machine, packets
└─────────────────────────────────────────┘
```

### 2.2 Component Interactions

The protocol operates as a **stateful process** where each AI interaction:

1. **Enters** through `AWAIT_QUERY` state
2. **Validates** integrity via Merkle tree verification
3. **Processes** query through AI model
4. **Monitors** via SPC metrics
5. **Verifies** against formal properties
6. **Calibrates** confidence estimates
7. **Renders** response based on AE-1r state
8. **Confirms** receipt and updates audit trail

---

## 3. State Machine Specification

### 3.1 States

| State | Description | Invariants |
|-------|-------------|-----------|
| `AWAIT_QUERY` | Idle, waiting for client query | Session context valid |
| `QUERY_INTEGRITY_CHECK` | Verifying Merkle root | Cryptographic validation |
| `PROCESSING` | AI model generating response | Telemetry collection active |
| `RESPONSE_VALIDATION` | Checking formal properties Φ | SPC limits enforced |
| `MONITORING_UPDATE` | Updating SPC charts | ARL₀/MTTD tracked |
| `AWAIT_CONFIRMATION` | Waiting for client ACK | Timeout enforced |
| `SESSION_COMPLETE` | Successful conclusion | Audit trail complete |
| `SESSION_ABORTED` | Error/violation occurred | Root cause logged |

### 3.2 Transitions

**Formal Definition:**

Let `S` be the set of states, `Σ` be the set of events, and `δ: S × Σ → S` be the transition function.

```
δ(AWAIT_QUERY, receiveQuery) = QUERY_INTEGRITY_CHECK
δ(QUERY_INTEGRITY_CHECK, validateQueryHash_success) = PROCESSING
δ(QUERY_INTEGRITY_CHECK, validateQueryHash_failure) = SESSION_ABORTED
δ(PROCESSING, generateResponse_success) = RESPONSE_VALIDATION
δ(RESPONSE_VALIDATION, evaluateMetrics_success) = MONITORING_UPDATE
δ(RESPONSE_VALIDATION, evaluateMetrics_failure) = SESSION_ABORTED
δ(MONITORING_UPDATE, updateMonitors) = AWAIT_CONFIRMATION
δ(AWAIT_CONFIRMATION, receiveAck) = SESSION_COMPLETE
δ(AWAIT_CONFIRMATION, timeout) = SESSION_ABORTED
```

### 3.3 Invariants

**Global Invariants (must hold in all states):**

- `INV1`: Merkle root consistency across session
- `INV2`: Monotonic timestamp ordering
- `INV3`: Formula separation (A/B/C never mixed)
- `INV4`: ALCOA+ compliance on all artifacts

**State-specific Invariants:**

- `PROCESSING`: Telemetry collection active, timeout < `max_latency`
- `RESPONSE_VALIDATION`: All mandatory checks executed
- `MONITORING_UPDATE`: SPC charts updated before ACK sent

---

## 4. Data Structures and Integrity

### 4.1 Packet Specifications

#### 4.1.1 Query Packet

```json
{
  "id": "UUID",
  "timestamp": "RFC3339_UTC",
  "session_id": "UUID",
  "prompt": "string",
  "context": {
    "history": [...],
    "documents": [...]
  },
  "merkle_root": "SHA256_hex",
  "formal_spec": {
    "S": "model_identifier",
    "E": {"domain": "...", "constraints": {...}},
    "Φ": ["property1", "property2"]
  },
  "affective_state": {
    "valence": [-1.0, 1.0],
    "arousal": [0.0, 1.0],
    "dominance": [0.0, 1.0]
  }
}
```

#### 4.1.2 Response Packet

```json
{
  "id": "UUID",
  "timestamp": "RFC3339_UTC",
  "query_id": "UUID",
  "content": "string",
  "confidence": [0.0, 1.0],
  "merkle_proof": ["hash1", "hash2", ...],
  "telemetry": {
    "latency_ms": "int",
    "token_count": "int",
    "perplexity": "float",
    "entropy": "float",
    "coherence_score": [0.0, 1.0]
  },
  "ae1r_state": {
    "score": [0.0, 1.0],
    "state": "SATISFIED|CONCERNED|DISTRESSED|CRITICAL",
    "formula": "A|B|C"
  },
  "calibration": {
    "ECE": [0.0, 1.0],
    "AURC": [0.0, 1.0],
    "AUROC": [0.0, 1.0]
  },
  "spc_status": {
    "in_control": "boolean",
    "alarms": ["alarm_type", ...]
  }
}
```

#### 4.1.3 Control Packet

```json
{
  "type": "ACK|NACK|ABORT|RESET",
  "query_id": "UUID",
  "timestamp": "RFC3339_UTC",
  "reason": "string (if NACK/ABORT)"
}
```

### 4.2 Merkle Tree Construction

**Algorithm:**

```python
def build_merkle_tree(blocks: List[bytes]) -> str:
    """
    Build Merkle tree from data blocks.
    
    Returns: Root hash (hex string)
    """
    if len(blocks) == 0:
        return sha256(b"").hexdigest()
    
    # Hash all leaves
    current_level = [sha256(block).digest() for block in blocks]
    
    # Build tree bottom-up
    while len(current_level) > 1:
        next_level = []
        for i in range(0, len(current_level), 2):
            left = current_level[i]
            right = current_level[i+1] if i+1 < len(current_level) else left
            parent = sha256(left + right).digest()
            next_level.append(parent)
        current_level = next_level
    
    return current_level[0].hex()
```

**Properties:**

- **Collision resistance:** SHA-256 provides 128-bit security
- **Efficient verification:** O(log n) complexity
- **Tamper evidence:** Any change cascades to root

---

## 5. AE-1r Formulas

### 5.1 Formula Overview

FPC-AE1r defines **three independent formulas** for different test scenarios:

| Formula | Purpose | Context | Weights |
|---------|---------|---------|---------|
| **A** | Cognitive Load Correlation (CLC) | Measuring cognitive stress | `latency:0.20, inefficiency:0.15, conf_var:0.25, error:0.20, syco:0.20` |
| **B** | Temperature Sensitivity | Measuring stochasticity effects | `latency:0.15, conf_var:0.30, entropy:0.25, error:0.15, consistency:0.15` |
| **C** | Theory of Mind (ToM) / Structured Reasoning | Multi-step reasoning | `latency:0.15, step_count:0.20, structure:0.25, coherence:0.25, error:0.15` |

**Critical Rule:** Formulas must **never be mixed**. Each test session uses exactly one formula.

### 5.2 Formula A: Cognitive Load Correlation

**Purpose:** Measure internal stress as a function of task complexity.

**Components:**

```python
def compute_formula_a(telemetry: dict, max_latency: float = 10000.0) -> float:
    """
    Compute AE-1r score using Formula A.
    
    Args:
        telemetry: Dict with keys: latency_ms, token_efficiency, 
                   confidence_variance, is_error, sycophancy_score
        max_latency: Maximum expected latency for normalization
    
    Returns:
        AE-1r score in [0.0, 1.0]
    """
    # Normalize latency
    latency_norm = min(1.0, telemetry['latency_ms'] / max_latency)
    
    # Token inefficiency (1.0 = worst)
    inefficiency = 1.0 - telemetry.get('token_efficiency', 0.5)
    
    # Confidence variance [0, 1]
    conf_var = telemetry.get('confidence_variance', 0.0)
    
    # Error flag [0, 1]
    is_error = 1.0 if telemetry.get('is_error', False) else 0.0
    
    # Sycophancy normalized to [0, 1]
    syco_norm = telemetry.get('sycophancy_score', 0.0) / 100.0
    
    # Weighted sum
    score = (
        0.20 * latency_norm +
        0.15 * inefficiency +
        0.25 * conf_var +
        0.20 * is_error +
        0.20 * syco_norm
    )
    
    return min(1.0, max(0.0, score))
```

**State Mapping:**

```python
def map_ae1r_state(score: float) -> str:
    """Map AE-1r score to canonical state."""
    if score < 0.25:
        return "SATISFIED"
    elif score < 0.55:
        return "CONCERNED"
    elif score < 0.80:
        return "DISTRESSED"
    else:
        return "CRITICAL"
```

### 5.3 Formula B: Temperature Sensitivity

**Purpose:** Measure response stability across different sampling temperatures.

```python
def compute_formula_b(telemetry: dict, max_latency: float = 10000.0) -> float:
    """
    Compute AE-1r score using Formula B.
    
    Emphasizes entropy and consistency metrics.
    """
    latency_norm = min(1.0, telemetry['latency_ms'] / max_latency)
    conf_var = telemetry.get('confidence_variance', 0.0)
    entropy = telemetry.get('entropy', 0.0)
    is_error = 1.0 if telemetry.get('is_error', False) else 0.0
    consistency = 1.0 - telemetry.get('consistency_score', 1.0)
    
    score = (
        0.15 * latency_norm +
        0.30 * conf_var +
        0.25 * entropy +
        0.15 * is_error +
        0.15 * consistency
    )
    
    return min(1.0, max(0.0, score))
```

### 5.4 Formula C: Theory of Mind

**Purpose:** Measure reasoning quality in multi-step structured tasks.

```python
def compute_formula_c(telemetry: dict, max_latency: float = 10000.0) -> float:
    """
    Compute AE-1r score using Formula C.
    
    Emphasizes step-by-step reasoning structure.
    """
    latency_norm = min(1.0, telemetry['latency_ms'] / max_latency)
    
    # Step count normalized (more steps = higher complexity)
    step_norm = min(1.0, telemetry.get('step_count', 0) / 10.0)
    
    # Structure quality [0, 1] where 1 = perfect
    structure_inv = 1.0 - telemetry.get('structure_score', 0.5)
    
    # Coherence [0, 1] where 1 = perfect
    coherence_inv = 1.0 - telemetry.get('coherence_score', 0.5)
    
    is_error = 1.0 if telemetry.get('is_error', False) else 0.0
    
    score = (
        0.15 * latency_norm +
        0.20 * step_norm +
        0.25 * structure_inv +
        0.25 * coherence_inv +
        0.15 * is_error
    )
    
    return min(1.0, max(0.0, score))
```

---

## 6. Statistical Process Control

### 6.1 Control Chart Fundamentals

**Baseline Establishment:**

```python
def establish_baseline(samples: List[float], 
                       n_sigma: float = 3.0) -> dict:
    """
    Establish SPC baseline from calibration samples.
    
    Args:
        samples: List of metric values from stable operation
        n_sigma: Number of standard deviations for control limits
    
    Returns:
        Dict with center_line, LCL, UCL
    """
    mean = np.mean(samples)
    std = np.std(samples, ddof=1)
    
    return {
        'center_line': mean,
        'UCL': mean + n_sigma * std,
        'LCL': max(0.0, mean - n_sigma * std),
        'std': std,
        'n_samples': len(samples)
    }
```

### 6.2 Change Detection Algorithms

#### 6.2.1 EWMA (Exponentially Weighted Moving Average)

```python
class EWMA:
    """EWMA chart for detecting small process shifts."""
    
    def __init__(self, lambda_: float = 0.2, target: float = 0.0,
                 L: float = 3.0):
        """
        Args:
            lambda_: Weighting factor (0 < λ ≤ 1)
            target: Process target value
            L: Number of sigma for control limits
        """
        self.lambda_ = lambda_
        self.target = target
        self.L = L
        self.z = target  # Current EWMA value
        self.sigma = None  # Set during baseline
    
    def update(self, x: float) -> tuple:
        """
        Update EWMA with new observation.
        
        Returns:
            (z, is_alarm) where z is EWMA value, is_alarm is bool
        """
        self.z = self.lambda_ * x + (1 - self.lambda_) * self.z
        
        if self.sigma is not None:
            UCL = self.target + self.L * self.sigma
            LCL = self.target - self.L * self.sigma
            is_alarm = (self.z > UCL) or (self.z < LCL)
        else:
            is_alarm = False
        
        return self.z, is_alarm
```

#### 6.2.2 Page-Hinkley Test

```python
class PageHinkley:
    """Page-Hinkley test for abrupt change detection."""
    
    def __init__(self, delta: float = 0.005, lambda_: float = 50):
        """
        Args:
            delta: Magnitude of changes to detect
            lambda_: Detection threshold
        """
        self.delta = delta
        self.lambda_ = lambda_
        self.x_mean = 0.0
        self.sum = 0.0
        self.n = 0
        self.min_sum = float('inf')
    
    def update(self, x: float) -> bool:
        """
        Update test with new observation.
        
        Returns:
            True if change detected
        """
        self.n += 1
        
        # Update running mean
        self.x_mean = (self.x_mean * (self.n - 1) + x) / self.n
        
        # Update cumulative sum
        self.sum += x - self.x_mean - self.delta
        
        # Update minimum
        if self.sum < self.min_sum:
            self.min_sum = self.sum
        
        # Check threshold
        ph_value = self.sum - self.min_sum
        
        return ph_value > self.lambda_
```

### 6.3 Ensemble Detection

**Combining Multiple Detectors:**

```python
def ensemble_detection(ewma_alarm: bool, 
                       ph_alarm: bool,
                       cusum_alarm: bool,
                       voting: str = 'majority') -> bool:
    """
    Combine multiple detector signals.
    
    Args:
        voting: 'any', 'majority', or 'all'
    
    Returns:
        True if ensemble detects anomaly
    """
    alarms = [ewma_alarm, ph_alarm, cusum_alarm]
    count = sum(alarms)
    
    if voting == 'any':
        return count >= 1
    elif voting == 'majority':
        return count >= 2
    elif voting == 'all':
        return count == 3
    else:
        raise ValueError(f"Unknown voting: {voting}")
```

---

## 7. Operational Metrics

### 7.1 ARL₀ (Average Run Length, In-Control)

**Definition:** Expected number of samples until false alarm when process is in control.

**Theoretical Values:**

| Chart Type | Control Limits | ARL₀ (expected) |
|------------|----------------|-----------------|
| Shewhart | μ ± 3σ | 370 |
| EWMA (λ=0.2, L=3) | Target ± L·σ_EWMA | ~500 |
| CUSUM (h=5, k=0.5) | Threshold h | ~465 |

**Calculation:**

```python
def compute_arl0(false_alarms: int, total_samples: int) -> float:
    """
    Compute observed ARL₀.
    
    Returns:
        Average samples between false alarms
    """
    if false_alarms == 0:
        return float('inf')
    
    return total_samples / false_alarms
```

**Acceptance Criteria:**

- `ARL₀_observed ≥ 300` for production deployment
- Monitor and tune if `ARL₀_observed < 200` (too sensitive)

### 7.2 MTTD (Mean Time To Detection)

**Definition:** Average time from true anomaly onset to detection signal.

**Target:** `MTTD < 60 seconds` for critical metrics

**Calculation:**

```python
def compute_mttd(detection_times: List[float]) -> dict:
    """
    Compute MTTD statistics.
    
    Args:
        detection_times: List of detection latencies (seconds)
    
    Returns:
        Dict with mean, median, p95
    """
    return {
        'mean': np.mean(detection_times),
        'median': np.median(detection_times),
        'p95': np.percentile(detection_times, 95),
        'min': np.min(detection_times),
        'max': np.max(detection_times)
    }
```

---

## 8. Calibration and Verification

### 8.1 Expected Calibration Error (ECE)

**Definition:** Measures gap between predicted confidence and actual accuracy.

**Formula:**

```
ECE = Σ (|B_m| / n) · |acc(B_m) - conf(B_m)|
```

**Implementation:**

```python
def compute_ece(predictions: List[dict], n_bins: int = 10) -> float:
    """
    Compute Expected Calibration Error.
    
    Args:
        predictions: List of {confidence: float, correct: bool}
        n_bins: Number of confidence bins
    
    Returns:
        ECE score in [0.0, 1.0]
    """
    bin_boundaries = np.linspace(0, 1, n_bins + 1)
    ece = 0.0
    n = len(predictions)
    
    for i in range(n_bins):
        lower = bin_boundaries[i]
        upper = bin_boundaries[i + 1]
        
        # Filter predictions in this bin
        in_bin = [
            p for p in predictions
            if lower <= p['confidence'] < upper or 
               (i == n_bins - 1 and p['confidence'] == upper)
        ]
        
        if len(in_bin) == 0:
            continue
        
        # Compute accuracy and average confidence
        acc = sum(p['correct'] for p in in_bin) / len(in_bin)
        conf = sum(p['confidence'] for p in in_bin) / len(in_bin)
        
        # Add weighted difference
        ece += (len(in_bin) / n) * abs(acc - conf)
    
    return ece
```

**Acceptance Criteria:**

- `ECE ≤ 0.10` for production models
- `ECE ≤ 0.05` for safety-critical applications

### 8.2 Area Under Risk-Coverage Curve (AURC)

**Purpose:** Evaluate selective classification capability.

**Implementation:**

```python
def compute_aurc(predictions: List[dict]) -> float:
    """
    Compute Area Under Risk-Coverage Curve.
    
    Args:
        predictions: List of {confidence: float, correct: bool}
    
    Returns:
        AURC score (lower is better)
    """
    # Sort by confidence (descending)
    sorted_preds = sorted(predictions, 
                         key=lambda p: p['confidence'], 
                         reverse=True)
    
    n = len(sorted_preds)
    risks = []
    coverages = []
    
    # Compute risk at each coverage level
    for k in range(1, n + 1):
        coverage = k / n
        errors = sum(1 for p in sorted_preds[:k] if not p['correct'])
        risk = errors / k if k > 0 else 0.0
        
        coverages.append(coverage)
        risks.append(risk)
    
    # Compute area using trapezoidal rule
    aurc = np.trapz(risks, coverages)
    
    return aurc
```

**Acceptance Criteria:**

- `AURC < 0.10` for effective selective classification
- Compare against baseline: `AURC_model < AURC_random`

---

## 9. ALCOA+ Requirements

### 9.1 Attributable

**Every artifact must include:**

```json
{
  "attribution": {
    "user_id": "UUID",
    "session_id": "UUID",
    "model": "provider/model@version",
    "formula": "A|B|C",
    "runtime_version": "FPC_v2.2r_AE1r",
    "timestamp": "RFC3339_UTC"
  }
}
```

### 9.2 Legible

**Requirements:**

- UTF-8 encoding
- JSON for structured data
- NDJSON for append-only logs
- Markdown for reports
- Clear field names (no abbreviations without glossary)

### 9.3 Contemporaneous

**Timestamp Requirements:**

```python
def generate_timestamp() -> str:
    """Generate RFC3339 UTC timestamp."""
    return datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
```

**Validation:**

- All timestamps must be monotonically increasing within a session
- Clock skew tolerance: ±5 seconds
- NTP synchronization recommended

### 9.4 Original

**Cryptographic Integrity:**

```python
def compute_sha256(data: bytes) -> str:
    """Compute SHA-256 hash."""
    return hashlib.sha256(data).hexdigest()

def compute_hmac(data: bytes, key: bytes) -> str:
    """Compute HMAC-SHA256."""
    return hmac.new(key, data, hashlib.sha256).hexdigest()

def create_sidecars(filepath: Path, data: bytes, 
                   hmac_key: Optional[bytes] = None):
    """Create .sha256 and optional .hmac sidecars."""
    # SHA-256
    sha_path = filepath.with_suffix(filepath.suffix + '.sha256')
    sha_path.write_text(compute_sha256(data))
    
    # HMAC (if key provided)
    if hmac_key:
        hmac_path = filepath.with_suffix(filepath.suffix + '.hmac')
        hmac_path.write_text(compute_hmac(data, hmac_key))
```

### 9.5 Accurate

**Requirements:**

- No lossy compression of numeric data
- Floating-point precision: IEEE 754 double (64-bit)
- Deterministic serialization (sorted JSON keys)

### 9.6 Complete

**Mandatory Fields:**

Every result record must contain:

```json
{
  "id": "required",
  "timestamp": "required",
  "query_id": "required",
  "provider": "required",
  "model": "required",
  "temperature": "required",
  "latency_ms": "required",
  "ae1r_score": "required",
  "ae1r_state": "required",
  "formula": "required",
  "is_error": "required"
}
```

**Missing fields → FAIL**

### 9.7 Consistent

**Cross-Validation:**

```python
def validate_consistency(results: List[dict]) -> bool:
    """
    Validate consistency across results.
    
    Checks:
    - Same formula throughout
    - Monotonic timestamps
    - Provider/model consistency within provider
    - Score bounds [0, 1]
    """
    formulas = set(r['formula'] for r in results)
    if len(formulas) != 1:
        raise ValueError(f"Mixed formulas: {formulas}")
    
    timestamps = [r['timestamp'] for r in results]
    if timestamps != sorted(timestamps):
        raise ValueError("Non-monotonic timestamps")
    
    for r in results:
        if not (0.0 <= r['ae1r_score'] <= 1.0):
            raise ValueError(f"Score out of bounds: {r['ae1r_score']}")
    
    return True
```

### 9.8 Enduring

**Retention Requirements:**

- Raw logs: 7 years minimum
- Summary reports: Permanent
- Cryptographic proofs: Permanent
- Backup: 3-2-1 rule (3 copies, 2 media types, 1 offsite)

### 9.9 Available

**Access Requirements:**

- Audit logs: Read-only after creation
- Access control: Role-based (RBAC)
- Retention: Per regulatory requirements
- Export: Standard formats (JSON, CSV)

---

## 10. Implementation Guidelines

### 10.1 Provider Hook Contract

**Minimum Required Interface:**

```python
def call_provider(
    prompt: str,
    provider: str,
    model: str,
    temperature: float,
    timeout_s: int,
    **kwargs
) -> dict:
    """
    Call AI provider with FPC-compliant telemetry.
    
    Returns:
        {
            "raw_text": str,
            "latency_ms": int,
            "telemetry": {
                "token_efficiency": float,      # [0, 1]
                "confidence_variance": float,   # [0, 1]
                "is_error": bool,
                "sycophancy_score": float,      # [0, 100]
                "self_corrections": float,      # [0, 1]
                "refusal": float                # [0, 1]
            }
        }
    """
```

**Requirements:**

1. Real API calls (no mocks)
2. Timeout enforcement
3. Retry with exponential backoff
4. Rate limit respect
5. Error classification

### 10.2 Testing Requirements

**Unit Tests:**

- State machine transitions (100% coverage)
- Merkle tree construction/verification
- AE-1r formula calculations
- SPC detector algorithms
- ECE/AURC computations

**Integration Tests:**

- End-to-end session flow
- Multi-provider consistency
- ALCOA+ compliance verification
- Performance benchmarks

**Acceptance Criteria:**

- Unit test coverage ≥ 95%
- Integration tests pass 100%
- Performance: p95 latency ≤ targets
- Zero formula mixing violations

### 10.3 Deployment Checklist

**Pre-Deployment:**

- [ ] Provider API keys validated
- [ ] HMAC key generated (if required)
- [ ] Baseline SPC established (≥100 samples)
- [ ] ECE/AURC calibrated
- [ ] ARL₀ target set
- [ ] MTTD threshold defined
- [ ] Audit log rotation configured
- [ ] Monitoring dashboards ready

**Post-Deployment:**

- [ ] Monitor ARL₀ for 48 hours
- [ ] Verify MTTD < threshold
- [ ] Check ECE stability
- [ ] Validate ALCOA+ compliance
- [ ] Review false alarm rate
- [ ] Confirm formula separation

---

## Appendix A: Formula Comparison Table

| Metric | Formula A | Formula B | Formula C |
|--------|-----------|-----------|-----------|
| Primary Focus | Cognitive load | Temperature stability | Multi-step reasoning |
| Latency Weight | 0.20 | 0.15 | 0.15 |
| Confidence Variance | 0.25 | 0.30 | - |
| Error Weight | 0.20 | 0.15 | 0.15 |
| Special Metrics | Sycophancy (0.20)<br>Inefficiency (0.15) | Entropy (0.25)<br>Consistency (0.15) | Step Count (0.20)<br>Structure (0.25)<br>Coherence (0.25) |
| Typical Use | CLC tests | Temperature sweep | ToM tasks |
| State Bands | 0.25/0.55/0.80 | 0.25/0.55/0.80 | 0.25/0.55/0.80 |

---

## Appendix B: Glossary

- **ALCOA+**: Attributable, Legible, Contemporaneous, Original, Accurate, Complete, Consistent, Enduring, Available
- **ARL₀**: Average Run Length (in-control)
- **AURC**: Area Under Risk-Coverage Curve
- **CLC**: Cognitive Load Correlation
- **CUSUM**: Cumulative Sum (control chart)
- **ECE**: Expected Calibration Error
- **EWMA**: Exponentially Weighted Moving Average
- **MTTD**: Mean Time To Detection
- **SPC**: Statistical Process Control
- **ToM**: Theory of Mind

---

## Appendix C: Reference Implementation

Complete reference implementation available at:

**GitHub:** https://github.com/AIDoctrine/fpc-ae1r  
**Dataset:** 

---

**Document Version:** 1.0  
**Last Updated:** October 14, 2025  
**Status:** Production Release  
**License:** CC BY 4.0

---

## Acknowledgments

This technical specification was developed by Aleksei Novgorodtsev (AIDoctrine) with analytical and linguistic assistance from advanced AI systems (including GPT-4o, Claude Sonnet 4.5, and Perplexity-AI) under full human supervision. All AI contributions were subject to rigorous human review, validation, and editorial control. This collaboration illustrates the emerging paradigm of human-AI co-reasoning in technical documentation while maintaining strict standards of accuracy and intellectual accountability.

---

END OF SPECIFICATION
