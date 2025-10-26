{

  description = "Racket development environment";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let pkgs = import nixpkgs { inherit system; };
      in {
        devShell = pkgs.mkShell {

          # Dependencies for project
          buildInputs = [ pkgs.racket ];

          #links libraries to shell
          LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
            #
          ];

          shellHook = ''
            PS1="[\\u@\\h && RACKET-DEV-ENV:\\w]\$ "
          '';
        };
      });
}
