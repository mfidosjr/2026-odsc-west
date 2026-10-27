# Exercício 1: RAG baseline (resultados)

Gerado em 2026-10-27 16:27 por `run_ex1.py`. Índice `bbc-vector-chunks`: **242** chunks.

## Perguntas

### Passo 2: OpenAI

`How much did OpenAI purchase Windsurf for?`

```text
========================================================================================
QUESTION: How much did OpenAI purchase Windsurf for?
========================================================================================

========================================================================================
ANSWER: OpenAI agreed to buy Windsurf for about $3 billion, though at the time of the report, the deal had not yet closed.


RAG Hits:
  - 600 | tech | score=0.9121
  - 601 | tech | score=0.8370
  - 038 | tech | score=0.7180
========================================================================================

Query time: 13.36s   (OpenSearch vector k-NN + LLM service generation)
Docs provided to LLM: 3
```

### Passo 3: Google

`How much did Google purchase Windsurf for?`

```text
========================================================================================
QUESTION: How much did Google purchase Windsurf for?
========================================================================================

========================================================================================
ANSWER: Google did not purchase Windsurf; it agreed to have neither a stake nor control in the company. Instead, Google is paying approximately **$2.4 billion** for Windsurf assets, talent, and a nonexclusive license to its technology. (Separately, OpenAI agreed to acquire Windsurf for about $3 billion).


RAG Hits:
  - 601 | tech | score=0.8682
  - 600 | tech | score=0.8370
  - 038 | tech | score=0.7291
========================================================================================

Query time: 13.35s   (OpenSearch vector k-NN + LLM service generation)
Docs provided to LLM: 3
```

### Passo 5: aquisição final

`Which company ultimately acquired Windsurf?`

```text
========================================================================================
QUESTION: Which company ultimately acquired Windsurf?
========================================================================================

========================================================================================
ANSWER: Based on the retrieved context, Windsurf was not fully acquired by either company:

* **OpenAI** agreed to buy Windsurf for about $3 billion, but the deal had not closed. 
* **Google** paid approximately $2.4 billion for a nonexclusive license to Windsurf's technology and to hire top talent (including its co-founders), but Google holds neither an ownership stake nor control over Windsurf, which continues to operate under an interim CEO.


RAG Hits:
  - 600 | tech | score=0.7885
  - 601 | tech | score=0.7621
  - 038 | tech | score=0.6957
========================================================================================

Query time: 19.74s   (OpenSearch vector k-NN + LLM service generation)
Docs provided to LLM: 3
```

### Passo 6a: declara preferência

`For future answers, I prefer short bullet points. What was OpenAI's reported Windsurf deal?`

```text
========================================================================================
QUESTION: For future answers, I prefer short bullet points. What was OpenAI's reported Windsurf deal?
========================================================================================

========================================================================================
ANSWER: * **Transaction:** OpenAI agreed to acquire AI-assisted coding tool Windsurf (formerly Codeium).
* **Value:** Approximately $3 billion, marking OpenAI's largest acquisition to date.
* **Status:** The deal had been agreed upon but was not yet closed at the time of reporting.
* **Objective:** To enhance ChatGPT's coding capabilities amidst increasing competition.


RAG Hits:
  - 600 | tech | score=0.8450
  - 601 | tech | score=0.7915
  - 114 | tech | score=0.6881
========================================================================================

Query time: 14.94s   (OpenSearch vector k-NN + LLM service generation)
Docs provided to LLM: 3
```

### Passo 6b: pergunta pela preferência (novo processo)

`What response format did I tell you I prefer in my previous question?`

```text
========================================================================================
QUESTION: What response format did I tell you I prefer in my previous question?
========================================================================================

========================================================================================
ANSWER: I don't know.


RAG Hits:
  - 118 | tech | score=0.6668
  - 056 | tech | score=0.6655
  - 009 | tech | score=0.6584
========================================================================================

Query time: 15.73s   (OpenSearch vector k-NN + LLM service generation)
Docs provided to LLM: 3
```

## Lacuna do corpus (busca textual direta no OpenSearch)

- `Windsurf`: **2** chunks (tech/600.txt, tech/601.txt)
- `Cognition`: **0** chunks (nenhum)

Leitura esperada: nenhum chunk indexado trata da aquisição pela Cognition (anúncio de 14/07/2025), então a pergunta 3 não tem evidência no corpus.
