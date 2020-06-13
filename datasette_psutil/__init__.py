import psutil
from datasette import hookimpl
from datasette.utils.asgi import Response


async def show_psutil():
    lines = []

    def info(code):
        lines.append(code)
        try:
            result = eval(code, {"process": process, "psutil": psutil,})
        except Exception as e:
            result = [e]
        if not isinstance(result, list):
            result = [result]
        lines.extend("  " + repr(r) for r in result)
        lines.append("")

    process = psutil.Process()
    info("process.open_files()")
    info("process.connections()")
    info("process.memory_info()")
    info("process.cmdline()")
    info("process.parents()")
    info("process.threads()")
    info("psutil.getloadavg()")
    info("psutil.cpu_times(True)")
    info("psutil.virtual_memory()")
    info("list(psutil.process_iter())")
    return Response.text("\n".join(lines))


@hookimpl
def register_routes():
    return [("^/-/psutil$", show_psutil)]
