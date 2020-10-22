import falcon
import json


class HealthResource(object):
    async def on_get(self, req, resp):
        resp.body = "ok"
        resp.status = falcon.HTTP_200


app = falcon.API()

check_health = HealthResource()

app.add_route("/health", check_health)

