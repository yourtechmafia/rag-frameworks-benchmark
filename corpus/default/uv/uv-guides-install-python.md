












Installing and managing Python | uv

























          Skip to content
        















            uv
          



            
              Installing and managing Python
            
          








































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
  

    
  




    
  
    Installing Python
  

    
  




      Table of contents
    




      
        Getting started
      
    





      
        Installing a specific version
      
    





      
        Reinstalling Python
      
    





      
        Viewing Python installations
      
    





      
        Automatic Python downloads
      
    





      
        Using existing Python versions
      
    





      
        Upgrading Python versions
      
    





      
        Next steps
      
    








    
  
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
    




      
        Getting started
      
    





      
        Installing a specific version
      
    





      
        Reinstalling Python
      
    





      
        Viewing Python installations
      
    





      
        Automatic Python downloads
      
    





      
        Using existing Python versions
      
    





      
        Upgrading Python versions
      
    





      
        Next steps
      
    













    Introduction
  





    Guides
  





Installing Python
If Python is already installed on your system, uv will
detect and use it without configuration. However, uv can also
install and manage Python versions. uv automatically installs missing
Python versions as needed — you don't need to install Python to get started.
Getting started
To install the latest Python version:
$ uv python install


Note
Python does not publish official distributable binaries. As such, uv uses distributions from the Astral python-build-standalone project. See the Python distributions documentation for more details.

Once Python is installed, it will be used by uv commands automatically. uv also adds the installed
version to your PATH:
$ python3.13

uv only installs a versioned executable by default. To install python and python3 executables,
include the experimental --default option:
$ uv python install --default


Tip
See the documentation on installing Python executables
for more details.

Installing a specific version
To install a specific Python version:
$ uv python install 3.12

To install multiple Python versions:
$ uv python install 3.11 3.12

To install an alternative Python implementation, e.g., PyPy:
$ uv python install [email protected]

See the python install documentation
for more details.
Reinstalling Python
To reinstall uv-managed Python versions, use --reinstall, e.g.:
$ uv python install --reinstall

This will reinstall all previously installed Python versions. Improvements are constantly being
added to the Python distributions, so reinstalling may resolve bugs even if the Python version does
not change.
Viewing Python installations
To view available and installed Python versions:
$ uv python list

See the python list
documentation for more details.
Automatic Python downloads
Python does not need to be explicitly installed to use uv. By default, uv will automatically
download Python versions when they are required. For example, the following would download Python
3.12 if it was not installed:
$ uvx [email protected] -c "print('hello world')"

Even if a specific Python version is not requested, uv will download the latest version on demand.
For example, if there are no Python versions on your system, the following will install Python
before creating a new virtual environment:
$ uv venv


Tip
Automatic Python downloads can be easily disabled if you want more control over when Python is downloaded.


Using existing Python versions
uv will use existing Python installations if present on your system. There is no configuration
necessary for this behavior: uv will use the system Python if it satisfies the requirements of the
command invocation. See the
Python discovery documentation for
details.
To force uv to use the system Python, provide the --no-managed-python flag. See the
Python version preference
documentation for more details.
Upgrading Python versions

Important
Support for upgrading Python patch versions is in preview. This means the behavior is
experimental and subject to change.

To upgrade a Python version to the latest supported patch release:
$ uv python upgrade 3.12

To upgrade all uv-managed Python versions:
$ uv python upgrade

See the python upgrade documentation
for more details.
Next steps
To learn more about uv python, see the Python version concept
page and the command reference.
Or, read on to learn how to run scripts and invoke Python with uv.





July 17, 2025









  Back to top










                Previous
              

                Guides overview
              





                Next
              

                Running scripts
              









  
  
    Made with
    
      Material for MkDocs
    



























