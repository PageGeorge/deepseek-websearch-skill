---
name: deepseek-websearch
description: Search the web using DeepSeek's built-in web_search tool (server-side execution). Use when the user asks to search, look up, verify, or find current information online. Also use when another web search tool returns empty or unreliable results.
allowed-tools: Bash(python3 *), Bash(python *)
---

# DeepSeek Web Search

Web search via DeepSeek's built-in `web_search_20250305` tool. Search is executed server-side — no client-side scraping needed.

## Usage

Prefer `python3`. If `python3` is unavailable, use `python` only if it is Python 3.

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/search.py "QUERY"
```

- `QUERY`: the search query (decided by Claude based on user's intent)

Write a focused query. Include date, location, product name, version, or source constraints when they matter. The script is instructed to include a `Sources:` section with markdown links.

When returning the result to the user, preserve the script's `Sources:` section and source URLs. Do not summarize away the links.

## How it works

The script sends a request to DeepSeek's Anthropic-compatible API with `web_search_20250305` tool. DeepSeek performs the search server-side and returns a comprehensive answer based on the search results.

Treat the output as a synthesized search answer. For high-stakes or disputed claims, verify the key details against the included sources.
