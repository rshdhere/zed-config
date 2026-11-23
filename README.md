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
