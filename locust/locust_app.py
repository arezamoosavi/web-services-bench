from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):
    @task(5)
    def homepage(self):
        self.client.get("/health")

class User(HttpUser):
    tasks = [UserBehavior,]
    host = "http://localhost:8000"
    wait_time = between(1, 3)