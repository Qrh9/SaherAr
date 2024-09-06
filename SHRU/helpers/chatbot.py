from .utils.extdl import install_pip
import asyncio

try:
    import randomstuff
except ModuleNotFoundError:
    install_pip("randomstuff.py")
    import randomstuff

from ..Config import Config

async def create_rs_client():
    return randomstuff.AsyncClient(api_key=Config.RANDOM_STUFF_API_KEY, version="4")

async def init_rs_client():
    try:
        rs_client = await create_rs_client()
        print("RandomStuff client created successfully")
        return rs_client
    except Exception as e:
        print(f"Error creating RandomStuff client: {str(e)}")
        return None

if __name__ == "__main__":
    asyncio.run(init_rs_client())
