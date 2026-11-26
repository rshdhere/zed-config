"""Install the folder mappings over the installed Zed Material Icon Theme."""
import json
import os
import shutil
from pathlib import Path

source = Path(__file__).resolve().parent
data = Path(os.environ.get("XDG_DATA_HOME") or Path.home() / ".local/share")
extensions = data / "zed/extensions/installed"
base = extensions / "material-icon-theme"
target = extensions / "local-material-workflows"
theme_path = Path("icon_themes/material-icon-theme.json")
if not (base / theme_path).is_file():
    raise SystemExit("Install Material Icon Theme in Zed first.")

document = json.loads((base / theme_path).read_text())
theme = next(theme for theme in document["themes"] if theme["appearance"] == "dark")
document["name"] = theme["name"] = "Material Icon Theme (Workflows)"
document["themes"] = [theme]
overrides = json.loads((source / "folders.json").read_text())
for pair in overrides.values():
    for asset in pair.values():
        if not ((source / asset).is_file() or (base / asset).is_file()):
            raise SystemExit(f"Missing icon: {asset}")
theme["named_directory_icons"].update(overrides)

(target / theme_path.parent).mkdir(parents=True, exist_ok=True)
icons = target / "icons"
if not icons.exists():
    icons.symlink_to(base / "icons", target_is_directory=True)
shutil.copytree(source / "aws-icons", target / "aws-icons", dirs_exist_ok=True)
(target / theme_path).write_text(json.dumps(document, separators=(",", ":")) + "\n")
shutil.copyfile(source / "extension.toml", target / "extension.toml")
