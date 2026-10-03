












Platform support | uv

























          Skip to content
        















            uv
          



            
              Platform support
            
          








































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
  

    
  




    
  
    Platform support
  

    
  




      Table of contents
    




      
        Linux versions
      
    





      
        Windows versions
      
    





      
        macOS versions
      
    








    
  
    Python support
  

    
  





    
  
    Rust support
  

    
  





    
  
    License
  

    
  



















      Table of contents
    




      
        Linux versions
      
    





      
        Windows versions
      
    





      
        macOS versions
      
    













    Introduction
  





    Reference
  





    Policies
  





Platform support
uv has Tier 1 support for the following platforms:

macOS (Apple Silicon)
macOS (x86_64)
Linux (x86_64)
Windows (x86_64)

uv is continuously built, tested, and developed against its Tier 1 platforms. Inspired by the Rust
project, Tier 1 can be thought of as
"guaranteed to work".
uv has Tier 2 support
("guaranteed to build")
for the following platforms:

Linux (PPC64LE)
Linux (RISC-V64)
Linux (aarch64)
Linux (armv7)
Linux (i686)
Linux (s390x)
Windows (arm64)

uv has Tier 3 support
("best effort") for the
following platforms:

FreeBSD (x86_64)
Windows (i686)

uv provides official binaries on GitHub and pre-built wheels on PyPI
for its Tier 1 and Tier 2 platforms.
Tier 2 platforms are continuously built, but the uv test suite is not run on them and stability may
vary in practice.
Tier 3 platforms may not be built or tested, but uv will accept patches to fix bugs.
Linux versions
On Linux, compatibility is determined by libc version.
uv publishes both glibc-based and musl-based distributions.
For glibc-based Linux distributions, uv publishes
manylinux-compatible wheels and corresponding binaries. These
artifacts depend on glibc being available on the host system. In a manylinux wheel tag, the version
encodes the minimum supported glibc version for that wheel; for example, manylinux_2_17_x86_64
requires glibc 2.17+.
uv's official glibc-based wheels and binaries are published for the following targets:

x86_64-unknown-linux-gnu (manylinux_2_17_x86_64)
aarch64-unknown-linux-gnu (manylinux_2_28_aarch64)
armv7-unknown-linux-gnueabihf (manylinux_2_17_armv7l)
i686-unknown-linux-gnu (manylinux_2_17_i686)
powerpc64le-unknown-linux-gnu (manylinux_2_17_ppc64le)
riscv64gc-unknown-linux-gnu (manylinux_2_31_riscv64)
s390x-unknown-linux-gnu (manylinux_2_17_s390x)

uv also publishes musl-based wheels and fully statically linked binaries for the following targets:

x86_64-unknown-linux-musl (musllinux_1_1_x86_64)
aarch64-unknown-linux-musl (musllinux_1_1_aarch64)
armv7-unknown-linux-musleabihf (musllinux_1_1_armv7l)
i686-unknown-linux-musl (musllinux_1_1_i686)
riscv64gc-unknown-linux-musl (musllinux_1_1_riscv64)
arm-unknown-linux-musleabihf (linux_armv6l)

The wheels are published with musllinux-compatible tags.
However, the embedded uv binaries are fully statically linked and do not require musl libc on the
host system.
The official Docker images include these fully statically
linked musl uv binaries for amd64 and arm64.
Windows versions
The minimum supported Windows versions are Windows 10 and Windows Server 2016, following
Rust's own Tier 1 support.
macOS versions
uv supports macOS 13+ (Ventura).
uv is known to work on macOS 12, but requires installation of a realpath executable.





March 20, 2026









  Back to top










                Previous
              

                Versioning
              





                Next
              

                Python support
              









  
  
    Made with
    
      Material for MkDocs
    



























