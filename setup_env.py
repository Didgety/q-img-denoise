"""Create the project's Python 3.14 environment and install notebook dependencies."""

import subprocess
import sys
import venv
from pathlib import Path

if sys.version_info[:2] != (3, 14):
    raise SystemExit("Use Python 3.14 to reproduce the notebook environment.")

project_dir = Path(__file__).resolve().parent
env_dir = project_dir / ".venv"
python = env_dir / ("Scripts/python.exe" if sys.platform == "win32" else "bin/python")

if not python.exists():
    venv.create(env_dir, with_pip=True)

if sys.platform == "win32":
    # Match the CUDA 13.0 PyTorch build used for the original Windows run.
    subprocess.run(
        [str(python), "-m", "pip", "install", "torch==2.11.0",
         "--index-url", "https://download.pytorch.org/whl/cu130"],
        check=True,
    )

subprocess.run(
    [str(python), "-m", "pip", "install", "-r", str(project_dir / "requirements.txt")],
    check=True,
)
print(f"Select this Python interpreter as your notebook kernel: {python}")
