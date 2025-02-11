import platform
import sys
from importlib.metadata import version, distributions

def print_system_info():
    print(f"Operating System: {platform.system()} {platform.release()}")
    print(f"OS Version: {platform.version()}")
    print(f"Architecture: {platform.architecture()[0]}")
    print(f"Python Version: {sys.version}")

    print("\nInstalled Packages:")
    installed_packages = sorted(
        [f"{dist.metadata['Name']}=={dist.version}" for dist in distributions()]
    )
    for package in installed_packages:
        print(package)

if __name__ == "__main__":
    print_system_info()
