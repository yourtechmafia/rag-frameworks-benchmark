












The auth CLI | uv

























          Skip to content
        















            uv
          



            
              The auth CLI
            
          








































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
  

    
  




    
  
    The auth CLI
  

    
  




      Table of contents
    




      
        Logging in to a service
      
    





      
        Logging out of a service
      
    





      
        Showing credentials for a service
      
    





      
        Using credentials with external tools
      
    





      
        Configuring the storage backend
      
    








    
  
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
    




      
        Logging in to a service
      
    





      
        Logging out of a service
      
    





      
        Showing credentials for a service
      
    





      
        Using credentials with external tools
      
    





      
        Configuring the storage backend
      
    













    Introduction
  





    Concepts
  





    Authentication
  





The uv auth CLI
uv provides a high-level interface for storing and retrieving credentials from services.
Logging in to a service
To add credentials for service, use the uv auth login command:
$ uv auth login example.com

This will prompt for the credentials.
The credentials can also be provided using the --username and --password options, or the
--token option for services which use a __token__ or arbitrary username.

Note
We recommend providing the secret via stdin. Use - to indicate the value should be read from
stdin, e.g., for --password:
$ echo 'my-password' | uv auth login example.com --password -

The same pattern can be used with --token.

Once credentials are added, uv will use them for packaging operations that require fetching content
from the given service. At this time, only HTTPS Basic authentication is supported. The credentials
will not yet be used for Git requests.

Note
The credentials will not be validated, i.e., incorrect credentials will not fail.

Logging out of a service
To remove credentials, use the uv auth logout command:
$ uv auth logout example.com


Note
The credentials will not be invalidated with the remote server, i.e., they will only be removed
from local storage not rendered unusable.

Showing credentials for a service
To show the credential stored for a given URL, use the uv auth token command:
$ uv auth token example.com

If a username was used to log in, it will need to be provided as well, e.g.:
$ uv auth token --username foo example.com

Using credentials with external tools
uv auth helper allows tools that support credential helpers to request HTTP credentials from uv.
At this time, uv supports the
Bazel credential helper protocol.
The command is intended to be invoked by external tools. It reads a JSON request from stdin and
writes a JSON response to stdout. When matching credentials are available, the response includes the
Authorization header:
$ echo '{"uri": "https://example.com/path"}' | uv --preview-features auth-helper auth helper --protocol=bazel get
{"headers":{"Authorization":["Basic ..."]}}

If no credentials are found, uv will return an empty set of headers:
{ "headers": {} }


Note
uv auth helper is experimental. Use --preview-features auth-helper or
UV_PREVIEW_FEATURES=auth-helper to disable the warning.

The Bazel integration guide explains how to use this command
with Bazel.
Configuring the storage backend
Credentials are persisted to the uv credentials store.
By default, credentials are written to a plaintext file. An encrypted system-native storage backend
can be enabled with UV_PREVIEW_FEATURES=native-auth.





May 13, 2026









  Back to top










                Previous
              

                Authentication
              





                Next
              

                HTTP credentials
              









  
  
    Made with
    
      Material for MkDocs
    



























