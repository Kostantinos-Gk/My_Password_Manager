class Application:

    def __init__(self, **kw):
        self.application_name = kw.get("application_name")
        self.url = kw.get("url")
        self.email = kw.get("email")
        self.password = kw.get("password")

    def display_app(self):
        return f" \n URL: {self.url} \n EMAIL : {self.email} \n PASSWORD : {self.password}"


