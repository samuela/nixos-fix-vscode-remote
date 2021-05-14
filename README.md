# nixos-fix-vscode-remote

VSCode Remote SSH into NixOS machines. By default VSCode Remote SSH ships with a node.js binary that doesn't run on NixOS systems.

## Usage

Try and fail to connect to the NixOS machine that you'd like to connect to with VSCode Remote SSH. Once that fails, SSH into the machine manually and run this tool:

```
nix-shell https://github.com/samuela/nixos-fix-vscode-remote/archive/main.tar.gz
```

Next time you try to connect from VSCode it should work without an issue!
