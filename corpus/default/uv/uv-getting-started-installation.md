












Installation | uv

























          Skip to content
        















            uv
          



            
              Installation
            
          








































            Initializing search
          












    uv
  















    uv
  






    uv
  






    
  
    Introduction
  

    
  







    
  
    Getting started
  

    
  








            
  
    Getting started
  

          





    
  
    Installation
  

    
  




    
  
    Installation
  

    
  




      Table of contents
    




      
        Installation methods
      
    






      
        Standalone installer
      
    





      
        PyPI
      
    





      
        Homebrew
      
    





      
        MacPorts
      
    





      
        WinGet
      
    





      
        Scoop
      
    





      
        Docker
      
    





      
        GitHub Releases
      
    





      
        Cargo
      
    








      
        Upgrading uv
      
    





      
        Shell autocompletion
      
    





      
        Uninstallation
      
    





      
        Next steps
      
    








    
  
    First steps
  

    
  





    
  
    Features
  

    
  





    
  
    Getting help
  

    
  










    
  
    Guides
  

    
  








            
  
    Guides
  

          




    
  
    Installing Python
  

    
  





    
  
    Running scripts
  

    
  





    
  
    Using tools
  

    
  





    
  
    Working on projects
  

    
  





    
  
    Publishing packages
  

    
  







    
  
    Migration
  

    
  








            
  
    Migration
  

          




    
  
    From pip to a uv project
  

    
  










    
  
    Integrations
  

    
  








            
  
    Integrations
  

          




    
  
    Docker
  

    
  





    
  
    Jupyter
  

    
  





    
  
    marimo
  

    
  





    
  
    GitHub Actions
  

    
  





    
  
    GitLab CI/CD
  

    
  





    
  
    Pre-commit
  

    
  





    
  
    PyTorch
  

    
  





    
  
    FastAPI
  

    
  





    
  
    Bazel
  

    
  





    
  
    Azure Artifacts
  

    
  





    
  
    Google Artifact Registry
  

    
  





    
  
    AWS CodeArtifact
  

    
  





    
  
    JFrog Artifactory
  

    
  





    
  
    Renovate
  

    
  





    
  
    Dependabot
  

    
  





    
  
    AWS Lambda
  

    
  





    
  
    Coiled
  

    
  













    
  
    Concepts
  

    
  








            
  
    Concepts
  

          






    
  
    Projects
  

    
  








            
  
    Projects
  

          




    
  
    Structure and files
  

    
  





    
  
    Creating projects
  

    
  





    
  
    Managing dependencies
  

    
  





    
  
    Running commands
  

    
  





    
  
    Locking and syncing
  

    
  





    
  
    Configuring projects
  

    
  





    
  
    Building distributions
  

    
  





    
  
    Exporting lockfiles
  

    
  





    
  
    Using workspaces
  

    
  








    
  
    Tools
  

    
  





    
  
    Python versions
  

    
  





    
  
    Configuration files
  

    
  





    
  
    Package indexes
  

    
  





    
  
    Resolution
  

    
  





    
  
    Build backend
  

    
  







    
  
    Authentication
  

    
  








            
  
    Authentication
  

          




    
  
    The auth CLI
  

    
  





    
  
    HTTP credentials
  

    
  





    
  
    Git credentials
  

    
  





    
  
    TLS certificates
  

    
  





    
  
    Third-party services
  

    
  








    
  
    Caching
  

    
  





    
  
    Preview features
  

    
  







    
  
    The pip interface
  

    
  








            
  
    The pip interface
  

          




    
  
    Using environments
  

    
  





    
  
    Managing packages
  

    
  





    
  
    Inspecting environments
  

    
  





    
  
    Declaring dependencies
  

    
  





    
  
    Locking environments
  

    
  





    
  
    Compatibility with pip
  

    
  













    
  
    Reference
  

    
  








            
  
    Reference
  

          




    
  
    Commands
  

    
  





    
  
    Settings
  

    
  





    
  
    Environment variables
  

    
  





    
  
    Storage
  

    
  





    
  
    Installer options
  

    
  







    
  
    Troubleshooting
  

    
  








            
  
    Troubleshooting
  

          




    
  
    Build failures
  

    
  





    
  
    Reproducible examples
  

    
  








    
  
    Contributing
  

    
  







    
  
    Internals
  

    
  








            
  
    Internals
  

          




    
  
    Resolver
  

    
  





    
  
    Workspace Metadata
  

    
  








    
  
    Benchmarks
  

    
  







    
  
    Policies
  

    
  








            
  
    Policies
  

          




    
  
    Versioning
  

    
  





    
  
    Platform support
  

    
  





    
  
    Python support
  

    
  





    
  
    Rust support
  

    
  





    
  
    License
  

    
  



















      Table of contents
    




      
        Installation methods
      
    






      
        Standalone installer
      
    





      
        PyPI
      
    





      
        Homebrew
      
    





      
        MacPorts
      
    





      
        WinGet
      
    





      
        Scoop
      
    





      
        Docker
      
    





      
        GitHub Releases
      
    





      
        Cargo
      
    








      
        Upgrading uv
      
    





      
        Shell autocompletion
      
    





      
        Uninstallation
      
    





      
        Next steps
      
    













    Introduction
  





    Getting started
  





