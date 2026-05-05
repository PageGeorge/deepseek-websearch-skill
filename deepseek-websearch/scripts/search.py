#!/usr/bin/env python3
"""Web search via DeepSeek's built-in web_search_20250305 tool."""

import sys
import anthropic

client = anthropic.Anthropic(
    base_url="https://api.deepseek.com/anthropic",
    api_key="{API_KEY}",
)

response = client.messages.create(
    model="deepseek-v4-pro",
    max_tokens=8192,
    system="You are an assistant for performing a web search tool use.",
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
