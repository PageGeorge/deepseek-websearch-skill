#!/usr/bin/env python3
"""Web search via DeepSeek's built-in web_search_20250305 tool."""

import sys
import anthropic

client = anthropic.Anthropic(
    base_url="https://api.deepseek.com/anthropic",
    api_key="{API_KEY}",
)

response = client.messages.create(
    model="{MODEL_NAME}",
    max_tokens=8192,
    system=(
        "You are an assistant for performing web search. "
        "After answering, include a Sources section at the end with relevant "
        "source URLs as markdown links in the format [Title](URL). "
        "Do not omit source URLs."
    ),
    tools=[{
        "type": "web_search_20250305",
        "name": "web_search",
        "max_uses": 8,
    }],
    messages=[{
        "role": "user",
        "content": sys.argv[1],
    }],
)

for block in response.content:
    if block.type == "text":
        print(block.text)
