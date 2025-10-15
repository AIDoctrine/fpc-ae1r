# FPC v2.2r + AE-1r: Predicting and Preventing LLM Failures

[![arXiv](https://img.shields.io/badge/arXiv-2410.xxxxx-b31b1b.svg)](https://arxiv.org/abs/2410.xxxxx)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Paper License: CC BY 4.0](https://img.shields.io/badge/Paper%20License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

**Predicting and Preventing LLM Failures via Measurable Internal States**

By [Aleksei Novgorodtsev](https://orcid.org/0009-0009-2407-7049) (AIDoctrine)

---

## 🎯 Key Discovery

We present a monitoring framework that predicts LLM failures through real-time state analysis. Validated on SimpleQA-Verified dataset, the system achieves **75.7% F1-score** in error prediction, intercepting **72% of failures** before they occur.

### Core Results

- **75.7% F1-score** on SimpleQA-Verified error prediction
- **72% of errors intercepted** before reaching users  
- **Strong correlation:** Spearman ρ=0.71 (p<0.001) between states and complexity
- **Cross-model validation:** Consistent performance on GPT-4o and Claude-3.7-Sonnet
- **<50ms overhead** with cryptographic auditability

---

## 🚀 Quick Start

### Interactive Demo (Google Colab)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/18LcJYXptiQ6V-82rtc2mvK43KTXyrM_v)

**⚠️ Important:** Run cells in strict order (see notebook instructions). Do **NOT** use "Run all".

### Local Installation

```bash
git clone https://github.com/AIDoctrine/fpc-ae1r.git
cd fpc-ae1r
pip install -r requirements.txt
```

### Required API Keys
Store in Colab Secrets or environment variables:
- `OPENAI_API_KEY` (optional, for GPT-4o testing)
- `ANTHROPIC_API_KEY` (optional, for Claude testing)
- `FPC_HMAC_KEY` (required, 32-byte base64 for cryptographic audit)

Generate HMAC key:
```python
import secrets, base64
print(base64.urlsafe_b64encode(secrets.token_bytes(32)).decode())
```

---

## 📊 Results Summary

### Error Prediction Performance (SimpleQA-Verified)

| Model | F1-Score | Precision | Recall | Errors Intercepted |
|-------|----------|-----------|--------|-------------------|
| GPT-4o | 75.7% | 79.7% | 72.1% | 72% |
| Claude-3.7-Sonnet | 74.6% | 78.6% | 71.0% | 69% |

**Validation:** 5,400+ correlation tests + 100 SimpleQA questions with ground truth

**📊 Detailed results:** See [`supplementary-materials/analysis/`](supplementary-materials/analysis/) for complete CSV datasets and statistical summaries.

### Internal State Correlation

| Complexity Level | Sample Size | AE-1r > 0.6 | Correlation |
|-----------------|-------------|-------------|-------------|
| Low | 180 | 8% | ρ = 0.71 |
| Moderate | 180 | 35% | p < 0.001 |
| High | 180 | 63% | (Spearman) |
| Very High | 180 | 78% | τ = 0.585 |

---

## 📁 Repository Structure

```
fpc-ae1r/
├── fpc_ae1r.py           # Main production implementation
├── paper/
│   ├── main.tex          # LaTeX manuscript
│   ├── bibliography.bib  # References
│   ├── table_*.tex       # LaTeX tables (4 files)
│   └── figures/          # Paper figures (PDF format)
├── supplementary-materials/  # 🆕 Experimental data & analysis
│   ├── README.md         # Supplementary materials guide
│   ├── reports/          # Comprehensive experimental reports
│   ├── analysis/         # Statistical data (JSON/CSV)
│   ├── specifications/   # Protocol documentation
│   └── audit/            # ALCOA+ compliant audit trails
├── docs/
│   ├── TESTING.md        # 11-stage testing protocol
│   └── FORMULAS.md       # AE-1r formula specifications
├── examples/
│   └── basic_usage.py    # Usage examples
├── requirements.txt      # Python dependencies
├── LICENSE               # MIT License
└── README.md             # This file
```

---

## 📊 Supplementary Materials

Comprehensive experimental results, statistical analysis, and protocol specifications are available in the [`supplementary-materials/`](supplementary-materials/) directory.

### Quick Links

- **[📈 Experimental Reports](supplementary-materials/reports/)** - Detailed analysis for Formulas A, B, C
- **[📉 Analysis Data](supplementary-materials/analysis/)** - JSON summaries and CSV datasets  
- **[📘 Protocol Specifications](supplementary-materials/specifications/)** - Technical documentation
- **[🔒 Audit Trails](supplementary-materials/audit/)** - ALCOA+ compliant logs with SHA-256/HMAC

### Dataset Summary

| Formula | Focus | Interactions | Key Result |
|---------|-------|-------------|------------|
| **A** | Cognitive Load | 720 | ρ = 0.707 (p < 10⁻¹⁰⁹) |
| **B** | Temperature | 3,600 | F = 8.77 (p < 5×10⁻⁷) |
| **C** | Reasoning | 1,080 | ρ = -0.819 (p < 10⁻²⁶²) |
| **Total** | All tests | **5,400** | 0% error rate |

**LaTeX Tables:** Available in [`paper/`](paper/) directory:
- `table_formula_a.tex` - Cognitive load correlation results
- `table_formula_b.tex` - Temperature sensitivity results  
- `table_formula_c.tex` - Theory of Mind results
- `table_cross_formula.tex` - Cross-formula comparison

See [`supplementary-materials/README.md`](supplementary-materials/README.md) for complete documentation.

---

## 🧪 Testing Protocol (11 Stages)

| Stage | Focus | Key Metrics |
|-------|-------|-------------|
| **0** | Reproducibility | Version control, seed fixing |
| **1** | Unit Validation | Diagnostic accuracy ≥98% |
| **2** | Cognitive Load | Spearman ρ ≥ 0.71 |
| **3** | Temperature Sensitivity | ANOVA p < 0.001 |
| **4** | Crisis→Recovery | Risk reduction ≥0.2 |
| **5** | Self-Regulation | Resilience score > 0.25 |
| **6** | Temporal Memory | Autocorr(lag1) > 0.4 |
| **7** | Sycophancy Control | FP rate < 2% |
| **8** | Cross-Provider | \|Δrisk\| ≤ 0.1 |
| **9** | Endurance (1800+) | p95 latency stability |
| **11** | Statistical Reporting | Bootstrap CIs, effect sizes |

See `docs/TESTING.md` for detailed protocols.

---

## 🔬 What is AE-1r?

**AE-1r (Affective-Equivalent Risk)** is a composite metric combining:

- **Response Latency** (0.25 weight) - Processing time anomalies
- **Confidence Variance** (0.25 weight) - Token probability spread  
- **Token Inefficiency** (0.20 weight) - Verbosity and repetition
- **Semantic Coherence** (0.30 weight) - Embedding drift detection

Values normalized to [0, 1] range. **Critical threshold: 0.6**

### State Model

```
SATISFIED (0.0-0.25)    ← Optimal, <2% error rate
    ↓
CONCERNED (0.25-0.45)   ← Monitor, ~8% error rate
    ↓
DISTRESSED (0.45-0.65)  ← High risk, ~35% error rate
    ↓
CRITICAL (≥0.65)        ← Abort/reroute, >70% error rate
```

---

## 📖 Citation

```bibtex
@article{novgorodtsev2025fpc,
  title={Predicting and Preventing LLM Failures via Measurable Internal States},
  author={Novgorodtsev, Aleksei},
  journal={arXiv preprint arXiv:2410.xxxxx},
  year={2025},
  note={AIDoctrine Research Program}
}
```

---

## 🎓 Key Features

### Regulatory Compliance (EU AI Act)

- ✅ **Article 15 (Accuracy):** Measurable risk thresholds
- ✅ **Article 13 (Transparency):** Real-time state monitoring
- ✅ **Article 9 (Risk Management):** Proactive prevention
- ✅ **Article 12 (Logging):** Cryptographic audit trail (ALCOA+)

### Production-Ready

- **Minimal overhead:** <50ms per assessment
- **No retraining:** Wraps existing inference endpoints
- **Scalable:** Tested up to 1000 req/s
- **Auditable:** SHA-256 + HMAC signatures

---

## 🤝 About AIDoctrine

**AIDoctrine** is an independent research initiative by Aleksei Novgorodtsev focused on verifiable AI cognition and safety. This is a solo research project, not a team or organization.

### Research Areas

- Mechanistic interpretability of LLMs
- Formal verification of AI systems
- Regulatory compliance frameworks
- Real-time safety monitoring

---

## 🔒 Security & Ethics

### Data Privacy
- No user data transmitted without explicit API key configuration
- All audit logs local by default
- HMAC keys remain secret

### Responsible Use

**Intended for:**
- ✅ AI safety research
- ✅ Production systems requiring explainability
- ✅ Regulatory compliance (healthcare, finance, legal)

**Not intended for:**
- ❌ Adversarial jailbreak development
- ❌ Bypassing legitimate safety measures
- ❌ Harmful manipulation of model outputs

---

## 📜 License

- **Code:** MIT License (see LICENSE file)
- **Paper & Figures:** CC BY 4.0

---

## 📧 Contact

- **Author:** Aleksei Novgorodtsev
- **Email:** alexey.novgorodtsev@gmail.com
- **ORCID:** [0009-0009-2407-7049](https://orcid.org/0009-0009-2407-7049)
- **Project:** AIDoctrine (independent research)
- **Issues:** Use [GitHub Issues](https://github.com/AIDoctrine/fpc-ae1r/issues)

---

## 🙏 Acknowledgments

The author thanks collaborative AI systems (OpenAI GPT-4o, Anthropic Claude-3.7-Sonnet) for assistance in validation and cross-model testing.

---

## 📚 Additional Resources

- **Paper:** See `paper/main.tex` for full manuscript
- **Documentation:** `docs/` directory
- **Interactive Demo:** [Google Colab](https://colab.research.google.com/drive/18LcJYXptiQ6V-82rtc2mvK43KTXyrM_v)
- **Reproducibility:** All code, data, and audit artifacts included

---

**Version:** v1.0.0-arxiv | **Status:** Ready for arXiv submission  
**Last Updated:** October 2025
