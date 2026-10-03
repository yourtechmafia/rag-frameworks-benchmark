












Getting help | uv

























          Skip to content
        















            uv
          



            
              Getting help
            
          








































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
  

    
  




    
  
    Getting help
  

    
  




      Table of contents
    




      
        Help menus
      
    





      
        Displaying verbose output
      
    





      
        Viewing the version
      
    





      
        Troubleshooting issues
      
    





      
        Open an issue on GitHub
      
    





      
        Chat on Discord
      
    













    
  
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
    




      
        Help menus
      
    





      
        Displaying verbose output
      
    





      
        Viewing the version
      
    





      
        Troubleshooting issues
      
    





      
        Open an issue on GitHub
      
    





      
        Chat on Discord
      
    













    Introduction
  





    Getting started
  





Getting help
Help menus
The --help flag can be used to view the help menu for a command, e.g., for uv:
$ uv --help

To view the help menu for a specific command, e.g., for uv init:
$ uv init --help

When using the --help flag, uv displays a condensed help menu. To view a longer help menu for a
command, use uv help:
$ uv help

To view the long help menu for a specific command, e.g., for uv init:
$ uv help init

When using the long help menu, uv will attempt to use less or more to "page" the output so it is
not all displayed at once. To exit the pager, press q.
Displaying verbose output
The -v flag can be used to display verbose output for a command, e.g., for uv sync:
$ uv sync -v

The -v flag can be repeated to increase verbosity, e.g.:
$ uv sync -vv

Often, the verbose output will include additional information about why uv is behaving in a certain
way.
Viewing the version
When seeking help, it's important to determine the version of uv that you're using — sometimes the
problem is already solved in a newer version.
To check the installed version:
$ uv self version

The following are also valid:
$ uv --version      # Same output as `uv self version`
$ uv -V             # Will not include the build commit and date


Note
Before uv 0.7.0, uv version was used instead of uv self version.

Troubleshooting issues
The reference documentation contains a
troubleshooting guide for common issues.
Open an issue on GitHub
The issue tracker on GitHub is a good place to report bugs
and request features. Make sure to search for similar issues first, as it is common for someone else
to encounter the same problem.
Chat on Discord
Astral has a Discord server, which is a great place to ask
questions, learn more about uv, and engage with other community members.





September 17, 2025









  Back to top










                Previous
              

                Features
              





                Next
              

                Guides overview
              









  
  
    Made with
    
      Material for MkDocs
    



























