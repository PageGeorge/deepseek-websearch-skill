# DeepSeek Web Search

A Claude Code skill that searches the web using DeepSeek's built-in `web_search_20250305` tool. Search is executed server-side — no client-side scraping needed.

This repository is designed to be installed by an agent. As a human user, you usually only need to give this repository URL to your agent and ask it to install the skill:

```text
https://github.com/PageGeorge/deepseek-websearch-skill
```

During installation, the agent should ask you for the required API key and model name, then write those values into the local copy of the skill.

## What It Does

- Sends a search query to DeepSeek's Anthropic-compatible API.
- DeepSeek performs the search on its server and returns a comprehensive answer.
- No dependency on external search engines (Google, Bing, DuckDuckGo).
- Returns synthesized answers, not just links.
- Can be asked to include source URLs when the user needs verification.

## For Users

Ask your agent to install this skill from the repository URL above.

The agent will need two values from you:

| Value | Description |
|---|---|
| API key | Your DeepSeek API key |
| Model name | The DeepSeek model to use, for example `deepseek-v4-pro` |

After installation, just ask a question that requires web search. The skill should trigger automatically when the agent determines that web search is needed.

## For Agents

Install the `deepseek-websearch` folder into the user's Claude Code skills directory.

Personal installation:

```bash
cp -r deepseek-websearch ~/.claude/skills/
```

Project-specific installation:

```bash
mkdir -p .claude/skills
cp -r deepseek-websearch .claude/skills/
```

Install the Python dependency if it is not already available:

```bash
python3 -m pip install anthropic
```

If the machine only provides `python` and it points to Python 3, use `python` instead of `python3`.

Then configure the local installed copy by replacing these placeholders in `deepseek-websearch/scripts/search.py`:

| Placeholder | Replace with |
|---|---|
| `{API_KEY}` | The user's DeepSeek API key |
| `{MODEL_NAME}` | The user's DeepSeek model name |

Do not commit or publish the user's configured `search.py` after inserting credentials.

Restart Claude Code after installation so the skill can be discovered.

## Verification

After configuration, run:

```bash
python3 ~/.claude/skills/deepseek-websearch/scripts/search.py "What is the weather today?"
```

If the script returns a search-based answer, the skill is ready.

If `python3` is unavailable, use `python` only after confirming it is Python 3.

## How It Works

The skill exposes a small Python helper script at:

```text
deepseek-websearch/scripts/search.py
```

The script sends a request to DeepSeek's Anthropic-compatible API (`https://api.deepseek.com/anthropic/v1/messages`) with the `web_search_20250305` tool type. DeepSeek performs the search on its server and returns a synthesized answer based on the search results.

## Safety Notes

- Configure credentials only in the user's local installed copy.
- Do not push configured API keys back to GitHub.
- If an API key has been shared publicly or committed by accident, rotate it before continuing.
- For high-stakes answers, ask the model to include source URLs and verify the important claims.
