"""Quick workaround to get up and running with VSCode Remote SSH onto a NixOS
host.

See also
  * https://github.com/microsoft/vscode-remote-release/issues/648#issuecomment-503148523
  * https://nixos.wiki/wiki/Vscode#Remote_ssh
"""

from glob import glob
import os
import stat

# Necessary to trick nix-shell to take the "real" nix-shell header above.
NEW_CONTENTS = "#!" "/usr/bin/env nix-shell" "\n" \
               "#!" "nix-shell -p nodejs-14_x --run node"

for path in glob(os.path.expanduser("~/.vscode-server/bin/**/node")):
  print(f"Fixing {path}...")
  os.remove(path)
  open(path, "w").write(NEW_CONTENTS)
  os.chmod(path, os.stat(path).st_mode | stat.S_IEXEC)
