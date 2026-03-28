import asyncio
import os
from mtprotoproxy import ProxyServer

async def main():
    # Render сам назначит порт, мы его просто считываем
    port = int(os.environ.get("PORT", 8080))
    config = {
        "port": port,
        "users": {
            "admin": "11223344556677889900aabbccddeeff" # Ваш секрет
        }
    }
    server = ProxyServer(config)
    print(f"🚀 Прокси запущен на порту {port}")
    await server.run()

if __name__ == "__main__":
    asyncio.run(main())
