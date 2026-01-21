# ML Calculus Lab

A **from-scratch learning lab** for calculus concepts used in Machine Learning, with a strong focus on intuition, numerical methods, and visualization.

## Overview

This repository builds calculus understanding without relying on symbolic math libraries. Instead of treating derivatives as abstract symbols, you'll see **what they actually measure** and **how they're used** in optimization algorithms like gradient descent.

**Core Question**: *If I change a parameter slightly, how does the loss change?*

This repo is designed to complement a separate Linear Algebra project (vectors, matrices, SVD, PCA).

---

## Repository Structure

```
ml-calculus-lab/
│
├── math/
│   ├── derivatives.py          # Numerical and analytical derivatives
│   ├── gradients.py             # Gradients (multi-variable, coming next)
│   └── chain_rule.py            # Chain rule for composed functions
│
├── experiments/
│   ├── gradient_1d.ipynb        # Visualizing derivatives and tangent lines
│   └── gradient_descent.ipynb   # Gradient descent experiments
│
├── README.md
└── requirements.txt
```

---

## Core Concepts Covered

### 1. Derivatives (Single Variable)
- Derivative as rate of change
- Derivative as slope of the tangent line
- Forward vs central difference
- Numerical stability considerations

### 2. Numerical Differentiation
- Finite difference methods
- Why ML libraries avoid naïve differentiation
- Accuracy vs stability tradeoffs

### 3. Gradients (Upcoming)
- Extension from 1D derivatives to multi-variable gradients
- Geometric interpretation of gradients
- Connection to loss landscapes

### 4. Optimization
- Gradient descent in 1D
- Intuition behind parameter updates
- Step size (learning rate) effects

---

## Getting Started

### Prerequisites
- Python 3.8+
- Basic understanding of functions and algebra
- Curiosity about how ML optimization works

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ml-calculus-lab.git
   cd ml-calculus-lab
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Quick Start

1. **Start with the experiment notebook**
   ```bash
   jupyter notebook experiments/gradient_1d.ipynb
   ```

   This notebook:
   - Plots a function (e.g., f(x) = x²)
   - Computes numerical derivatives
   - Draws tangent lines
   - Builds intuition visually

2. **Explore the implementation**
   
   Check out `math/derivatives.py` to see how derivatives are computed numerically using finite differences.

---

## Design Philosophy

- **No black boxes** — Everything is implemented explicitly
- **Visualization first** — Math should be seen, not memorized
- **ML relevance** — Every concept maps to real ML workflows
- **Numerical awareness** — Stability and approximation errors matter

---

## Relation to Machine Learning

This repository directly prepares you for understanding:

- Gradient descent
- Backpropagation
- Loss optimization
- Neural network training
- How frameworks like PyTorch and TensorFlow compute gradients

---

## Recommended Learning Path

1. `math/derivatives.py` — Understand the implementation
2. `experiments/gradient_1d.ipynb` — Visualize derivatives
3. `math/gradients.py` — Extend to multiple variables
4. `experiments/gradient_descent.ipynb` — See optimization in action
5. `math/chain_rule.py` — Build backpropagation intuition

---

## Why From Scratch?

Most ML courses jump straight to frameworks like PyTorch or TensorFlow. While powerful, these tools hide the mechanics of how gradients are computed. By building from scratch, you'll:

- Understand what `.backward()` actually does
- Debug gradient issues with confidence
- Develop numerical intuition
- Appreciate the engineering behind autodiff systems

---

## Status

🚧 **Active Learning Project**

This repository prioritizes:
- ✅ Correctness
- ✅ Intuition
- ✅ Clarity

Over:
- ❌ Completeness
- ❌ Production-readiness

---

## Contributing

This is a personal learning project, but suggestions and corrections are welcome! Feel free to open an issue or submit a pull request.

---

## License

MIT License - feel free to use this for your own learning journey.

---

## Resources

Complementary materials that pair well with this repository:

- [3Blue1Brown - Essence of Calculus](https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr)
- [Calculus for Machine Learning](https://explained.ai/matrix-calculus/)
- Understanding backpropagation and the chain rule

---

**Happy Learning!** 🎓

If you find this helpful, consider giving it a ⭐