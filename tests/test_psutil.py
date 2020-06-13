from datasette.app import Datasette
import httpx
import pytest


@pytest.mark.asyncio
async def test_datasette_psutil():
    ds = Datasette([], memory=True)
    async with httpx.AsyncClient(app=ds.app()) as client:
        response = await client.get("http://localhost/-/psutil")
        assert 200 == response.status_code
        for fragment in (
            "process.open_files()",
            "process.connections()",
            "process.memory_info()",
            "process.cmdline()",
            "process.parents()",
            "process.threads()",
            "psutil.getloadavg()",
            "psutil.cpu_times(True)",
            "psutil.virtual_memory()",
            "list(psutil.process_iter())",
        ):
            assert fragment in response.text
