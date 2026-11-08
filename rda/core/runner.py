import asyncio
import logging
from .registry import CHECKS

class AsyncAuditRunner:
    def __init__(self, config):
        self.config = config
        self.results = []

    async def execute_check(self, check_instance):
        try:
            # Await if the module is async, otherwise run synchronously 
            if asyncio.iscoroutinefunction(check_instance.execute):
                return await check_instance.execute()
            else:
                return check_instance.execute()
        except Exception as e:
            logging.error(f"Execution error in {check_instance.__class__.__name__}: {str(e)}")
            return None

    async def run_all(self):
        tasks = []
        for check_cls in CHECKS:
            instance = check_cls(self.config)
            if instance.is_enabled():
                tasks.append(self.execute_check(instance))
        
        if not tasks:
            return []

        completed_results = await asyncio.gather(*tasks)
        self.results = [r for r in completed_results if r is not None]
        return self.results
