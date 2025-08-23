---
title: '[2312.07316] GateNet: A novel Neural Network Architecture for Automated Flow
  Cytometry Gating'
authors:
- Lukas Fisch
- Michael O. Heming
- Andreas Schulte-Mecklenbeck
- Catharina C. Gross
- Stefan Zumdick
- Carlotta Barkhau
- Daniel Emden
- Jan Ernsting
- Ramona Leenings
- Kelvin Sarink
- Nils R. Winter
- Udo Dannlowski
- Heinz Wiendl
- Gerd Meyer zu Hörste
- Tim Hahn
date: '2023-12-01'
publishDate: '2025-08-23T15:44:27.878221Z'
publication_types:
- article-journal
publication: '*arXiv*'
abstract: Flow cytometry is widely used to identify cell populations in patient-derived
  fluids such as peripheral blood (PB) or cerebrospinal fluid (CSF). While ubiquitous
  in research and clinical practice, flow cytometry requires gating, i.e. cell type
  identification which requires labor-intensive and error-prone manual adjustments.
  To facilitate this process, we designed GateNet, the first neural network architecture
  enabling full end-to-end automated gating without the need to correct for batch
  effects. We train GateNet with over 8,000,000 events based on N=127 PB and CSF samples
  which were manually labeled independently by four experts. We show that for novel,
  unseen samples, GateNet achieves human-level performance (F1 score ranging from
  0.910 to 0.997). In addition we apply GateNet to a publicly available dataset confirming
  generalization with an F1 score of 0.936. As our implementation utilizes graphics
  processing units (GPU), gating only needs 15 microseconds per event. Importantly,
  we also show that GateNet only requires 1̃0 samples to reach human-level performance,
  rendering it widely applicable in all domains of flow cytometry.
links:
- name: URL
  url: https://arxiv.org/abs/2312.07316
---
