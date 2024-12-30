# About
DiscordへWebHookを行うためのexeファイルです。  
Windowsでのcurl.exeでは、マルチバイトを正常に処理できずWebHook時にエラーとなってしまうため、このexeからDiscordへWebHookを行います。

# Usage
1. 基本的な使い方  
    適当なディレクトリに配置し、コマンドプロンプトから呼び出してください。  
    例: C:\discord_webhook\discord_webhook.exe

    ```
    Usage: discord_webhook.exe <Webhook_URL> <content> [<username>]
    ```

    |引数          |説明                                       |
    |--------------|-------------------------------------------|
    | Webhook_URL  |Discordで発行したWebhookのURLを指定します。|
    | content      |送信するメッセージを指定します。|
    | username     |送信するユーザー名を指定します。（任意）|

1. 拡張  
    discord_webhook.exeと同じディレクトリに、payload.jsonという名前でjsonファイルを作成することにより、"avatar_url"や"embeds"を定義しておくことができます。

    https://discordjs.guide/popular-topics/embeds.html#embed-preview  
    例:
    ```
    {
        "username": "サーバー通知",
        "content": "message",
        "embeds": [
            {
                "title": "埋め込みタイトル",
                "description": "message",
                "color": 65280
            }
        ]
    }
    ```

# Build
1. このリポジトリをCloneまたはダウンロード

1. 必要なライブラリをインストール
    ```
    pip install -r requirements.txt
    ```

1. exeをビルド
    ```
    pyinstaller --onefile --console --clean --icon=image/icon.bmp discord_webhook.py
    ```