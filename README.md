# lean-index-special-functions

Topical index for special functions formalization in Lean 4. **[How to use this index in your project](https://github.com/mrdouglasny/lean-index/blob/main/docs/use-topic-index.md)**

<!-- STATS_START -->
**Building...** — run the CI workflow or build locally to populate stats.
<!-- STATS_END -->

Tracks Lean declarations related to:
- **Classical special functions**: Gamma, Beta, digamma, Pochhammer, hypergeometric, Gaussian, Stirling, Hermite, elliptic functions
- **Exponential and logarithmic**: exp, log, rpow, sqrt, complex powers
- **Trigonometric**: sin, cos, tan, arctan, hyperbolic functions, Chebyshev polynomials
- **Zeta and L-functions**: Riemann/Hurwitz zeta, Dirichlet L-series, Euler products, Bernoulli numbers, arithmetic functions
- **Modular forms**: modular/cusp forms, Eisenstein series, Jacobi theta, Dedekind eta, upper half plane
- **Power series**: formal/multivariate power series, Hahn series, Fourier/Mellin transforms
- **Elliptic curves**: Weierstrass curves, division polynomials, j-invariant

See [SELECTION.md](SELECTION.md) for exact selection criteria. See [REPOS.md](REPOS.md) for all indexed repositories.

## Indexed Repos

<!-- REPOS_TABLE_START -->
*Will be populated after first CI run.*
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
