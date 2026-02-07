---
title: "Wideband Modeling and Simulation of Multiple PCB Components in CubeSat Environment"
excerpt: "Presented at 2025 ESA workshop on aerospace EMC, this talk explored how to model the electromagnetic behavior of wideband PCBs in closed environments, such as inside a CubeSat."
collection: talks
type: "Conference proceedings talk"
permalink: /talks/ESA_workshop_2025
venue: "2025 ESA Workshop on Aerospace EMC (Aerospace EMC)"
date: 2025-05-13
location: "Seville, Spain"
---


## 🎤 Talk Overview

This **technical paper** introduces a wideband modeling method for deriving equivalent **Infinitesimal Dipole Models (IDMs)** of **Printed Circuit Boards (PCBs)** within a CubeSat environment. The approach utilizes a **morphological image-processing** technique to enable rapid, wideband simulations that predict **mutual coupling** and enhance **Electromagnetic Compatibility (EMC)** testing for compact satellite designs.

### 🔹 **Key Topics**

✔ **Morphological Dipole Search (MDS)** for deterministic and efficient source identification 
✔ **Infinitesimal Dipole Model (IDM)** construction using base electric and magnetic dipoles 
✔ **Multi-frequency equivalent models** that maintain validity across a wide operational spectrum 
✔ **Full-wave simulation (HFSS)** integration to evaluate EMI in dense CubeSat stacking 
✔ **Mutual coupling estimation ($S_m$)** between multiple boards using reciprocity-based formulas 

### 🛠 **Methodology**

* **Modeling Approach**: **MDS algorithm** based on **binary erosion** to match measured field maps with radiation "kernels" of base dipoles.
* **Optimization**: Dipole moments are calculated using **normal equations** with a **regularization parameter** to prevent overfitting.
* **Validation**:
  * Tested on two virtual DUTs: a **patch strip** and a **bent strip**. Simulated over a frequency range from **30 MHz to 1000 MHz**.
  * Boards were placed in a $10\times 10 \times 10$ cm **cubic box** with reflective sides to **simulate a CubeSat interior**. 
  
* **Key Findings**:
  * IDMs show **excellent agreement** with original board near-field maps at validation heights.
  * The model successfully predicts **coupled power** between boards at various separation distances.
  * The method provides a **robust tool** for design optimization where traditional wiring pathways for EMI are absent.


### 📍 **Publication Details**
📅 **Date**: February 7, 2026 (Access Date) 
📍 **Location**: Seville, Spain  
🏢 **Venue**: 2025 ESA workshop on Aerospace EMC

---

📑 **[Download Slides](/files/ESA_workshop_Seville_2025.pptx)**  
📄 **[Read the Full Paper](https://doi.org/10.23919/AerospaceEMC64918.2025.11074834)**  
🔗 **[Conference Website](https://ieeexplore-ieee-org.zorac.aub.aau.dk/xpl/conhome/11074777/proceeding)** 