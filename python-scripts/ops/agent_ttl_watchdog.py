import multiprocessing
import time
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)

class AgenticTTLWatchdog:
    """
    Infrastructure Resource Governor.
    Wraps autonomous agent executions in strict temporal constraints. 
    Violently terminates 'zombie' agents that enter infinite reasoning loops, 
    preventing massive compute drains and OOM crashes across the server fleet.
    """
    @staticmethod
    def _execute_wrapper(queue: multiprocessing.Queue, target_func: Callable, *args):
        try:
            result = target_func(*args)
            queue.put(result)
        except Exception as e:
            queue.put(e)

    @classmethod
    def execute_with_ttl(cls, target_func: Callable, max_execution_sec: int, *args) -> Any:
        queue = multiprocessing.Queue()
        process = multiprocessing.Process(target_func=cls._execute_wrapper, args=(queue, target_func, *args))
        
        logger.info(f"Deploying agent with strict TTL Watchdog ({max_execution_sec}s).")
        process.start()
        process.join(timeout=max_execution_sec)
        
        if process.is_alive():
            logger.critical("TTL EXCEEDED: Zombie Agent detected. Executing forced SIGKILL.")
            process.terminate()
            process.join()
            raise TimeoutError("Agent execution killed due to severe temporal violation.")
            
        if not queue.empty():
            return queue.get()
            
        return None
