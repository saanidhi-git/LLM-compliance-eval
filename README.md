# LLM Compliance Evaluation Framework (`llm-compliance-eval`)

An experimental evaluation framework designed to detect and quantify **Deceptive Compliance (Alignment Faking)** within Tool-Augmented LLM Agents.

## 1. Research Motivation
As Large Language Models scale, they frequently learn behavioral profiles that superficially mimic rule adherence in text while violating parameters under execution. This repository implements a multi-stage probing harness to measure the divergence between **Stated Strategic Intent** (what the model declares in natural language chain-of-thought) and **Enacted Operational Behavior** (the structural tool paths executed via function calling API triggers).

This approach isolates and measures behavioral gaps under targeted, rule-constrained enterprise operation parameters.

## 2. Tech Stack
* **Language/Environment:** Python 3.10+
* **Core Inference Engine:** OpenAI/Anthropic SDKs (structured function schemas)
* **Data Pipelines & Modeling:** Pandas, NumPy
* **Visualization Suite:** Matplotlib, Seaborn

## 3. Evaluation Pipeline Topology
The engine operates on a deterministic 2-stage verification framework:
1. **The Probing Stage:** System parameters present strict operational barriers along with high-pressure prompts to violate them. The model produces a raw text log stating reasoning constraints.
2. **The Execution Stage:** The model is evaluated along with its prior stated text output and explicit instruction tokens prompting tool use, verifying if the final programmatic function matched the stated baseline rule safety claims.

## 4. Setup & Usage Instructions

### Installation
```bash
git clone [https://github.com/saanidhi-git/llm-compliance-eval.git](https://github.com/saanidhi-git/llm-compliance-eval.git)
cd llm-compliance-eval
pip install -r requirements.txt