












Git credentials | uv

























          Skip to content
        















            uv
          



            
              Git credentials
            
          








































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
  

    
  




    
  
    Git credentials
  

    
  




      Table of contents
    




      
        SSH authentication
      
    






      
        HTTP authentication
      
    








      
        Persistence of credentials
      
    





      
        Git credential helpers
      
    








    
  
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
    




      
        SSH authentication
      
    






      
        HTTP authentication
      
    








      
        Persistence of credentials
      
    





      
        Git credential helpers
      
    













    Introduction
  





    Concepts
  





    Authentication
  





Git credentials
uv allows packages to be installed from private Git repositories using SSH or HTTP authentication.
SSH authentication
To authenticate using an SSH key, use the ssh:// protocol:

git+ssh://git@<hostname>/... (e.g., git+ssh://[email protected]/astral-sh/uv)
git+ssh://git@<host>/... (e.g., git+ssh://[email protected]/astral-sh/uv)

SSH authentication requires using the username git.
See the
GitHub SSH documentation
for more details on how to configure SSH.
HTTP authentication
To authenticate over HTTP Basic authentication using a password or token:

git+https://<user>:<token>@<hostname>/... (e.g.,
  git+https://git:[email protected]/astral-sh/uv)
git+https://<token>@<hostname>/... (e.g., git+https://[email protected]/astral-sh/uv)
git+https://<user>@<hostname>/... (e.g., git+https://[email protected]/astral-sh/uv)


Note
When using a GitHub personal access token, the username is arbitrary. GitHub doesn't allow you to
use your account name and password in URLs like this, although other hosts may.

If there are no credentials present in the URL and authentication is needed, the
Git credential helper will be queried.
Persistence of credentials
When using uv add, uv will not persist Git credentials to the pyproject.toml or uv.lock.
These files are often included in source control and distributions, so it is generally unsafe to
include credentials in them.
If you have a Git credential helper configured, your credentials may be automatically persisted,
resulting in successful subsequent fetches of the dependency. However, if you do not have a Git
credential helper or the project is used on a machine without credentials seeded, uv will fail to
fetch the dependency.
You may force uv to persist Git credentials by passing the --raw option to uv add. However, we
strongly recommend setting up a credential helper instead.
Git credential helpers
Git credential helpers are used to store and retrieve Git credentials. See the
Git documentation to learn more.
If you're using GitHub, the simplest way to set up a credential helper is to
install the gh CLI and use:
$ gh auth login

See the gh auth login documentation for more
details.

Note
When using gh auth login interactively, the credential helper will be configured automatically.
But when using gh auth login --with-token, as in the uv
GitHub Actions guide, the
gh auth setup-git command will need to be
run afterwards to configure the credential helper.






August 28, 2025









  Back to top










                Previous
              

                HTTP credentials
              





                Next
              

                TLS certificates
              









  
  
    Made with
    
      Material for MkDocs
    



























