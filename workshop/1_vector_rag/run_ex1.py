"""Roda o Exercício 1 de ponta a ponta e grava um relatório em markdown.

Uso (na pasta 1_vector_rag, com o venv ativo e `source ../env-gemini.sh`):
    python run_ex1.py            # ingere (se o índice estiver vazio) e roda tudo
    python run_ex1.py --ingest   # força a reingestão
"""
import argparse
import json
import subprocess
import sys
import urllib.request
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).parent
INDEX = "bbc-vector-chunks"
OPENSEARCH = "http://127.0.0.1:9200"
REPORT = HERE / "RESULTADOS-EX1.md"

QUESTIONS = [
    ("Passo 2: OpenAI", "How much did OpenAI purchase Windsurf for?"),
    ("Passo 3: Google", "How much did Google purchase Windsurf for?"),
    ("Passo 5: aquisição final", "Which company ultimately acquired Windsurf?"),
    (
        "Passo 6a: declara preferência",
        "For future answers, I prefer short bullet points. What was OpenAI's reported Windsurf deal?",
    ),
    (
        "Passo 6b: pergunta pela preferência (novo processo)",
        "What response format did I tell you I prefer in my previous question?",
    ),
]


def count_docs() -> int:
    try:
        with urllib.request.urlopen(f"{OPENSEARCH}/{INDEX}/_count", timeout=10) as r:
            return json.load(r)["count"]
    except Exception:
        return 0


def search_term(term: str) -> list[dict]:
    body = json.dumps(
        {"size": 10, "_source": {"excludes": ["embedding"]}, "query": {"match": {"text": term}}}
    ).encode()
    req = urllib.request.Request(
        f"{OPENSEARCH}/{INDEX}/_search", data=body, headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.load(r)["hits"]["hits"]


def run_query(question: str) -> str:
    proc = subprocess.run(
        [sys.executable, str(HERE / "query.py"), "--question", question],
        capture_output=True, text=True, cwd=HERE,
    )
    out = proc.stdout
    start = out.find("=" * 40)
    return (out[start:] if start >= 0 else out + proc.stderr[-800:]).strip()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ingest", action="store_true", help="força a reingestão")
    args = ap.parse_args()

    if args.ingest or count_docs() == 0:
        print("Ingerindo corpus...", flush=True)
        subprocess.run([sys.executable, str(HERE / "ingest.py")], cwd=HERE, check=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    lines = [
        "# Exercício 1: RAG baseline (resultados)",
        "",
        f"Gerado em {datetime.now():%Y-%m-%d %H:%M} por `run_ex1.py`. "
        f"Índice `{INDEX}`: **{count_docs()}** chunks.",
        "",
        "## Perguntas",
        "",
    ]
    for title, q in QUESTIONS:
        print(f"Rodando: {title}", flush=True)
        lines += [f"### {title}", "", f"`{q}`", "", "```text", run_query(q), "```", ""]

    lines += ["## Lacuna do corpus (busca textual direta no OpenSearch)", ""]
    for term in ("Windsurf", "Cognition"):
        hits = search_term(term)
        paths = ", ".join(sorted({h["_source"]["path"] for h in hits})) or "nenhum"
        lines.append(f"- `{term}`: **{len(hits)}** chunks ({paths})")
    lines += [
        "",
        "Leitura esperada: nenhum chunk indexado trata da aquisição pela Cognition "
        "(anúncio de 14/07/2025), então a pergunta 3 não tem evidência no corpus.",
        "",
    ]
    REPORT.write_text("\n".join(lines))
    print(f"\nRelatório: {REPORT}")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
