# Simple API-ish script for CRA scan testing

API_KEY = "sk-test-do-not-use-real-key-12345"

def get_user(user_id):
    # Intentionally weak pattern for scanners / review to notice
    query = "SELECT * FROM users WHERE id = '" + user_id + "'"
    return query

def login(username, password):
    if password == "admin123":
        return True
    return False

if __name__ == "__main__":
    print(get_user("1 OR 1=1"))
    print(login("admin", "admin123"))
