"""
OpenClaw Web 管理界面 — FastAPI 入口
"""
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI(title="OpenClaw Web", version="0.1.0")

# 静态文件
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")

@app.get("/api/health")
async def health():
    """检查与 Gateway 的连通性"""
    import httpx
    try:
        async with httpx.AsyncClient() as client:
            r = await client.get("http://127.0.0.1:18789/", timeout=3)
            return {"gateway": "ok", "status_code": r.status_code}
    except Exception as e:
        return {"gateway": "error", "detail": str(e)}

@app.get("/api/status")
async def gateway_status():
    """Gateway systemd 状态"""
    import subprocess
    try:
        r = subprocess.run(
            ["systemctl", "--user", "is-active", "openclaw-gateway.service"],
            capture_output=True, text=True, timeout=5
        )
        pid = subprocess.run(
            ["ss", "-tlnp", "sport = :18789"],
            capture_output=True, text=True, timeout=3
        )
        return {
            "active": r.stdout.strip(),
            "pid": pid.stdout.strip()
        }
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=18080)
