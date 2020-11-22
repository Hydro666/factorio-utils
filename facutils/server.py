import flask
import redis

from facutils import constants
from facutils import recipe_getter

app = flask.Flask(__name__)


@app.route("/get_recipe/<recipe_key>", methods=["GET"])
def get_recipe(recipe_key):
    return str(getter.get_task(recipe_key))


if __name__ == "__main__":
    redis_client = redis.StrictRedis(
        host="localhost", port=constants.REDIS_PORT, password="", decode_responses=True
    )
    getter = recipe_getter.RecipeTaskGetter(redis_client)
    app.run()
