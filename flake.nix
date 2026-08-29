{
  description = "CIS-129 Python Development Environment";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs =
    {
      self,
      nixpkgs,
      flake-utils,
    }:
    flake-utils.lib.eachDefaultSystem (
      system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        python = pkgs.python314;
        pythonEnv = python.withPackages (
          ps: with ps; [
            pytest
            mypy
          ]
        );

        codium = pkgs.vscode-with-extensions.override {
          vscode = pkgs.vscodium;
          vscodeExtensions = with pkgs.vscode-extensions; [
            ms-python.python
            ms-pyright.pyright
            vscodevim.vim
            arcticicestudio.nord-visual-studio-code
          ];
        };

      in
      {
        devShells.default = pkgs.mkShell {
          packages = [
            pythonEnv
            codium
          ];

          shellHook = ''
            echo "Python $(python --version)"
            echo "VSCodium $(codium --version 2>/dev/null | head -n1)"
          '';
        };
      }
    );
}
