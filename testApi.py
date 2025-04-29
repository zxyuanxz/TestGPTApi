import requests

# API 基础信息
API_URL = "https://xxxx.com/v1/chat/completions"
API_KEY = "sk-xxxx"

# 要测试的模型列表
models_to_test = [
    "gpt-4.1",
    "gpt-4.1-mini",
    "gpt-4o-mini",
    "gpt-4.1-nano",
    "deepseek-v3",
    "deepseek-reasoner",
    "deepseek-r1",
    "deepseek-chat",
    "moonshot-v1-128k",
    "moonshot-v1-32k",
    "moonshot-v1-8k"
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
<<<<<<< HEAD
        print(f"❌ 解析失败：{e}")
=======
        print(f"❌ 解析失败：{e}")
>>>>>>> 18af329 (Initial commit)
