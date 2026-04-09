import os
import datetime
from company_data import FILENAME, INITIAL_CONTENT
 
#  ROLE DEFINITIONS
 
ROLES = {
    "admin":   {"read", "write", "delete", "manage"},
    "manager": {"read", "write", "delete"},
    "editor":  {"read", "write"},
    "viewer":  {"read"},
    "auditor": {"read", "audit"},
    "guest":   set(),
}
 
#  USER DATABASE
 
USERS = {
    "alice": "admin",
    "bob":   "manager",
    "carol": "editor",
    "dave":  "viewer",
    "eve":   "auditor",
    "frank": "guest",
}
 
#  CORE FUNCTIONS
 
def ensure_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w", encoding="utf-8") as f:
            f.write(INITIAL_CONTENT)
        print(f"[+] Protected file created: {FILENAME}\n")
 
def has_permission(user, perm):
    role = USERS.get(user)
    if not role:
        return False
    return perm in ROLES.get(role, set())
 
def add_user(username, role):
    if role not in ROLES:
        print(f"[!] Unknown role: '{role}'")
        print(f"    Available roles: {', '.join(ROLES.keys())}")
        return
    if username in USERS:
        print(f"[!] User '{username}' already exists with role: {USERS[username]}")
        return
    USERS[username] = role
    print(f"[+] User '{username}' added with role '{role}'")
 
def read_file(user):
    if not has_permission(user, "read"):
        print(f"[DENIED] {user} (role={USERS.get(user)}) cannot read")
        return
    print(f"[GRANTED] {user} reading {FILENAME}:")
    print("-" * 40)
    with open(FILENAME, "r", encoding="utf-8") as f:
        print(f.read())
    print("-" * 40)
 
def write_file(user, text):
    if not has_permission(user, "write"):
        print(f"[DENIED] {user} (role={USERS.get(user)}) cannot write")
        return
    ts = datetime.datetime.now().isoformat(sep=" ", timespec="seconds")
    with open(FILENAME, "a", encoding="utf-8") as f:
        f.write(f"\n[{ts}] {user}: {text}\n")
    print(f"[GRANTED] {user} wrote to {FILENAME}")
 
def delete_file(user):
    if not has_permission(user, "delete"):
        print(f"[DENIED] {user} (role={USERS.get(user)}) cannot delete")
        return
    if os.path.exists(FILENAME):
        os.remove(FILENAME)
        print(f"[GRANTED] {user} deleted {FILENAME}")
    else:
        print("[!] File not found")
 
def show_state():
    print("\nRoles and permissions:")
    print("-" * 40)
    for r, perms in ROLES.items():
        print(f"  {r:<10} {', '.join(sorted(perms)) or 'none'}")
    print("\nCurrent users:")
    print("-" * 40)
    for u, r in USERS.items():
        print(f"  {u:<12} {r}")
    print()
 
#  MAIN
 
def execute():
    ensure_file()
 
    while True:
        print("\n  ROLE-BASED ACCESS CONTROL SYSTEM")
        print("  ----------")
        print("  1. Show all users and roles")
        print("  2. Add a new user")
        print("  3. Read file")
        print("  4. Write to file")
        print("  5. Delete file")
        print("  6. Exit")
        print()
 
        choice = input("  Enter choice: ").strip()
 
        if choice == "1":
            show_state()
 
        elif choice == "2":
            username = input("  Enter new username: ").strip()
            print(f"  Available roles: {', '.join(ROLES.keys())}")
            role = input("  Enter role: ").strip()
            add_user(username, role)
 
        elif choice == "3":
            username = input("  Enter username: ").strip()
            if username not in USERS:
                print(f"[!] User '{username}' not found")
            else:
                ensure_file()
                read_file(username)
 
        elif choice == "4":
            username = input("  Enter username: ").strip()
            if username not in USERS:
                print(f"[!] User '{username}' not found")
            else:
                text = input("  Enter text to write: ").strip()
                ensure_file()
                write_file(username, text)
 
        elif choice == "5":
            username = input("  Enter username: ").strip()
            if username not in USERS:
                print(f"[!] User '{username}' not found")
            else:
                delete_file(username)
 
        elif choice == "6":
            print("\n  Exiting RBAC system. Goodbye.")
            break
 
        else:
            print("  [!] Invalid choice. Please enter 1-6.")
 
if __name__ == "__main__":
    execute()
 




