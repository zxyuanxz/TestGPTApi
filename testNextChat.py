import requests
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from time import sleep

API_URL = "https://xxx.com/api/openai/v1/chat/completions"
HEADERS = {
    "Authorization": "Bearer nk-xxxx!",
    "Content-Type": "application/json",
    "Accept": "application/json, text/event-stream"
}

# 要测试的模型列表
models = [
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
    
    # OpenAi
    "gpt-3.5-turbo", "gpt-3.5-turbo-1106", "gpt-3.5-turbo-0125",
    "gpt-4-turbo", "gpt-4-turbo-preview", "gpt-4.1", "gpt-4o",
    "gpt-4.1-2025-04-14", "gpt-4o-2024-05-13", "gpt-4.1-mini",
    "gpt-4o-2024-08-06", "gpt-4.1-mini-2025-04-14", "gpt-4o-2024-11-20",
    "chatgpt-4o-latest", "gpt-4.1-nano", "gpt-4o-mini", "gpt-4.1-nano-2025-04-14",
    "gpt-4o-mini-2024-07-18", "gpt-4.5-preview", "gpt-4.5-preview-2025-02-27",
    "gpt-4o-turbo-2024-04-09", "dall-e-3", "o1-mini", "o1-preview", "o3-mini", "o3"
]

PROMPT = "请用一句话介绍你自己。"

def query_model(model_name, retry=2):
    """向指定模型发送请求，返回响应内容"""

    payload = {
        "model": model_name,
        "messages": [
            {"role": "system", "content": "你是一个 AI 助手"},
            {"role": "user", "content": PROMPT}
        ],
        "temperature": 0.5,
        "top_p": 1,
        "max_tokens": 500,
        "stream": True
    }

    for attempt in range(retry + 1):
        try:
            response = requests.post(API_URL, headers=HEADERS, json=payload, stream=True, timeout=30)
            if response.status_code != 200:
                raise Exception(f"HTTP {response.status_code}: {response.text}")

            full_text = ""
            for line in response.iter_lines():
                if line:
                    decoded = line.decode("utf-8")
                    if decoded.startswith("data: "):
                        data = decoded[6:]
                        if data.strip() == "[DONE]":
                            break
                        try:
                            content = json.loads(data)["choices"][0]["delta"].get("content", "")
                            full_text += content
                        except Exception as e:
                            continue
            return model_name, full_text
        except Exception as e:
            if attempt < retry:
                sleep(1)
            else:
                return model_name, f"❌ 请求失败：{str(e)}"

def run_batch_query():
    results = {}
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(query_model, model) for model in models]

        for future in as_completed(futures):
            model_name, reply = future.result()
            results[model_name] = reply
            print(f"✅ {model_name}:\n{reply}\n{'-'*60}")

    return results

if __name__ == "__main__":
<<<<<<< HEAD
    all_results = run_batch_query()
=======
    all_results = run_batch_query()
>>>>>>> 18af329 (Initial commit)
