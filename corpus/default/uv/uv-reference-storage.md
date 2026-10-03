












Storage | uv

























          Skip to content
        















            uv
          



            
              Storage
            
          








































            Initializing search
          












    uv
  















    uv
  






    uv
  






    
  
    Introduction
  

    
  







    
  
    Getting started
  

    
  








            
  
    Getting started
  

          




    
  
    Installation
  

    
  





    
  
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
  

    
  




    
  
    Storage
  

    
  




      Table of contents
    




      
        Storage directories
      
    






      
        Temporary directory
      
    





      
        Cache directory
      
    





      
        Persistent data directory
      
    





      
        Configuration directories
      
    





      
        Executable directory
      
    








      
        Types of data
      
    






      
        Dependency cache
      
    





      
        Python versions
      
    





      
        Python executables
      
    





      
        Tools
      
    





      
        Tool executables
      
    





      
        The uv executable
      
    





      
        Configuration files
      
    





      
        Project virtual environments
      
    





      
        Script virtual environments
      
    











    
  
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
    




      
        Storage directories
      
    






      
        Temporary directory
      
    





      
        Cache directory
      
    





      
        Persistent data directory
      
    





      
        Configuration directories
      
    





      
        Executable directory
      
    








      
        Types of data
      
    






      
        Dependency cache
      
    





      
        Python versions
      
    





      
        Python executables
      
    





      
        Tools
      
    





      
        Tool executables
      
    





      
        The uv executable
      
    





      
        Configuration files
      
    





      
        Project virtual environments
      
    





      
        Script virtual environments
      
    
















    Introduction
  





    Reference
  





Storage
Storage directories
uv uses the following high-level directories for storage.
For each location, uv checks for the existence of environment variables in the given order and uses
the first path found.
The paths of storage directories are platform-specific. uv follows the
XDG conventions on Linux and macOS
and the Known Folder scheme
on Windows.
Temporary directory
The temporary directory is used for ephemeral data.
UnixWindows



$TMPDIR
/tmp




%TMP%
%TEMP%
%USERPROFILE%




Cache directory
The cache directory is used for data that is disposable, but is useful to be long-lived.
UnixWindows



$XDG_CACHE_HOME/uv
$HOME/.cache/uv




%LOCALAPPDATA%\uv\cache
uv\cache within FOLDERID_LocalAppData




Persistent data directory
The persistent data directory is used for non-disposable data.
UnixWindows



$XDG_DATA_HOME/uv
$HOME/.local/share/uv
$CWD/.uv




%APPDATA%\uv\data
.\.uv




Configuration directories
The configuration directories are used to store changes to uv's settings.
User-level configuration
UnixWindows



$XDG_CONFIG_HOME/uv
$HOME/.config/uv




%APPDATA%\uv
uv within FOLDERID_RoamingAppData




System-level configuration
UnixWindows



$XDG_CONFIG_DIRS/uv
/etc/uv




%PROGRAMDATA%\uv
uv within FOLDERID_AppDataProgramData




Executable directory
The executable directory is used to store files that can be run by the user, i.e., a directory that
should be on the PATH.
UnixWindows



$XDG_BIN_HOME
$XDG_DATA_HOME/../bin
$HOME/.local/bin




%XDG_BIN_HOME%
%XDG_DATA_HOME%\..\bin
%USERPROFILE%\.local\bin




Types of data
Dependency cache
uv uses a local cache to avoid re-downloading and re-building dependencies.
By default, the cache is stored in the cache directory but it can be overridden
via command line arguments, environment variables, or settings as detailed in
the cache documentation. When the cache is disabled, the
cache will be stored in a temporary directory.
Use uv cache dir to show the current cache directory path.

Important
For optimal performance, the cache directory needs to be on the same filesystem as virtual
environments.

Python versions
uv can install managed Python versions, e.g., with
uv python install.
By default, Python versions managed by uv are stored in a python/ subdirectory of the
persistent data directory, e.g., ~/.local/share/uv/python.
Use uv python dir to show the Python installation directory.
Use the UV_PYTHON_INSTALL_DIR environment variable to override the installation directory.

Note
Changing where Python is installed will not be automatically reflected in existing virtual environments; they will keep referring to the old location, and will need to be updated manually (e.g. by re-creating them).

Python executables
uv installs executables for Python versions, e.g., python3.13.
By default, Python executables are stored in the executable directory.
Use uv python dir --bin to show the Python executable directory.
Use the UV_PYTHON_BIN_DIR environment variable to override the Python executable directory.
Tools
uv can install Python packages as command-line tools using
uv tool install.
By default, tools are installed in a tools/ subdirectory of the
persistent data directory, e.g., ~/.local/share/uv/tools.
Use uv tool dir to show the tool installation directory.
Use the UV_TOOL_DIR environment variable to configure the installation directory.
Tool executables
uv installs executables for installed tools, e.g., ruff.
By default, tool executables are stored in the executable directory.
Use uv tool dir --bin to show the tool executable directory.
Use the UV_TOOL_BIN_DIR environment variable to configure the tool executable directory.
The uv executable
When using uv's standalone installer to install uv, the uv and uvx executables
are installed into the executable directory.
Use the UV_INSTALL_DIR environment variable to configure uv's installation directory.
Configuration files
uv's behavior can be configured through TOML files.
Configuration files are discovered in the configuration directories.
For more details, see the configuration files documentation.
Project virtual environments
When working on projects, uv creates a dedicated virtual
environment for each project.
By default, project virtual environments are created in .venv in the project or workspace root,
i.e., next to the pyproject.toml.
Use the UV_PROJECT_ENVIRONMENT environment variable to override this location. For more details,
see the
projects environment documentation.
With the centralized-project-envs preview feature, uv stores default
project environments in the cache directory. They can be removed by
uv cache clean or uv cache prune and are recreated when next needed. See the
centralized project environments
documentation for details.
Script virtual environments
When running scripts with inline metadata, uv creates a dedicated virtual
environment for each script in the cache directory.





June 25, 2026









  Back to top










                Previous
              

                Environment variables
              





                Next
              

                Installer options
              









  
  
    Made with
    
      Material for MkDocs
    



























