# AI Context — Chunking Strategies Lab

## Project identity
- **Project:** PA Day 2 — Track B: RAG & Vector DBs
- **Subtopic:** Chunking Strategies
- **Type:** Hands-on AI learning lab / RAG engineering experiment
- **Status:** Implemented and deployed; evaluation and learning observations are ongoing.
- **Language:** Python
- **Recommended version:** Python 3.11
- **Modes:** Local CLI, local Streamlit, hosted Streamlit Community Cloud
- **Goal:** Compare practical document chunking approaches using open-source libraries and study how chunk boundaries affect retrieval.

## Project links
- **Run experience:** https://ai-daily-practice-chunking-strategies.streamlit.app/
- **GitHub source documentation:** https://github.com/atanuduttagupta/ai-daily-practice/tree/main/AI/chunking-strategies
- **Repository:** https://github.com/atanuduttagupta/ai-daily-practice
- **Project directory:** `AI/chunking-strategies/`

## Learning objectives
1. Understand why RAG systems split source documents into smaller chunks.
2. Compare chunk boundaries produced by different open-source chunking APIs.
3. Understand character-based, token-based, structure-aware, and semantic chunking.
4. Inspect chunk text and metadata rather than relying only on aggregate metrics.
5. Observe how chunking affects retrieval accuracy and retrieved context size.
6. Learn that the best strategy depends on document structure, query patterns, and evaluation results.

## Implemented chunking strategies
1. **Recursive character splitting — LangChain**
   - Uses `RecursiveCharacterTextSplitter`.
   - Tries configured separators in order to preserve paragraph and text boundaries while respecting a character-size target.
2. **Token-based splitting — LangChain**
   - Uses `TokenTextSplitter` and `tiktoken`.
   - Measures size in tokens, not characters. Character and token settings are not directly equivalent.
3. **Markdown structure-aware splitting — LangChain**
   - Uses `MarkdownHeaderTextSplitter` to capture heading hierarchy as metadata.
   - Applies a recursive splitter afterward to bound oversized sections.
4. **Semantic chunking — Chonkie**
   - Uses `SemanticChunker` with `minishlab/potion-base-8M`.
   - Uses semantic similarity to form meaning-oriented chunks.
   - `chonkie[model2vec]` is declared to install Chonkie's optional Model2Vec provider dependency.
   - If Chonkie cannot initialize, the other strategies continue and the Streamlit app surfaces the initialization message.

## Technical stack
- LangChain: `langchain-core`, `langchain-text-splitters`
- Tokenizer: `tiktoken`
- Semantic chunking: `chonkie[model2vec]`
- Dense retrieval embedding model: `sentence-transformers/all-MiniLM-L6-v2`
- Vector store: Qdrant Client, in-memory (`:memory:`)
- Lexical retrieval: `rank-bm25`
- UI: Streamlit
- Tabular display: pandas

No proprietary LLM API key is required. This iteration focuses on chunking and retrieval, not answer generation.

## Dataset and evaluation
The CLI and Streamlit app use a small built-in Acme Drive Help Centre document and six curated question/reference-answer pairs in the current repository version.

Metrics:
- **Chunk count:** Number of chunks created.
- **Answer coverage:** Fraction of reference answers present intact in at least one chunk, independent of retrieval ranking.
- **Hit@1:** Fraction of questions where the top retrieved chunk contains the complete reference answer.
- **Hit@k:** Fraction of questions where at least one of the top-k retrieved chunks contains the complete reference answer.
- **Average retrieved context characters:** Average total character count across the retrieved top-k chunks.

### Latest observed local CLI results
These are results shared during the learning session for the run configuration at that time; they are observations, not a permanent benchmark.

| Strategy | Chunks | Coverage | Hit@1 | Hit@k | Average context characters |
|---|---:|---:|---:|---:|---:|
| Recursive character | 8 | 0.50 | 0.50 | 0.50 | 737.17 |
| Token-based | 6 | 1.00 | 1.00 | 1.00 | 1008.50 |
| Markdown structure-aware | 9 | 1.00 | 1.00 | 1.00 | 628.67 |
| Chonkie semantic | 9 | 1.00 | 1.00 | 1.00 | 599.67 |

