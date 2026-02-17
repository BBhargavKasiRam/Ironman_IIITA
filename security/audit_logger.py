import datetime

def log_event(intent, status):

    with open("security/audit.log", "a") as f:
        f.write(
            f"{datetime.datetime.now()} | {status} | "
            f"{intent.dict()}\n"
        )
