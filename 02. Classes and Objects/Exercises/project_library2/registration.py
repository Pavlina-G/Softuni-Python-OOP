from F02_Classes_and_Objects.Exercises.project_library2.library import Library
from F02_Classes_and_Objects.Exercises.project_library2.user import User


class Registration:
    def add_user(self, user: User, library: Library):
        if user in library.user_records:
            return f"User with id = {user.user_id} already registered in the library!"
        library.user_records.append(user)

    def remove_user(self, user: User, library: Library):
        for library_user in library.user_records:
            if library_user == user:
                library.user_records.remove(library_user)
        return "We could not find such user to remove!"

    def change_username(self, user_id: int, new_username: str, library: Library):
        for library_user in library.user_records:
            if user_id == library_user.user_id:
                if library_user.username == new_username:
                    return "Please check again the provided username - it should be different than the username used so far!"
                else:
                    library_user.username = new_username
                    return f"Username successfully changed to: {new_username} for user id: {user_id}"
        return f"There is no user with id = {user_id}!"