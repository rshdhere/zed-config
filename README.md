# Zed configuration

The project panel shows hidden and Git-ignored project files, including local Codex instructions. Git's internal `.git` directory is excluded from the tree and file search.

For a checkout with the [Codex project setup](https://github.com/rshdhere/raashed-skills/tree/main/skills/project-agent-setup), the panel can show:

```text
.agents/
  context/
  rules/
  skills/
  templates/
  workflows/
.codex/
  agents/
AGENTS.override.md
.gitignore
```

The relevant settings are `file_scan_exclusions` and the two visibility options under `project_panel` in [settings.json](settings.json).

## Folder icons

On Linux, install Material Icon Theme from Zed’s extensions, then run the following from this checkout and reload Zed. The dark theme uses custom icons for workflows, environments, infrastructure categories and 15 AWS service folders.

```sh
python3 folder-icons/install.py
```

The installer reuses the installed Material assets. AWS service artwork comes from [AWS Icons for PlantUML](https://github.com/awslabs/aws-icons-for-plantuml) under [CC BY-ND 2.0](https://creativecommons.org/licenses/by-nd/2.0/).
