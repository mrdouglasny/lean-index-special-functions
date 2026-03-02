# lean-index-special-functions

Topical index for special functions formalization in Lean 4. **[How to use this index in your project](https://github.com/mrdouglasny/lean-index/blob/main/docs/use-topic-index.md)**

<!-- STATS_START -->
**12,695 topic-matched declarations** across **18 repositories** (scanned 28 repos, 19,970 declarations).

Tracks Lean declarations related to:
- **Power series** (2,958 matches): formal/multivariate power series, Hahn series, Fourier/Mellin transforms
- **Exponential and logarithmic** (2,773 matches): exp, log, rpow, sqrt, complex powers
- **Trigonometric** (2,257 matches): sin, cos, tan, arctan, hyperbolic functions, Chebyshev polynomials
- **Zeta and L-functions** (1,625 matches): Riemann/Hurwitz zeta, Dirichlet L-series, Euler products, Bernoulli numbers, arithmetic functions
- **Elliptic curves** (1,382 matches): Weierstrass curves, division polynomials, j-invariant
- **Modular forms** (1,290 matches): modular/cusp forms, Eisenstein series, Jacobi theta, Dedekind eta, upper half plane
- **Classical special functions** (1,111 matches): Gamma, Beta, digamma, Pochhammer, hypergeometric, Gaussian, Stirling, Hermite, elliptic functions
<!-- STATS_END -->

See [SELECTION.md](SELECTION.md) for exact selection criteria. See [REPOS.md](REPOS.md) for all indexed repositories.

## Indexed Repos

<!-- REPOS_TABLE_START -->
| Repository | Topic Matches | Description |
|-----------|:---:|-------------|
| [leanprover-community/mathlib4](https://github.com/leanprover-community/mathlib4) | 11,690 | The math library for Lean 4 (indexed via cache, not cloned) |
| [AlexKontorovich/PrimeNumberTheoremAnd](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd) | 391 | Prime Number Theorem, L-series, Mellin transforms |
| [CBirkbeck/ModularForms_Lean4](https://github.com/CBirkbeck/ModularForms_Lean4) | 258 | Modular forms in Lean 4 |
| [laughinggas/padic-L-functions4](https://github.com/laughinggas/padic-L-functions4) | 78 | p-adic L-functions |
| [BryceT233/power-series-ring-is-noetherian-](https://github.com/BryceT233/power-series-ring-is-noetherian-) | 60 | This file formalized that if $R$ is noetherian, then its power series ring... |
| [mo271/stirling](https://github.com/mo271/stirling) | 45 | Stirling's formula in Lean |
| [chenlingccll/a-lean4-formalisation-of-Hilbert-basis-theorem-for-power-series-ring](https://github.com/chenlingccll/a-lean4-formalisation-of-Hilbert-basis-theorem-for-power-series-ring) | 39 | a lean4 formalization of Hilbert basis theorem for power series ring. Supposed... |
| [girving/interval](https://github.com/girving/interval) | 34 | Interval arithmetic, rigorous numerics |
| [girving/ray](https://github.com/girving/ray) | 24 | Analytic number theory, special functions |
| [attila-ac/hyperlocal](https://github.com/attila-ac/hyperlocal) | 21 | Off-Critical Riemann Zeta Zeros Cannot Seed Symmetric Entire Functions: A... |
| [MichaelStollBayreuth/EulerProducts](https://github.com/MichaelStollBayreuth/EulerProducts) | 16 | Euler products for Dirichlet L-series |
| [AlexKontorovich/Lean-RH](https://github.com/AlexKontorovich/Lean-RH) | 15 | Riemann hypothesis formalization |
| [loefflerd/ModularFormDimensions](https://github.com/loefflerd/ModularFormDimensions) | 11 | Finite-dimensionality of modular forms spaces |
| [kckennylau/EllipticCurve](https://github.com/kckennylau/EllipticCurve) | 5 | Towards a general definition of elliptic curve over schemes |
| [daniele-bolla/leanproject](https://github.com/daniele-bolla/leanproject) | 3 | Topological Sine Curve: Connected but Not Path-Connected (Lean 4 Formalization) |
| [mmew-2022/Riemann_zeta](https://github.com/mmew-2022/Riemann_zeta) | 3 | Riemann zeta function |
| [laughinggas/bernoulli](https://github.com/laughinggas/bernoulli) | 1 | Bernoulli numbers |
| [jamesa9283/special-functions](https://github.com/jamesa9283/special-functions) | 1 | Special functions in Lean |
<!-- REPOS_TABLE_END -->

## Usage

### As a consumer

```bash
pip install git+https://github.com/mrdouglasny/lean-index.git
lean-index fetch-db mrdouglasny/lean-index-special-functions
lean-index search "Gamma function"
lean-index search --kind theorem --topic zeta-and-l-functions
lean-index stats
```

### Building locally

```bash
pip install git+https://github.com/mrdouglasny/lean-index.git
cd lean-index-special-functions
lean-index init                # Downloads Mathlib cache + creates topic-filtered DB
lean-index update              # Discovers repos + indexes + matches topics
lean-index stats
lean-index preview-topics      # Estimate impact of changing topics.yaml
```

## CI

The database is rebuilt weekly and published as a GitHub release. Download the latest with:

```bash
lean-index fetch-db mrdouglasny/lean-index-special-functions
```

## License

Copyright 2026 Michael R. Douglas. MIT License.
