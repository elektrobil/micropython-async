# ms_timer_test.py Test/demo program for MillisecTimer

import uasyncio as asyncio
import utime
import ms_timer

async def timer_test(n):
    timer = ms_timer.MillisecTimer()
    while True:
        t = utime.ticks_ms()
        await timer(30)
        print(n, utime.ticks_diff(utime.ticks_ms(), t))
        await asyncio.sleep(0.5 + n/5)

async def foo():
    while True:
        await asyncio.sleep(0)
        utime.sleep_ms(10)  # Emulate slow processing

def test(fast_io=True):
    loop = asyncio.get_event_loop(ioq_len=6 if fast_io else 0)
    for _ in range(10):
        loop.create_task(foo())
    for n in range(3):
        loop.create_task(timer_test(n))
    loop.run_forever()

print('Run test() to test fast I/O, test(False) to test normal I/O.')