**Interpretation:** On this small curated set, token-based, Markdown-aware, and Chonkie semantic splitting achieved the same observed hit rates. Chonkie had the smallest average retrieved context among those three, while Markdown-aware splitting retains useful heading metadata. These results do not establish a universal winner. The test set is small, and context size alone does not measure answer quality.

## Run instructions
Run from `AI/chunking-strategies/`.

### Windows PowerShell setup
```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### CLI
```powershell
python main.py
python main.py --size 300 --overlap 60 --retriever bm25
python main.py --size 300 --overlap 60 --retriever vector
```

### Streamlit
```powershell
python -m streamlit run app.py
```

## Dependencies
The repository `requirements.txt` currently contains:
```text
streamlit>=1.40
pandas>=2.0
langchain-core>=0.3
langchain-text-splitters>=0.3
sentence-transformers>=3.0
qdrant-client>=1.12
rank-bm25>=0.2.2
chonkie[model2vec]>=0.5
tiktoken>=0.7
```

Notes:
- `tiktoken` is required by LangChain's `TokenTextSplitter`.
- `chonkie[model2vec]` installs the optional Model2Vec provider dependency.
- First use of Chonkie or Sentence Transformers may download models from Hugging Face.
- Hugging Face unauthenticated-download notices and Windows symlink-cache warnings do not necessarily indicate application failure.
- When Windows symlink support is unavailable, Hugging Face caching may use more disk space. Developer Mode can enable symlinks; it is not required to run the project.
- Python 3.11 is the recommended environment for this project.

## Current design boundaries
- Qdrant uses in-memory storage; vectors are not persisted between runs.
- Dense retrieval downloads and uses a local Sentence Transformers model.
- The current CLI exposes either BM25 or dense vector retrieval; hybrid retrieval and Reciprocal Rank Fusion (RRF) are not implemented.
- There is no LLM answer generation in this subtopic.
- Ollama and LangGraph are intentionally deferred to later learning days / a later agentic RAG sprint.
- The Acme Drive dataset is a controlled teaching example, not a production benchmark.

## Learning conclusions so far
- Chunk boundaries can determine whether a complete reference answer is contained in one chunk.
- A higher hit rate does not make a strategy best for every document type or workload.
- Markdown-aware chunking is useful when section hierarchy and heading metadata matter.
- Semantic chunking may produce compact, meaning-oriented chunks, but depends on model initialization and should be evaluated on representative data.
- Token-based splitting is useful when controlling token budgets matters; token counts are not directly comparable to character counts.
- More robust evaluation should include varied questions, boundary-sensitive questions, multi-section questions, paraphrases, chunk coherence inspection, and latency/resource measurements.

## Potential next learning steps
These are future ideas, not implemented features:
1. Inspect and compare actual chunk boundaries and metadata.
2. Expand the evaluation set with paraphrased, boundary-sensitive, and multi-section questions.
3. Test chunk sizes and overlaps systematically.
4. Evaluate multiple document types, including Markdown documentation and unstructured prose.
5. In later RAG topics, study BM25 versus dense retrieval, hybrid retrieval/RRF, reranking, persistent vector stores, and LLM answer generation.
6. In a later agentic RAG topic, explore Ollama and LangGraph.

## Guidance for future AI assistants
- Continue from this project; do not restart or replace it with a different architecture.
- Keep this subtopic focused on chunking and its effect on retrieval.
- Do not introduce RRF, Ollama generation, LangGraph, or other later-day topics unless explicitly requested.
- Distinguish observed metrics from general claims; six questions cannot prove a universal winner.
- Prefer open-source libraries and local-first workflows. Avoid proprietary API requirements.
- Give Windows PowerShell commands for local setup.
- Treat the Streamlit deployment as the public run experience and the GitHub directory as source documentation.
