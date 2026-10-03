












Google Artifact Registry | uv

























          Skip to content
        















            uv
          



            
              Google Artifact Registry
            
          








































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
  

    
  




    
  
    Google Artifact Registry
  

    
  




      Table of contents
    




      
        Authenticate with a Google access token
      
    





      
        Authenticate with keyring and keyrings.google-artifactregistry-auth
      
    





      
        Publishing packages
      
    








    
  
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
    




      
        Authenticate with a Google access token
      
    





      
        Authenticate with keyring and keyrings.google-artifactregistry-auth
      
    





      
        Publishing packages
      
    













    Introduction
  





    Guides
  





    Integrations
  





Google Artifact Registry
uv can install packages from
Google Artifact Registry, either by using an
access token, or using the keyring package.

Note
This guide assumes that gcloud CLI is installed and
authenticated.

To use Google Artifact Registry, add the index to your project:
pyproject.toml[[tool.uv.index]]
name = "private-registry"
url = "https://<REGION>-python.pkg.dev/<PROJECT>/<REPOSITORY>/simple/"

Authenticate with a Google access token
Credentials can be provided via "Basic" HTTP authentication scheme. Include access token in the
password field of the URL. Username must be oauth2accesstoken, otherwise authentication will fail.
Generate a token with gcloud:
export ARTIFACT_REGISTRY_TOKEN=$(
    gcloud auth application-default print-access-token
)


Note
You might need to pass extra parameters to properly generate the token (like --project), this
is a basic example.

Then set credentials for the index with:
export UV_INDEX_PRIVATE_REGISTRY_USERNAME=oauth2accesstoken
export UV_INDEX_PRIVATE_REGISTRY_PASSWORD="$ARTIFACT_REGISTRY_TOKEN"


Note
PRIVATE_REGISTRY should match the name of the index defined in your pyproject.toml.

Authenticate with keyring and keyrings.google-artifactregistry-auth
You can also authenticate to Artifact Registry using keyring
package with the
keyrings.google-artifactregistry-auth plugin.
Because these two packages are required to authenticate to Artifact Registry, they must be
pre-installed from a source other than Artifact Registry.
The keyrings.google-artifactregistry-auth plugin wraps
gcloud CLI to generate short-lived access tokens, securely
store them in system keyring, and refresh them when they are expired.
uv only supports using the keyring package in
subprocess mode. The keyring executable must be in
the PATH, i.e., installed globally or in the active environment. The keyring CLI requires a
username in the URL and it must be oauth2accesstoken.
# Pre-install keyring and Artifact Registry plugin from the public PyPI
uv tool install keyring --with keyrings.google-artifactregistry-auth

# Enable keyring authentication
export UV_KEYRING_PROVIDER=subprocess

# Set the username for the index
export UV_INDEX_PRIVATE_REGISTRY_USERNAME=oauth2accesstoken


Note
The tool.uv.keyring-provider
setting can be used to enable keyring in your uv.toml or pyproject.toml.
Similarly, the username for the index can be added directly to the index URL.

Publishing packages
If you also want to publish your own packages to Google Artifact Registry, you can use uv publish
as described in the Building and publishing guide.
First, add a publish-url to the index you want to publish packages to. For example:
pyproject.toml[[tool.uv.index]]
name = "private-registry"
url = "https://<REGION>-python.pkg.dev/<PROJECT>/<REPOSITORY>/simple/"
publish-url = "https://<REGION>-python.pkg.dev/<PROJECT>/<REPOSITORY>/"

Then, configure credentials (if not using keyring):
$ export UV_PUBLISH_USERNAME=oauth2accesstoken
$ export UV_PUBLISH_PASSWORD="$ARTIFACT_REGISTRY_TOKEN"

And publish the package:
$ uv publish --index private-registry

To use uv publish without adding the publish-url to the project, you can set UV_PUBLISH_URL:
$ export UV_PUBLISH_URL=https://<REGION>-python.pkg.dev/<PROJECT>/<REPOSITORY>/
$ uv publish

Note this method is not preferable because uv cannot check if the package is already published
before uploading artifacts.





March 23, 2026









  Back to top










                Previous
              

                Azure Artifacts
              





                Next
              

                AWS CodeArtifact
              









  
  
    Made with
    
      Material for MkDocs
    



























