# GitHub 发布前检查

公开发布前，请确认仓库里没有私人信息。

## 必查内容

不要提交：

- API Key
- 飞书 app_id、app_secret、tenant token
- DeepSeek 或 OpenAI Key
- 私人 Obsidian 绝对路径
- 真实飞书多维表格链接
- 真实飞书知识库链接
- 未公开当事人隐私信息
- 未授权的全文转载
- 付费内容全文

## 推荐检查关键词

```text
sk-
app_secret
tenant_access_token
open-apis
feishu.cn/base/
feishu.cn/wiki/
/Users/
/home/
C:\\Users
api_key
API_KEY
DeepSeek
OpenAI
```

## 发布前命令

可以运行：

```bash
python3 scripts/check_publication_safety.py .
```

如果脚本报告疑似敏感内容，先人工检查再发布。

## 建议仓库名

```text
story-material-accumulation-workflow
```

或中文：

```text
sucai-jilei-chendian-workflow
```

## 建议简介

```text
一套 Codex + Obsidian + 飞书多维表格 + 飞书知识库的故事素材收集、评级、精选和自检流程。
```

