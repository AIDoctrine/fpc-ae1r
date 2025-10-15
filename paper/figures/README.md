# Paper Figures

This directory contains figures for the manuscript.

## Required Figures (PDF format)

1. **figure_s1_pipeline.pdf** - Experimental pipeline overview
2. **figure_s2_states.pdf** - State transition model
3. **figure_formula_a_correlation.pdf** - Cognitive load correlation (N=720)
4. **figure_formula_b_temperature.pdf** - Temperature effects (N=3,600)
5. **figure_cross_formula_comparison.pdf** - Cross-formula validation
6. **figures/figure_mechanistic_unified.pdf** - Unified mechanistic model

## Generating Figures

Figures are generated from test results:

```python
from fpc_ae1r import generate_paper_figures
generate_paper_figures(session_id="your-session-id", output_dir="paper/figures/")
```

## Specifications

- Format: PDF (vector graphics)
- Resolution: 300 DPI minimum
- Fonts: Embedded
- Color: Color-blind friendly
