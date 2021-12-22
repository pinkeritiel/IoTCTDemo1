from locust import HttpUser, TaskSet, task, between

class EntriesStep(TaskSet):
    @task
    def entries(self):
        self.client.get("/")

class EntriesTest(HttpUser):
    host = "https://www.demoblaze.com"
    tasks = [EntriesStep]
    wait_time = between(0.100, 0.500)
