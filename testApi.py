import requests

# API 基础信息
API_URL = "https://xxxx.com/v1/chat/completions"
API_KEY = "sk-xxxx"

# 要测试的模型列表
models_to_test = [
   # Google Gemini
    "gemini-1.0-pro", "gemini-1.5-pro-latest", "gemini-1.5-flash-latest",
    "gemini-pro-vision", "gemini-1.5-pro", "gemini-1.5-pro-002",
    "gemini-exp-1114", "gemini-1.5-pro-exp-0827", "gemini-exp-1121",
    "learnlm-1.5-pro-experimental", "gemini-1.5-flash-8b-latest",
    "gemini-1.5-flash", "gemini-1.5-flash-8b", "gemini-2.0-pro-exp-02-05",

    # Claude (Anthropic)
    "claude-instant-1.2", "claude-2.0", "claude-2.1",
    "claude-3-sonnet-20240229", "claude-3-opus-20240229", "claude-3-haiku-20240307",
    "claude-3-5-sonnet-20240620", "claude-3-5-haiku-20241022", "claude-3-5-sonnet-20241022",
    "claude-3-5-haiku-latest", "claude-3-5-sonnet-latest", "claude-3-opus-latest",
    "claude-3-7-sonnet-20250219",

    # XAI Grok
    "grok-beta", "grok-2", "grok-2-1212", "grok-2-latest",
    "grok-vision-beta", "grok-2-vision-1212", "grok-2-vision", "grok-2-vision-latest",

    # ChatGLM
    "glm-4-plus", "glm-4-0520", "glm-4", "glm-4-air", "glm-4-airx"
    
    # ChatGPT
    "gpt-3.5-turbo", "gpt-3.5-turbo-1106", "gpt-3.5-turbo-0125",
    "gpt-4-turbo", "gpt-4-turbo-preview", "gpt-4.1", "gpt-4o",
    "gpt-4.1-2025-04-14", "gpt-4o-2024-05-13", "gpt-4.1-mini",
    "gpt-4o-2024-08-06", "gpt-4.1-mini-2025-04-14", "gpt-4o-2024-11-20",
    "chatgpt-4o-latest", "gpt-4.1-nano", "gpt-4o-mini", "gpt-4.1-nano-2025-04-14",
    "gpt-4o-mini-2024-07-18", "gpt-4.5-preview", "gpt-4.5-preview-2025-02-27",
    "gpt-4o-turbo-2024-04-09", "dall-e-3", "o1-mini", "o1-preview", "o3-mini", "o3"
]

# 测试提示词
test_prompt = "请用一句话介绍一下你自己。"

# 请求头
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

# 测试每个模型
for model in models_to_test:
    print(f"\n🔍 正在测试模型：{model}")
    
    payload = {
        "model": model,
        "messages": [
            {"role": "user", "content": test_prompt}
        ],
        "temperature": 0.7
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=20)
        response.raise_for_status()
        data = response.json()

        # 打印模型返回的内容
        reply = data.get("choices", [{}])[0].get("message", {}).get("content", "⚠️ 无返回内容")
        print(f"✅ 回复：{reply}")

    except requests.exceptions.RequestException as e:
        print(f"❌ 请求失败：{e}")
    except Exception as e:
        print(f"❌ 解析失败：{e}")