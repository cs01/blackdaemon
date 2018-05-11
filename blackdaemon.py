import argparse
import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

VERSION = '0.1.0.1'
extra_black_args = []


def run_black(path):
    subprocess.run(["black", *extra_black_args, path])


class BlackHandler(FileSystemEventHandler):

    def on_modified(self, event):
        if event.src_path.endswith(".py"):
            run_black(event.src_path)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "path", help="path of file or directory to watch for changes", nargs="?"
    )
    recurse_parser = parser.add_mutually_exclusive_group()
    recurse_parser.add_argument(
        "--recursive",
        action="store_true",
        help="recursively watch director for changes (default)",
    )
    recurse_parser.add_argument("--non-recursive", action="store_true")
    parser.add_argument(
        "--no-run-on-start",
        action="store_true",
        help="run black only when files change, not on startup.",
    )
    parser.add_argument(
        "-q",
        "--quiet",
        help="don't emit non-error messages to stderr. Errors are still emitted, silence those with 2>/dev/null",
        action="store_true",
    )
    parser.add_argument(
        "-v",
        "--version",
        help="print version of blackdaemon and black, then exit",
        action="store_true",
    )

    args = parser.parse_args()
    if args.version:
        print(F"blackdaemon, version {VERSION}")
        subprocess.run(["black", "--version"])
        exit(0)
    if not args.path:
        print("Missing required argument path. See blackdaemon --help.")
        exit(1)

    path = args.path
    if args.quiet:
        extra_black_args.append("--quiet")

    event_handler = BlackHandler()
    observer = Observer()
    recursive = (args.non_recursive is False)
    observer.schedule(event_handler, path, recursive=recursive)
    if not args.no_run_on_start:
        run_black(path)
    observer.start()
    try:
        while True:
            time.sleep(0.5)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    main()
