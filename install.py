from pathlib import Path

import shutil
import sys
import json
import re

from configure import configure_ocr_model


working_dir = Path(__file__).parent
install_path = working_dir / Path("install")
version = len(sys.argv) > 1 and sys.argv[1] or "v0.0.1"


def install_deps():
    if not (working_dir / "deps" / "bin").exists():
        print('Please download the MaaFramework to "deps" first.')
        print('请先下载 MaaFramework 到 "deps"。')
        sys.exit(1)

    shutil.copytree(
        working_dir / "deps" / "bin",
        install_path,
        ignore=shutil.ignore_patterns(
            "*MaaDbgControlUnit*",
            "*MaaThriftControlUnit*",
            "*MaaRpc*",
            "*MaaHttp*",
        ),
        dirs_exist_ok=True,
    )
    shutil.copytree(
        working_dir / "deps" / "share" / "MaaAgentBinary",
        install_path / "MaaAgentBinary",
        dirs_exist_ok=True,
    )


def install_resource():
    configure_ocr_model()

    shutil.copytree(
        working_dir / "assets" / "resource",
        install_path / "resource",
        dirs_exist_ok=True,
    )
    shutil.copy2(
        working_dir / "assets" / "interface.json",
        install_path,
    )

    with open(install_path / "interface.json", "r", encoding="utf-8") as f:
        interface = json.load(f)

    interface["version"] = version

    with open(install_path / "interface.json", "w", encoding="utf-8") as f:
        json.dump(interface, f, ensure_ascii=False, separators=(",", ":"))


def install_chores():
    shutil.copy2(
        working_dir / "README.md",
        install_path,
    )
    shutil.copy2(
        working_dir / "LICENSE",
        install_path,
    )


def install_agent():
    shutil.copytree(
        working_dir / "assets" / "agent",
        install_path / "agent",
        dirs_exist_ok=True,
    )


def load_jsonc(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        raw = f.read()
    raw = re.sub(r"\/\/.*", "", raw)
    raw = re.sub(r"\/\*[\s\S]*?\*\/", "", raw)
    return json.loads(raw)


def minify_pipelines():
    pipeline_dir = install_path / "resource" / "pipeline"

    for pipeline_file in pipeline_dir.glob("*.json"):
        with open(pipeline_file, "r", encoding="utf-8") as f:
            pipeline_data = load_jsonc(pipeline_file)

        with open(pipeline_file, "w", encoding="utf-8") as f:
            json.dump(pipeline_data, f, ensure_ascii=False, separators=(",", ":"))


if __name__ == "__main__":
    install_deps()
    install_resource()
    install_chores()
    install_agent()

    minify_pipelines()

    print(f"Install to {install_path} successfully.")
