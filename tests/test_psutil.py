from datasette.app import Datasette
import pytest


@pytest.mark.asyncio
async def test_datasette_psutil():
    ds = Datasette([], memory=True)
    response = await ds.client.get("/-/psutil")
    assert response.status_code == 200
    for fragment in (
        "process.open_files()",
        "process.net_connections()",
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
