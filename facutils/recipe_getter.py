import json

import redis

from facutils import constants
from facutils import process_atoms


class RecipeTaskGetter:
    def __init__(self, redis_client: redis.StrictRedis):
        self.redis = redis_client

    def get_task(self, key: str) -> process_atoms.CraftTask:
        task_dict = json.loads(self.redis.get(key))
        return process_atoms.make_craftable_item(task_dict)
