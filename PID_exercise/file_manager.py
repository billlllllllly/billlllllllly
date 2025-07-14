import contextlib, portalocker  

@contextlib.contextmanager
def locker(path, mode):
    """Open `path` with `mode`, holding an exclusive lock."""
    with open(path, mode) as f:
        portalocker.lock(f, portalocker.LOCK_EX)
        try:
            yield f                # locked region
        finally:
            portalocker.unlock(f)  # lock released automatically