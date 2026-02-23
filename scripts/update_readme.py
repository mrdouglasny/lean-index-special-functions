#!/usr/bin/env python3
"""Update README.md with current stats from index.db."""

import re
import sqlite3
from pathlib import Path

DB = Path("data/index.db")
README = Path("README.md")


def get_stats(db):
    """Get summary stats and repos table."""
    cur = db.cursor()

    total_matched = cur.execute(
        "SELECT COUNT(DISTINCT declaration_id) FROM topic_matches"
    ).fetchone()[0]

    repos_with_matches = cur.execute(
        """SELECT COUNT(DISTINCT r.id) FROM repos r
           JOIN declarations d ON d.repo_id = r.id
           JOIN topic_matches tm ON tm.declaration_id = d.id"""
    ).fetchone()[0]

    total_scanned = cur.execute("SELECT COUNT(*) FROM repos").fetchone()[0]
    total_decls = cur.execute("SELECT COUNT(*) FROM declarations").fetchone()[0]

    topics = cur.execute(
        """SELECT t.name, COUNT(DISTINCT tm.declaration_id)
           FROM topics t JOIN topic_matches tm ON tm.topic_id = t.id
           GROUP BY t.id ORDER BY COUNT(DISTINCT tm.declaration_id) DESC"""
    ).fetchall()

    all_repos = cur.execute(
        """SELECT r.url, r.name, r.description, COUNT(DISTINCT tm.declaration_id) as matches
           FROM repos r
           JOIN declarations d ON d.repo_id = r.id
           JOIN topic_matches tm ON tm.declaration_id = d.id
           GROUP BY r.id
           HAVING matches > 0
           ORDER BY matches DESC"""
    ).fetchall()

    return {
        "total_matched": total_matched,
        "repos_with_matches": repos_with_matches,
        "total_scanned": total_scanned,
        "total_decls": total_decls,
        "topics": topics,
        "all_repos": all_repos,
    }


TOPIC_NAMES = {
    "classical-special-functions": "Classical special functions",
    "exponential-logarithmic": "Exponential and logarithmic",
    "trigonometric": "Trigonometric",
    "zeta-and-l-functions": "Zeta and L-functions",
    "modular-forms": "Modular forms",
    "power-series": "Power series",
    "elliptic-curves": "Elliptic curves",
}

TOPIC_DESCS = {
    "classical-special-functions": "Gamma, Beta, digamma, Pochhammer, hypergeometric, Gaussian, Stirling, Hermite, elliptic functions",
    "exponential-logarithmic": "exp, log, rpow, sqrt, complex powers",
    "trigonometric": "sin, cos, tan, arctan, hyperbolic functions, Chebyshev polynomials",
    "zeta-and-l-functions": "Riemann/Hurwitz zeta, Dirichlet L-series, Euler products, Bernoulli numbers, arithmetic functions",
    "modular-forms": "modular/cusp forms, Eisenstein series, Jacobi theta, Dedekind eta, upper half plane",
    "power-series": "formal/multivariate power series, Hahn series, Fourier/Mellin transforms",
    "elliptic-curves": "Weierstrass curves, division polynomials, j-invariant",
}


def format_number(n):
    return f"{n:,}"


def build_summary(stats):
    lines = []
    lines.append(
        f"**{format_number(stats['total_matched'])} topic-matched declarations** "
        f"across **{stats['repos_with_matches']} repositories** "
        f"(scanned {stats['total_scanned']} repos, "
        f"{format_number(stats['total_decls'])} declarations)."
    )
    lines.append("")
    lines.append("Tracks Lean declarations related to:")
    for name, count in stats["topics"]:
        display = TOPIC_NAMES.get(name, name)
        desc = TOPIC_DESCS.get(name, "")
        lines.append(f"- **{display}** ({format_number(count)} matches): {desc}")
    return "\n".join(lines)


def build_table(all_repos):
    lines = []
    lines.append("| Repository | Topic Matches | Description |")
    lines.append("|-----------|:---:|-------------|")
    for url, name, desc, matches in all_repos:
        owner_repo = "/".join(url.rstrip("/").split("/")[-2:])
        short_desc = (desc or "")[:80]
        if len(desc or "") > 80:
            short_desc = short_desc.rsplit(" ", 1)[0] + "..."
        lines.append(f"| [{owner_repo}]({url}) | {format_number(matches)} | {short_desc} |")
    return "\n".join(lines)


def update_readme(stats):
    text = README.read_text()

    # Update stats block
    summary = build_summary(stats)
    text = re.sub(
        r"<!-- STATS_START -->.*?<!-- STATS_END -->",
        f"<!-- STATS_START -->\n{summary}\n<!-- STATS_END -->",
        text,
        flags=re.DOTALL,
    )

    # Update repos table
    table = build_table(stats["all_repos"])
    text = re.sub(
        r"<!-- REPOS_TABLE_START -->.*?<!-- REPOS_TABLE_END -->",
        f"<!-- REPOS_TABLE_START -->\n{table}\n<!-- REPOS_TABLE_END -->",
        text,
        flags=re.DOTALL,
    )

    README.write_text(text)
    print(f"Updated README.md: {format_number(stats['total_matched'])} matches, "
          f"{len(stats['all_repos'])} repos")


if __name__ == "__main__":
    if not DB.exists():
        print("No index.db found, skipping README update")
        exit(0)
    db = sqlite3.connect(str(DB))
    stats = get_stats(db)
    update_readme(stats)
    db.close()
