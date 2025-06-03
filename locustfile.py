from locust import HttpUser, task, between

class UsuarioSimulado(HttpUser):
    wait_time = between(1, 2)

    @task
    def visitar_pagina_principal(self):
        self.client.get("/")
