# Selection Criteria

This document describes exactly which Lean declarations are included in this index. Only declarations matching at least one criterion below are indexed — everything else is excluded. Declarations containing `sorry` are excluded.

## Topic: classical-special-functions

### Module prefixes (confidence: 1.0)
- `Mathlib.Analysis.SpecialFunctions.Gamma.*` — Gamma, Beta, digamma, Bohr-Mollerup
- `Mathlib.Analysis.SpecialFunctions.Elliptic.*` — Weierstrass elliptic functions
- `Mathlib.Analysis.SpecialFunctions.OrdinaryHypergeometric` — hypergeometric functions
- `Mathlib.Analysis.SpecialFunctions.Pochhammer` — rising/falling factorials
- `Mathlib.Analysis.SpecialFunctions.Gaussian.*` — Gaussian integrals, Poisson summation
- `Mathlib.Analysis.SpecialFunctions.Stirling` — Stirling's approximation
- `Mathlib.Analysis.SpecialFunctions.Integrals.*` — integrals of special functions
- `Mathlib.RingTheory.Polynomial.Hermite.*` — Hermite polynomials

### Type mentions (confidence: 0.8)
- `Real.Gamma`, `Complex.Gamma`, `Real.Beta`, `Complex.Beta`
- `Real.digamma`, `Complex.digamma`
- `ascPochhammer`, `descPochhammer`
- `ordinaryHypergeometric`, `WeierstrassEllipticFunction`

### Name patterns (confidence: 0.6)
- `.*Gamma.*`, `.*BetaF.*`, `.*Bessel.*`, `.*Hypergeometric.*`
- `.*Pochhammer.*`, `.*Stirling.*`, `.*Hermite.*`, `.*Digamma.*`

## Topic: exponential-logarithmic

### Module prefixes (confidence: 1.0)
- `Mathlib.Analysis.SpecialFunctions.Exp*` — exponential functions
- `Mathlib.Analysis.SpecialFunctions.Log.*` — logarithms (real, complex, ENNReal)
- `Mathlib.Analysis.SpecialFunctions.Pow.*` — power functions, rpow
- `Mathlib.Analysis.SpecialFunctions.Sqrt` — square root
- `Mathlib.Data.Complex.Exponential` — complex exponential

### Type mentions (confidence: 0.8)
- `Real.exp`, `Complex.exp`, `Real.log`, `Complex.log`
- `Real.rpow`, `NNReal.rpow`, `Complex.cpow`, `Real.sqrt`

## Topic: trigonometric

### Module prefixes (confidence: 1.0)
- `Mathlib.Analysis.SpecialFunctions.Trigonometric.*` — sin, cos, tan, arctan, Euler sine product, Chebyshev
- `Mathlib.Analysis.SpecialFunctions.Arcosh` — inverse hyperbolic cosine
- `Mathlib.Analysis.SpecialFunctions.Arsinh` — inverse hyperbolic sine
- `Mathlib.Analysis.SpecialFunctions.Artanh` — inverse hyperbolic tangent
- `Mathlib.RingTheory.Polynomial.Chebyshev` — Chebyshev polynomials

### Type mentions (confidence: 0.8)
- `Real.sin`, `Real.cos`, `Real.tan`, `Real.arctan`
- `Complex.sin`, `Complex.cos`
- `Real.cosh`, `Real.sinh`, `Real.sinc`
- `Polynomial.Chebyshev.T`, `Polynomial.Chebyshev.U`

## Topic: zeta-and-l-functions

### Module prefixes (confidence: 1.0)
- `Mathlib.NumberTheory.LSeries.*` — L-series, Hurwitz/Riemann zeta, Dirichlet continuation
- `Mathlib.NumberTheory.ArithmeticFunction.*` — Mobius, von Mangoldt, Carmichael
- `Mathlib.NumberTheory.EulerProduct.*` — Euler product formulas
- `Mathlib.NumberTheory.Bernoulli*` — Bernoulli numbers and polynomials
- `Mathlib.NumberTheory.Harmonic.*` — harmonic numbers, Euler-Mascheroni
- `Mathlib.NumberTheory.ZetaValues` — special values of zeta
- `Mathlib.NumberTheory.NumberField.DedekindZeta` — Dedekind zeta

### Type mentions (confidence: 0.8)
- `riemannZeta`, `hurwitzZeta`, `LSeries`, `LSeriesSummable`
- `DirichletCharacter`, `ArithmeticFunction`
- `EulerProduct`, `eulerMascheroniConstant`, `bernoulli`

### Name patterns (confidence: 0.6)
- `.*Zeta.*`, `.*Bernoulli.*`, `.*LSeries.*`, `.*Dirichlet.*`
- `.*EulerProduct.*`, `.*VonMangoldt.*`, `.*Moebius.*`

## Topic: modular-forms

### Module prefixes (confidence: 1.0)
- `Mathlib.NumberTheory.ModularForms.*` — modular forms, cusp forms, Eisenstein series, Jacobi theta, Dedekind eta
- `Mathlib.Analysis.Complex.UpperHalfPlane.*` — upper half plane infrastructure

### Type mentions (confidence: 0.8)
- `ModularForm`, `CuspForm`, `SlashInvariantForm`
- `EisensteinSeries`, `UpperHalfPlane`, `jacobiTheta`

### Name patterns (confidence: 0.6)
- `.*ModularForm.*`, `.*CuspForm.*`, `.*Eisenstein.*`
- `.*JacobiTheta.*`, `.*DedekindEta.*`

## Topic: power-series

### Module prefixes (confidence: 1.0)
- `Mathlib.RingTheory.PowerSeries.*` — formal power series
- `Mathlib.RingTheory.MvPowerSeries.*` — multivariate power series
- `Mathlib.RingTheory.HahnSeries.*` — Hahn series
- `Mathlib.Analysis.Fourier.*` — Fourier transforms
- `Mathlib.Analysis.MellinTransform` — Mellin transform
- `Mathlib.Analysis.MellinInversion` — Mellin inversion

### Type mentions (confidence: 0.8)
- `PowerSeries`, `MvPowerSeries`, `HahnSeries`, `FourierTransform`

## Topic: elliptic-curves

### Module prefixes (confidence: 1.0)
- `Mathlib.AlgebraicGeometry.EllipticCurve.*` — elliptic curve theory
- `Mathlib.NumberTheory.EllipticDivisibilitySequence` — division sequences

### Type mentions (confidence: 0.8)
- `EllipticCurve`, `WeierstrassCurve`

---

## How selection works

1. **Mathlib declarations** are downloaded from the official docs cache (~384K total).
2. **Non-Mathlib repos** are cloned and parsed via regex extraction.
3. Each declaration is tested against the criteria above.
4. Only declarations matching **at least one criterion** from **any topic** are stored.
5. Declarations containing `sorry` in their body are **excluded**.
6. Confidence scores: **1.0** (module prefix) > **0.8** (type mention) > **0.6** (name pattern).

## Previewing changes

```bash
lean-index preview-topics                                    # current topics.yaml
lean-index preview-topics --config-file modified-topics.yaml # proposed changes
```
