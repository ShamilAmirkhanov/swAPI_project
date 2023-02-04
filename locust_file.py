from locust import HttpUser, TaskSet, task


class UserBehavior(TaskSet):
    # runs one time for each user
    def on_start(self):
        self.client.get("/")

    @task
    def people(self):
        self.client.get("/people/4")


class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    min_wait = 1000
    max_wait = 2000

# locust -f locust_file.py --host=http://127.0.0.1:8000