Installing uv
Installation methods
Install uv with our standalone installers or your package manager of choice.
Standalone installer
uv provides a standalone installer to download and install uv:
macOS and LinuxWindows


Use curl to download the script and execute it with sh:
$ curl -LsSf https://astral.sh/uv/install.sh | sh

If your system doesn't have curl, you can use wget:
$ wget -qO- https://astral.sh/uv/install.sh | sh

Request a specific version by including it in the URL:
$ curl -LsSf https://astral.sh/uv/0.12.22/install.sh | sh



Use irm to download the script and execute it with iex:
PS> powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

Changing the execution policy allows running a script from the internet.
Request a specific version by including it in the URL:
PS> powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/0.12.22/install.ps1 | iex"





Tip
The installation script may be inspected before use:
macOS and LinuxWindows


$ curl -LsSf https://astral.sh/uv/install.sh | less



PS> powershell -c "irm https://astral.sh/uv/install.ps1 | more"




Alternatively, the installer or binaries can be downloaded directly from GitHub.

See the reference documentation on the installer for details on
customizing your uv installation.
PyPI
For convenience, uv is published to PyPI.
If installing from PyPI, we recommend installing uv into an isolated environment, e.g., with pipx:
$ pipx install uv

However, pip can also be used:
$ pip install uv


Note
uv ships with prebuilt distributions (wheels) for many platforms; if a wheel is not available for a given
platform, uv will be built from source, which requires a Rust toolchain. See the
contributing setup guide
for details on building uv from source.

Homebrew
uv is available in the core Homebrew packages.
$ brew install uv

MacPorts
uv is available via MacPorts.
$ sudo port install uv

WinGet
uv is available via WinGet.
$ winget install --id=astral-sh.uv  -e

Scoop
uv is available via Scoop.
$ scoop install main/uv

Docker
uv provides a Docker image at
ghcr.io/astral-sh/uv.
See our guide on using uv in Docker for more details.
GitHub Releases
uv release artifacts can be downloaded directly from
GitHub Releases.
Each release page includes binaries for all supported platforms as well as instructions for using
the standalone installer via github.com instead of astral.sh.
Cargo
uv is available via crates.io.
$ cargo install --locked uv


Note
This method builds uv from source, which requires a compatible Rust toolchain.

Upgrading uv
When uv is installed via the standalone installer, it can update itself on-demand:
$ uv self update


Tip
Updating uv will re-run the installer and can modify your shell profiles. To disable this
behavior, set UV_NO_MODIFY_PATH=1.

When another installation method is used, self-updates are disabled. Use the package manager's
upgrade method instead. For example, with pip:
$ pip install --upgrade uv

Shell autocompletion

Tip
You can run echo $SHELL to help you determine your shell.

To enable shell autocompletion for uv commands, run one of the following:
BashZshfishElvishPowerShell / pwsh


echo 'eval "$(uv generate-shell-completion bash)"' >> ~/.bashrc



echo 'eval "$(uv generate-shell-completion zsh)"' >> ~/.zshrc



echo 'uv generate-shell-completion fish | source' > ~/.config/fish/completions/uv.fish



echo 'eval (uv generate-shell-completion elvish | slurp)' >> ~/.elvish/rc.elv



if (!(Test-Path -Path $PROFILE)) {
  New-Item -ItemType File -Path $PROFILE -Force
}
Add-Content -Path $PROFILE -Value '(& uv generate-shell-completion powershell) | Out-String | Invoke-Expression'




To enable shell autocompletion for uvx, run one of the following:
BashZshfishElvishPowerShell / pwsh


echo 'eval "$(uvx --generate-shell-completion bash)"' >> ~/.bashrc



echo 'eval "$(uvx --generate-shell-completion zsh)"' >> ~/.zshrc



echo 'uvx --generate-shell-completion fish | source' > ~/.config/fish/completions/uvx.fish



echo 'eval (uvx --generate-shell-completion elvish | slurp)' >> ~/.elvish/rc.elv



if (!(Test-Path -Path $PROFILE)) {
  New-Item -ItemType File -Path $PROFILE -Force
}
Add-Content -Path $PROFILE -Value '(& uvx --generate-shell-completion powershell) | Out-String | Invoke-Expression'




Then restart the shell or source the shell config file.
Uninstallation
If you need to remove uv from your system, follow these steps:


Clean up stored data (optional):
$ uv cache clean
$ rm -r "$(uv python dir)"
$ rm -r "$(uv tool dir)"


Tip
Before removing the binaries, you may want to remove any data that uv has stored. See the
storage reference for details on where uv stores data.



Remove the uv, uvx, and uvw binaries:
macOS and LinuxWindows


$ rm ~/.local/bin/uv ~/.local/bin/uvx



PS> rm $HOME\.local\bin\uv.exe
PS> rm $HOME\.local\bin\uvx.exe
PS> rm $HOME\.local\bin\uvw.exe





Note
Prior to 0.5.0, uv was installed into ~/.cargo/bin. The binaries can be removed from there to
uninstall. Upgrading from an older version will not automatically remove the binaries from
~/.cargo/bin.



Next steps
See the first steps or jump straight to the guides to
start using uv.





October 1, 2026









  Back to top










                Previous
              

                Getting started
              





                Next
              

                First steps
              









  
  
    Made with
    
      Material for MkDocs
    



























