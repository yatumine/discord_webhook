import sys
import requests
import json
import os
import chardet

def log_message(message):
    """メッセージを標準出力およびログファイルに出力"""
    with open("output.log", "a", encoding="utf-8") as log_file:
        log_file.write(message + "\n")
    print(message, flush=True)

def send_webhook(webhook_url, payload):
    try:
        response = requests.post(webhook_url, data=json.dumps(payload), headers={"Content-Type": "application/json"})
        if response.status_code == 204:
            log_message("メッセージが送信されました。")
        else:
            log_message(f"エラー: {response.status_code}")
            log_message(response.text)
    except Exception as e:
        log_message(f"例外が発生しました: {e}")

def read_payload_file(file_path):
    try:
        # エンコーディングを判定
        with open(file_path, 'rb') as file:
            raw_data = file.read()
            result = chardet.detect(raw_data)
            encoding = result['encoding']

        # 判定されたエンコーディングでファイルを読み込む
        with open(file_path, 'r', encoding=encoding) as file:
            data = file.read()

        # コメントを削除してJSONを解析
        data = json.loads(data)
        return data
    except Exception as e:
        log_message(f"payload.json の読み込み中にエラーが発生しました: {e}")
        sys.exit(1)

def main():
    payload_file = "payload.json"
    payload = None

    # payload.json の存在を確認して読み込む
    if os.path.exists(payload_file):
        log_message(f"{payload_file} を読み込んでいます...")
        payload = read_payload_file(payload_file)
    else:
        # payload.json が存在しない場合、content 引数が必須
        if len(sys.argv) < 3:
            log_message("エラー: payload.json が存在しません。content をコマンドライン引数で指定してください。")
            log_message("使用法: discord_webhook.exe <Webhook_URL> <content> [<username>]")
            sys.exit(1)
        payload = {
            "content": sys.argv[2],
            "embeds": []
        }

    if len(sys.argv) < 2:
        log_message("エラー: Webhook_URL が指定されていません。")
        log_message("使用法: discord_webhook.exe <Webhook_URL> <content> [<username>]")
        sys.exit(1)
    webhook_url = sys.argv[1]

    if len(sys.argv) >= 3:
        payload["content"] = sys.argv[2]
    if len(sys.argv) >= 4:
        payload["username"] = sys.argv[3]

    send_webhook(webhook_url, payload)

if __name__ == "__main__":
    main()
