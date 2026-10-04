# Sam Green
 
**Research Software Engineer / Computational Specialist**
ARC Centre of Excellence for the Weather of the 21st Century — UNSW Sydney 🇦🇺
 
[![ORCID](https://img.shields.io/badge/ORCID-0000--0003--1129--4676-A6CE39?logo=orcid&logoColor=white)](https://orcid.org/0000-0003-1129-4676)
[![Zenodo](https://img.shields.io/badge/Zenodo-software%20releases-1682D4?logo=zenodo&logoColor=white)](https://zenodo.org/search?q=metadata.creators.person_or_org.name%3A%22Sam%20Green%22)
[![21st Century Weather](https://img.shields.io/badge/CoE-21st%20Century%20Weather-0B3C5D)](https://21centuryweather.org.au/profile/sam-green/)
 
I build the computational machinery that climate and atmospheric science runs on: HPC pipelines, ML surrogates for physical models, and data engineering at the TB-to-PB scale. PhD in computational astrophysics; these days the fluid dynamics happen closer to the ground.
 
---
 
### What I work on
 
- **ML for the atmosphere** — CFD surrogates, neural compression, and physics-informed architectures on H200 GPUs
- **HPC scientific computing** — PBS Pro on NCI Gadi, Slurm on Pawsey Setonix; Apptainer/Singularity, Lustre & GPFS I/O tuning
- **Scientific data engineering** — xarray · Dask · Zarr · Pipelines for ERA5, MERRA-2, BARRA2, OISST, 20CRv3
- **Research tooling** — Rust CLIs and web dashboards that make shared systems less painful for the people using them
I care a lot about operational elegance: tools that deploy cleanly on shared systems, respect inode budgets, and don't fall over at 3am.
 
---
 
### Selected projects
 
| Project | What it is |
| --- | --- |
| **[HPC Dashboard](https://github.com/greensh16/hpc_dashboard_public)** [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22105689.svg)](https://doi.org/10.5281/zenodo.22105689) | Web dashboard tracking job efficiency, queue behaviour and resource utilisation across the Centre's allocations. |
| **[logger-rs](https://github.com/greensh16/logger-rs)** [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22105314.svg)](https://doi.org/10.5281/zenodo.22105314) | High-performance telemetry collection for HPC jobs, written in Rust. |
| **Feilian-3D** [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18252581.svg)](https://doi.org/10.5281/zenodo.18252581) | 3D U-Net CFD surrogate predicting volumetric urban wind fields, with FiLM conditioning on inflow direction. Trained across 355 urban domains. |
| **TRACE / AtmosCodec** | Transformer Reanalysis Atmospheric Compression Engine — a Swin-Transformer VAE neural codec for MERRA-2 and ERA5 reanalysis, built on CompressAI. |
| **[rudu](https://github.com/greensh16/rudu)** [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15347728.svg)](https://doi.org/10.5281/zenodo.15347728) | Parallel disk-usage tool in Rust. Rayon-based, reports allocated-block usage — built for HPC filesystems where `du` gives up. |
| **[zarr-dump](https://github.com/greensh16/zarr-dump)** [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18666267.svg)](https://doi.org/10.5281/zenodo.18666267) | A CLI tool for inspecting Zarr v2/v3 stores and printing their metadata in a familiar NetCDF-style header format (similar to `ncdump -h`) |
 
---
 
### Recent publications & software
 
<!-- PUBLICATIONS:START -->
- **[logger-rs: resource telemetry for HPC jobs](https://doi.org/10.5281/ZENODO.22105313)**  
  <sub>software · 2026</sub>
- **[greensh16/xray-cs: v1.3.1](https://doi.org/10.5281/ZENODO.22910459)**  
  <sub>software · 2026</sub>
- **[greensh16/rudu: v1.5.1](https://doi.org/10.5281/ZENODO.15321604)**  
  <sub>software · 2026</sub>
- **[HPC Dashboard: seeing what an HPC job actually used](https://doi.org/10.5281/ZENODO.22105688)**  
  <sub>software · 2026</sub>
- **[Hacking Kilometer-Scale Models: A Participative Model for Climate Information](https://doi.org/10.1175/BAMS-D-25-0183.1)**  
  <sub>Bulletin of The American Meteorological Society - (BAMS) · journal article · 2026</sub>
- **Quantifying the impact of climate change on Indigenous right-way burning practices in the Mimal Management Area**  
  <sub>Journal of Southern Hemisphere Earth Systems Science · preprint · 2026</sub>
<!-- PUBLICATIONS:END -->
 
<sub>Full record: [ORCID 0000-0003-1129-4676](https://orcid.org/0000-0003-1129-4676)</sub>
 
---
 
### Toolbox
 
**Languages** Python · Rust · Bash
**Scientific stack** xarray · Dask · NumPy · Numba · Zarr · Kerchunk · cuDF
**ML** PyTorch · DDP/torchrun · CompressAI · NVIDIA PhysicsNeMo
**Infrastructure** PBS Pro · Slurm · Apptainer/Singularity · GitHub Actions · Docker
 
---
 
### Currently
 
- Scaling Feilian-3D
- Extending TRACE from MERRA-2 to ERA5, with an eye on CMIP6/7
- Making the Centre's dataset pipelines fail loudly instead of silently
- Preparing the release of the HPC Dashboard and logger-rs
---
 
<sub>📍 Sydney, NSW · [sam.green@unsw.edu.au](mailto:sam.green@unsw.edu.au) · [21centuryweather.org.au](https://21centuryweather.org.au/profile/sam-green/)</sub>