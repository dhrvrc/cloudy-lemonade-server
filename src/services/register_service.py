

class RegisterService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def register(self, user: User):
        self.user_repository.save(user)