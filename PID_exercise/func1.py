from file_manager import locker

LOG = "target.log"

while True:
    print("new target: ", end="")
    newTarget = input()
    with locker(LOG, "w") as f:
        f.write(newTarget)