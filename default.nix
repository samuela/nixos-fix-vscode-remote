{pkgs ? import <nixpkgs> {}}:

pkgs.mkShell {
  name = "nixos-fix-vscode-remote";
  buildInputs = with pkgs; [ python3 ];
  shellHook = "exec python3 ${./fix.py}";
}
