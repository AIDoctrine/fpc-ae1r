# Ancillary Materials for FPC v2.2 + AE-1r

**Author:** Aleksei Novgorodtsev (AIDoctrine)  
**Contact:** alexey.novgorodtsev@gmail.com  
**Date:** October 2025

---

## 📂 Directory Structure

```
ancillary/
├── README.txt                         # This file
├── reports/                           # Comprehensive experimental reports
│   ├── formula_a_comprehensive_report.md
│   ├── formula_b_comprehensive_report.md
│   └── formula_c_comprehensive_report.md
├── analysis/                          # Statistical analysis data
│   ├── formula_a_analysis_summary.json
│   ├── formula_b_analysis_summary.json
│   ├── formula_c_analysis_summary.json
│   ├── cross_formula_summary.json
│   ├── formula_a_detailed_report.csv
│   ├── formula_b_detailed_report.csv
│   └── formula_c_detailed_report.csv
└── specifications/                    # Protocol documentation
    ├── fpc_technical_specification.md
    ├── fpc_production_manifest.md
    ├── fpc_ral_appendix.pdf
    └── README_ARXIV_SUBMISSION.md
```

---

## 📊 Reports Directory

### Formula A: Cognitive Load Correlation

**File:** `reports/formula_a_comprehensive_report.md`

**Contents:**
- Complete experimental methodology
- Per-provider breakdowns (OpenAI, Anthropic)
- Complexity bin analysis (very_low, low, medium, high)
- State transition matrices
- Statistical tests (Spearman, Kendall, bootstrap CI)

**Key Results:**
- N = 720 interactions
- Spearman ρ = 0.707 (p < 10⁻¹⁰⁹)
- Monotonic load → risk correlation validated

---

### Formula B: Temperature Sensitivity

**File:** `reports/formula_b_comprehensive_report.md`

**Contents:**
- Temperature sweep methodology (T: 0.1, 0.3, 0.5, 0.7, 0.9)
- Per-temperature statistics
- Entropy and variance analysis
- State distribution changes
- ANOVA results

**Key Results:**
- N = 3,600 interactions
- ANOVA F = 8.77 (p < 5×10⁻⁷)
- SATISFIED states: 43% decrease (T: 0.1 → 0.9)

---

### Formula C: Theory of Mind / Reasoning

**File:** `reports/formula_c_comprehensive_report.md`

**Contents:**
- Multi-step reasoning task design
- Structure and coherence scoring
- Per-family analysis (belief, false-belief, etc.)
- Degradation patterns in complex tasks
- Qualitative examples

**Key Results:**
- N = 1,080 interactions
- Coherence ↔ Risk: ρ = -0.819 (p < 10⁻²⁶²)
- Causal reasoning gap identified (0% conclusions)

---

## 📈 Analysis Directory

### JSON Summaries

**Files:**
- `formula_a_analysis_summary.json` — Formula A statistics
- `formula_b_analysis_summary.json` — Formula B statistics
- `formula_c_analysis_summary.json` — Formula C statistics
- `cross_formula_summary.json` — Cross-formula comparison

**Format:**
```json
{
  "experiment": "formula_a",
  "n_total": 720,
  "providers": ["openai", "anthropic"],
  "statistics": {
    "spearman_rho": 0.707,
    "p_value": "< 1e-109",
    "bootstrap_ci": [0.65, 0.76]
  },
  "by_complexity": {...},
  "by_provider": {...}
}
```

### CSV Reports

**Files:**
- `formula_a_detailed_report.csv`
- `formula_b_detailed_report.csv`  
- `formula_c_detailed_report.csv`

**Columns:**
```
question_id, provider, model, temperature, complexity_bin,
ae1r_score, ae1r_state, latency_ms, is_error, ...
```

**Use:** Raw data for independent validation

---

## 📚 Specifications Directory

### FPC Technical Specification

**File:** `specifications/fpc_technical_specification.md`  
**Size:** ~27 KB  
**Format:** Markdown

**Contents:**
- Complete protocol specification (FPC v2.2r + AE-1r)
- State machine definitions
- AE-1r formulas (A, B, C) with Python code
- SPC algorithms (EWMA, CUSUM, Page-Hinkley)
- ALCOA+ requirements
- Implementation guidelines

**Use:** Reference for protocol implementation

---

### Production Manifest

