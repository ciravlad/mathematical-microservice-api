import asyncio, time
import httpx

CONCURRENCY = 100
BASE_URL = "http://127.0.0.1:8000"

# Choose which endpoint to test by setting one of these:
ENDPOINT = "/pow"  # "/factorial" or "/fibonacci"
BODY = {"base": 2, "exponent": 1000}  # for /pow
# BODY   = {"number": 20}                # for /factorial
# BODY   = {"n": 200}                   # for /fibonacci


async def one_call(client, i):
    t0 = time.perf_counter()
    try:
        r = await client.post(f"{BASE_URL}{ENDPOINT}", json=BODY, timeout=30)
        return i, r.status_code, r.elapsed.total_seconds(), r.text[:120]
    except Exception as e:
        return i, "ERR", time.perf_counter() - t0, str(e)


async def run_batch():
    async with httpx.AsyncClient() as client:
        tasks = [one_call(client, i) for i in range(CONCURRENCY)]
        return await asyncio.gather(*tasks)


def summarize(tag, results):
    oks = [r for r in results if r[1] == 200]
    errs = [r for r in results if r[1] != 200]
    lats = [r[2] for r in oks]
    print(f"{tag}: total={len(results)} ok={len(oks)} err={len(errs)}")
    if lats:
        print(
            f"{tag}: avg={sum(lats)/len(lats):.4f}s min={min(lats):.4f}s"
            f" max={max(lats):.4f}s"
        )
    if errs:
        print(f"{tag}: sample errors: {errs[:3]}")


async def main():
    # Cold cache
    cold = await run_batch()
    summarize("COLD", cold)

    # Warm cache (same payload again)
    warm = await run_batch()
    summarize("WARM", warm)


if __name__ == "__main__":
    asyncio.run(main())
