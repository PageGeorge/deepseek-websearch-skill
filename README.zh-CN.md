# DeepSeek Web Search

一个 Claude Code Skill，使用 DeepSeek 内置的 `web_search_20250305` 工具进行网页搜索。搜索在服务端执行——无需客户端爬取。

这个仓库的设计目标是让 Agent 自己安装。作为人类用户，你通常只需要把下面这个仓库地址交给 Agent，并让它安装这个 Skill：

```text
https://github.com/PageGeorge/deepseek-websearch-skill
```

安装过程中，Agent 应该向你询问所需的 API key 和模型名称，然后把这些值写入本地安装后的 Skill 副本。

## 功能

- 向 DeepSeek 的 Anthropic 兼容 API 发送搜索请求。
- DeepSeek 在服务端执行搜索并返回综合性的回答。
- 不依赖外部搜索引擎（Google、Bing、DuckDuckGo）。
- 返回的是综合回答，而非仅仅是链接。
- 当用户需要核验时，可以要求返回来源 URL。

## 给用户

请让你的 Agent 使用上面的仓库地址安装这个 Skill。

Agent 会需要你提供两个值：

| 值 | 说明 |
|---|---|
| API key | 你的 DeepSeek API key |
| 模型名称 | 要使用的 DeepSeek 模型，例如 `deepseek-v4-pro` |

安装完成后，只需要提出需要搜索的问题。当 Agent 判断需要进行网页搜索时，这个 Skill 应该会自动触发。

## 给 Agent

将 `deepseek-websearch` 文件夹安装到用户的 Claude Code skills 目录。

个人级安装：

```bash
cp -r deepseek-websearch ~/.claude/skills/
```

项目级安装：

```bash
mkdir -p .claude/skills
cp -r deepseek-websearch .claude/skills/
```

如果 Python 依赖尚未安装，请安装 Anthropic SDK：

```bash
python3 -m pip install anthropic
```

如果用户电脑上只有 `python`，并且它指向 Python 3，可以把下面命令中的 `python3` 替换为 `python`。

然后配置本地已安装的副本，替换 `deepseek-websearch/scripts/search.py` 中的这些占位符：

| 占位符 | 替换为 |
|---|---|
| `{API_KEY}` | 用户的 DeepSeek API key |
| `{MODEL_NAME}` | 用户的 DeepSeek 模型名称 |

写入凭据后，不要提交或发布用户本地配置过的 `search.py`。

安装完成后重启 Claude Code，让 Skill 被重新发现。

## 验证

配置完成后运行：

```bash
python3 ~/.claude/skills/deepseek-websearch/scripts/search.py "今天天气怎么样"
```

如果脚本返回了基于搜索的回答，说明 Skill 已经可以使用。

如果 `python3` 不可用，请先确认 `python` 是 Python 3，再用 `python` 替代 `python3`。

## 工作方式

这个 Skill 提供了一个小型 Python 辅助脚本：

```text
deepseek-websearch/scripts/search.py
```

脚本向 DeepSeek 的 Anthropic 兼容 API (`https://api.deepseek.com/anthropic/v1/messages`) 发送带有 `web_search_20250305` 工具类型的请求。DeepSeek 在服务端执行搜索，并基于搜索结果返回综合性的回答。

## 安全提醒

- 只在用户本地安装后的副本中配置凭据。
- 不要把配置后的 API key 推送回 GitHub。
- 如果 API key 曾经公开分享或误提交，请先轮换 key 再继续使用。
- 对于高风险答案，请要求模型给出来源 URL，并核验关键结论。