**File:** `specifications/fpc_production_manifest.md`  
**Size:** ~16 KB  
**Format:** Markdown

**Contents:**
- 11 non-negotiable production rules
- Cell-by-cell execution order
- Provider hook contracts
- Formula specifications
- Compliance checklist
- Version history

**Use:** Deployment and audit guide

---

### RAL Appendix

**File:** `specifications/fpc_ral_appendix.pdf`  
**Size:** ~99 KB  
**Format:** PDF

**Contents:**
- Tri-Sentinel architecture (Math/Logic/Semantics)
- Risk fusion algorithm
- Calibration requirements  
- Configuration examples (YAML)
- Evaluation metrics
- Implementation roadmap

**Use:** Advanced risk decomposition extension

---

### Detailed Submission Guide

**File:** `specifications/README_ARXIV_SUBMISSION.md`  
**Size:** ~13 KB  
**Format:** Markdown

**Contents:**
- Complete package overview
- Quick start guide (5 minutes)
- Key results summary
- Citation information
- Troubleshooting
- Contact information

**Use:** Comprehensive guide for reviewers and reproducers

---

## 🔬 Data Integrity

All experimental data is ALCOA+ compliant:

- **Attributable:** Every interaction tagged with session_id, provider, model
- **Legible:** UTF-8 JSON/CSV, human-readable
- **Contemporaneous:** RFC3339 UTC timestamps
- **Original:** SHA-256 + HMAC integrity verification
- **Accurate:** IEEE 754 double precision
- **Complete:** No missing required fields
- **Consistent:** Validated across sessions
- **Enduring:** Permanent retention
- **Available:** Publicly accessible

**Verification:**
```bash
# Check integrity (example)
sha256sum formula_a_detailed_report.csv
# Compare with published hash
```

---

## 🎯 For Reviewers

### Quick Validation Checklist

1. **Verify dataset scale:**
   ```bash
   wc -l analysis/*.csv
   # Should show 720, 3600, 1080 lines (+ headers)
   ```

2. **Check statistical significance:**
   ```bash
   cat analysis/formula_a_analysis_summary.json | grep p_value
   # Should show p < 1e-100 range
   ```

3. **Review provider consistency:**
   ```bash
   cat analysis/cross_formula_summary.json
   # Check inter_provider_correlation > 0.85
   ```

4. **Examine error rates:**
   ```bash
   grep is_error analysis/*.csv
   # Should show zero errors
   ```

---

## 📖 Citation

When citing these materials:

**Comprehensive Reports:**
```bibtex
@misc{novgorodtsev2025fpc_reports,
  author={Novgorodtsev, Aleksei},
  title={{FPC-AE1r Comprehensive Experimental Reports}},
  year={2025},
  note={Supplementary material for arXiv:XXXX.XXXXX}
}
```

**Dataset:**
```bibtex
@dataset{novgorodtsev2025fpc_data,
  author={Novgorodtsev, Aleksei},
  title={{FPC-AE1r Experimental Dataset}},
  year={2025},
  publisher={public dataset hosts},
  url={}
}
```

---

## 🌐 External Resources

**Full Dataset (public dataset hosts):**  


**Code Repository (GitHub):**  
https://github.com/AIDoctrine/fpc-ae1r

**Interactive Notebooks:**  
Available in repository `/notebooks` directory

---

## 📞 Contact

**For questions about:**

- **Scientific methodology:** alexey.novgorodtsev@gmail.com
- **Technical implementation:** GitHub issues
- **Data access:** public dataset hosts repository
- **Collaboration:** LinkedIn (https://www.linkedin.com/in/anovgorodtsev/)

---

## 🙏 Acknowledgments

These supplementary materials were developed by Aleksei Novgorodtsev (AIDoctrine) with analytical and linguistic assistance from advanced AI systems (including GPT-4o, Claude Sonnet 4.5, and Perplexity-AI) under full human supervision. All AI contributions were subject to rigorous human review, validation, and editorial control.

Special appreciation to the open-source community for analytical tools enabling reproducibility.

---

## 📄 License

**Reports:** CC BY 4.0  
**Analysis Data:** CC BY 4.0  
**Specifications:** CC BY 4.0  
**Code (in repository):** MIT License

Full license texts available in repository.

---

**Last Updated:** October 14, 2025  
**Version:** 1.0 FINAL

---

END OF ANCILLARY README
