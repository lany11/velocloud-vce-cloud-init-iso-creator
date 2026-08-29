# VeloCloud VCE Cloud-Init ISO Creator

[![Python Support](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A pure-Python utility to generate ISO 9660 boot disk images containing `cloud-init` configuration files for Virtual VeloCloud Edges (VCE). 

This script streamlines the Zero-Touch Provisioning (ZTP) process for VCE deployments on hypervisors like VMware ESXi and KVM. By using the `pycdlib` library, it entirely removes the need for OS-level dependencies like `mkisofs` or `genisoimage`, making it completely cross-platform.

---

## 📖 Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
---

## ✨ Features
* **Pure Python:** No need to install `mkisofs`, `genisoimage`, or `xorriso`.
* **VeloCloud Optimized:** Formatted precisely to standard `NoCloud` datasource specifications required by VCE.
* **Cross-Platform:** Works natively on Windows, macOS, and Linux.
* **Automation-Friendly:** Easily integrates into CI/CD pipelines or larger deployment scripts.

---

## 🛠️ Prerequisites

* Python 3.7 or higher
* [pycdlib](https://clalancette.github.io/pycdlib/)

---

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/lany11/velocloud-vce-cloud-init-iso-creator
