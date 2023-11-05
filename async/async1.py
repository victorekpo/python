# SuperFastPython.com
# example of asynchronous programming with asyncio
import asyncio

# define a coroutine to run as a task
async def task_coroutine():
    # report a message
    print('Hello from the task')
    # sleep a moment
    await asyncio.sleep(1)
    # report another message
    print('Task is all done')

# entry point coroutine
async def main():
    # create the task coroutine
    coro = task_coroutine()
    # wrap in a task object and schedule execution
    task = asyncio.create_task(coro)
    # suspend a moment to allow the task to run
    await asyncio.sleep(0)
    # do other things, like report a message
    print('Main is doing other things...')
    # wait for the task to complete
    await task

# entry point into the program
asyncio.run(main())