AIDoctrine — FPC v2.2r + AE-1r Reproducibility Package
-------------------------------------------------------

This archive contains the complete set of experimental and cryptographic
artifacts accompanying the publication:

    “Predicting and Preventing LLM Failures via Measurable Internal States:
     The FPC v2.2r + AE-1r Protocol”

All materials are provided to ensure full scientific reproducibility and
regulatory-grade traceability in compliance with ALCOA+ principles and the
EU AI Act Annex IV requirements.

-------------------------------------------------------
STRUCTURE
-------------------------------------------------------

/ancillary/
│
├── AUDIT_A/   → Test 9.2.0 – Formula A (Cognitive Load Correlation)
│     clc_progress.jsonl[+sha256+hmac]
│     clc_results.jsonl[+sha256+hmac]
│     clc_summary.json[+sha256+hmac]
│     clc_pointer.json
│     clc_report.sha256
│
├── AUDIT_B/   → Test 9.3.0 – Formula B (Temperature Sensitivity)
│     formulaB_results.jsonl[+sha256+hmac]
│     formulaB_progress.jsonl
│     provider_calls.jsonl[+sha256+hmac]
│     provider_calls.pointer.json[+sha256+hmac]
│     provider_telemetry.json[+sha256+hmac]
│     formulaB_report.sha256
│
└── AUDIT_C/   → Test 9.4.0 – Formula C (Structured Reasoning / ToM)
      formulaC_progress.jsonl[+sha256+hmac]
      formulaC_results.jsonl[+sha256+hmac]
      formulaC_summary.json[+sha256+hmac]
      formulaC_pointer.json
      po_validation_report.json[+sha256+hmac]
      data_provenance.json[+sha256+hmac]
      data_schema_report.json
      schemas.json
      runtime_census.sha256
      formulaC_report.sha256

-------------------------------------------------------
INTEGRITY VERIFICATION
-------------------------------------------------------

Each file is accompanied by a SHA-256 digest (.sha256) and, where applicable,
an HMAC-SHA256 signature (.hmac).  These sidecars guarantee the authenticity,
integrity, and immutability of every artifact.

To verify integrity using standard Linux tools:

    sha256sum -c filename.sha256

All timestamps follow RFC3339 UTC format.  
No private signing key is disclosed; verification can be performed via
SHA-256 recomputation and Merkle-root validation using the included
shadow-verification scripts.

-------------------------------------------------------
REPRODUCIBILITY SCOPE
-------------------------------------------------------

The artifacts collectively satisfy all Proof Obligations (PO1–PO10)
defined in the FPC Production Manifest:

    • PO1 – Runtime Census Integrity
    • PO2 – Environment Control
    • PO3 – Chronological Logging
    • PO4 – Traceability
    • PO5 – Accuracy & Stability
    • PO6 – ALCOA+ Sidecars
    • PO7 – Persistence
    • PO8 – Statistical Summary
    • PO9 – Reproducibility Record
    • PO10 – Deterministic Timestamps

-------------------------------------------------------
AUTHOR AND PROJECT
-------------------------------------------------------

Author: Aleksei Novgorodtsev
Project: AIDoctrine
Protocol Series: FPC v2.2r + AE-1r (RAL-Ready)
Release Date: October 2025
License: CC BY-NC 4.0 + Reproducibility Supplement Clause
