# 📱 Can My AI Model Run On Phone?

> A practical toolkit to evaluate whether an AI model can realistically run on a mobile device.

---

## 🎯 Why This Project Exists

During a hackathon, I worked on a deep learning model for deepfake detection that was required to run **fully on-device**, without any cloud dependency. In practical terms, this meant the model had to execute reliably on a smartphone, offline, under real resource constraints.

While evaluating feasibility, I realized there was no single, practical reference that addressed this problem end-to-end. Most resources either focused on model accuracy or assumed ideal hardware, ignoring mobile OS behavior, memory pressure, and latency tradeoffs.

**This repository is an attempt to fill that gap.**

It provides practical tools to answer a simple question:

> **Can this model actually run on a phone — acceptably and reliably?**

---

## 🛠️ What This Project Does

This repository provides three complementary tools to evaluate mobile deployability of AI models:

| Method | Approach | Accuracy vs Accessibility |
|--------|----------|--------------------------|
| **1. ONNX Runtime** | Constrained desktop benchmarking | ⚡ Fastest to set up |
| **2. Browser-based** | Inference under artificial slowdown | 🌐 Most accessible (planned) |
| **3. Android Termux** | On-device benchmarking | ✅ Gold standard |

Each tool trades accuracy for accessibility differently. Used together, they provide a realistic feasibility signal.

---

## 📋 Tooling Overview

### 1. 🖥️ ONNX Runtime (Constrained Desktop Probe)

Runs an ONNX model under controlled CPU, memory, and thread limits to obtain a rough upper-bound estimate. This is the easiest to implement.

**✨ Use Cases**
- Early-stage feasibility checks
- CI/automated screening
- Catching obviously non-mobile models

**⚠️ Limitations**
- Desktop CPU ≠ mobile CPU: they use different architectures
- Does not model Android scheduling or thermal behavior

---

### 2. 🌐 Browser-based Slowdown Proxy (Planned)

Runs inference in a browser environment with artificial slowdowns (e.g., 4×, 6×) to approximate client-side constraints.

**✨ Use Cases**
- Quick experimentation
- WebML and WASM-based inference
- Extremely accessible testing

**⚠️ Limitations**
- Not representative of mobile CPUs

**Status:** 🚧 Planned

---

### 3. 📱 Android Termux Benchmark (Gold Standard)

Runs inference directly on a physical Android device using Termux.

**This captures:**
- ARM execution characteristics
- Android memory pressure
- OS scheduling and process behavior

This is treated as the **ground truth** for mobile feasibility. Though setting this up is time-consuming, once done, it runs smoothly and provides the most accurate results.

**Recommended:** ⭐⭐⭐⭐⭐

---

## 💡 Important Note

> **ℹ️ About the Example Models**
>
> The example models used in this repository (e.g., dog vs cat image classification) are intentionally simple and familiar.
>
> They are **not meant to demonstrate model accuracy or training techniques**. The purpose is to provide a clear baseline for reasoning about inference latency, memory usage, and behavior under resource constraints.
>
> These models act as sanity checks for the pipeline. The same tooling applies to larger and more complex models without modification.

---

## 🧪 Test Environments

| Method | Environment |
|--------|-------------|
| **Method 1** (Constrained ONNX Runtime) | Google Colab with explicit CPU and memory limits |
| **Method 3** (On-device Benchmark) | Physical Android device: Samsung F23, Snapdragon 750G, 6 GB RAM (Termux) |

Example scripts and screenshots for each method are provided in the repository.

---

## 📥 Model Input

All methods assume an **exported ONNX model**.

If you don't already have one, a reference Colab notebook is included that demonstrates:
- Training a simple model
- Exporting it to ONNX format

---

## 🚫 Non-Goals

This project is **not**:
- ❌ A model accuracy benchmark
- ❌ A replacement for professional on-device profiling tools

However, Method 3 (Termux benchmark) comes pretty close to real-world performance.

---

## 🚀 Estimated Time for Setting up:

Method 1: <5 min
Method 3: <30min

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

---

**Made with ❤️ for practical mobile AI deployment**