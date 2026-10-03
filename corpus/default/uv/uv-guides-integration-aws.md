












AWS CodeArtifact | uv

























          Skip to content
        















            uv
          



            
              AWS CodeArtifact
            
          








































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
  

    
  




    
  
    AWS CodeArtifact
  

    
  




      Table of contents
    




      
        Authenticate with an AWS access token
      
    





      
        Authenticate with keyring and keyrings.codeartifact
      
    





      
        Publishing packages
      
    








    
  
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
    




      
        Authenticate with an AWS access token
      
    





      
        Authenticate with keyring and keyrings.codeartifact
      
    





      
        Publishing packages
      
    













    Introduction
  





    Guides
  





    Integrations
  





AWS CodeArtifact
uv can install packages from
AWS CodeArtifact, either by
using an access token, or using the keyring package.

Note
This guide assumes that awscli is installed and authenticated.

The index can be declared like so:
pyproject.toml[[tool.uv.index]]
name = "private-registry"
url = "https://<DOMAIN>-<ACCOUNT_ID>.d.codeartifact.<REGION>.amazonaws.com/pypi/<REPOSITORY>/simple/"

Authenticate with an AWS access token
Credentials can be provided via "Basic" HTTP authentication scheme. Include access token in the
password field of the URL. Username must be aws, otherwise authentication will fail.
Generate a token with awscli:
export AWS_CODEARTIFACT_TOKEN="$(
    aws codeartifact get-authorization-token \
    --domain <DOMAIN> \
    --domain-owner <ACCOUNT_ID> \
    --query authorizationToken \
    --output text
)"


Note
You might need to pass extra parameters to properly generate the token (like --region), this
is a basic example.

Then set credentials for the index with:
export UV_INDEX_PRIVATE_REGISTRY_USERNAME=aws
export UV_INDEX_PRIVATE_REGISTRY_PASSWORD="$AWS_CODEARTIFACT_TOKEN"


Note
PRIVATE_REGISTRY should match the name of the index defined in your pyproject.toml.

Authenticate with keyring and keyrings.codeartifact
You can also authenticate to Artifact Registry using keyring
package with the keyrings.codeartifact plugin.
Because these two packages are required to authenticate to Artifact Registry, they must be
pre-installed from a source other than Artifact Registry.
The keyrings.codeartifact plugin wraps boto3 to generate
short-lived access tokens, securely store them in system keyring, and refresh them when they are
expired.
uv only supports using the keyring package in
subprocess mode. The keyring executable must be in
the PATH, i.e., installed globally or in the active environment. The keyring CLI requires a
username in the URL and it must be aws.
# Pre-install keyring and AWS CodeArtifact plugin from the public PyPI
uv tool install keyring --with keyrings.codeartifact

# Enable keyring authentication
export UV_KEYRING_PROVIDER=subprocess

# Set the username for the index
export UV_INDEX_PRIVATE_REGISTRY_USERNAME=aws


Note
The tool.uv.keyring-provider
setting can be used to enable keyring in your uv.toml or pyproject.toml.
Similarly, the username for the index can be added directly to the index URL.

Publishing packages
If you also want to publish your own packages to AWS CodeArtifact, you can use uv publish as
described in the Building and publishing guide.
First, add a publish-url to the index you want to publish packages to. For example:
pyproject.toml[[tool.uv.index]]
name = "private-registry"
url = "https://<DOMAIN>-<ACCOUNT_ID>.d.codeartifact.<REGION>.amazonaws.com/pypi/<REPOSITORY>/simple/"
publish-url = "https://<DOMAIN>-<ACCOUNT_ID>.d.codeartifact.<REGION>.amazonaws.com/pypi/<REPOSITORY>/"

Then, configure credentials (if not using keyring):
$ export UV_PUBLISH_USERNAME=aws
$ export UV_PUBLISH_PASSWORD="$AWS_CODEARTIFACT_TOKEN"

And publish the package:
$ uv publish --index private-registry

To use uv publish without adding the publish-url to the project, you can set UV_PUBLISH_URL:
$ export UV_PUBLISH_URL=https://<DOMAIN>-<ACCOUNT_ID>.d.codeartifact.<REGION>.amazonaws.com/pypi/<REPOSITORY>/
$ uv publish

Note this method is not preferable because uv cannot check if the package is already published
before uploading artifacts.





March 23, 2026









  Back to top










                Previous
              

                Google Artifact Registry
              





                Next
              

                JFrog Artifactory
              









  
  
    Made with
    
      Material for MkDocs
    



























