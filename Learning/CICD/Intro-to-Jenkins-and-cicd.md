# Intro to Jenkins and CI/CD
 
## What is CI? Benefits?
 
- Continuous Integration
- Often triggered when developers push code changes to a shared repository
- Tests are automatically run on the code before it's merged
- The tested code is then integrated/merged into the main codebase

## What is CD? Benefits?
 
Means either:
 
- **Continuous Deployment**
  - Does everything Continuous Delivery does, but goes one step further
  - Also automatically deploys the code
- **Continuous Delivery**
  - Making sure the software is always in a deliverable state
  - Code can be pushed to production at any time (may take the form of an artifact)

## What is Jenkins?
 
- Open-source automation server
- Not just for CI/CD pipelines


**Why use Jenkins? Benefits and disadvantages:**
 
**Benefits**
- Automation
- Extensible via plugins
- Scalability
- Community support
- Cross-platform

**Disadvantages**
- Complex for beginners
- Maintenance overhead
- Can be resource intensive
- User interface


## Stages of a typical CI/CD pipeline
 
1. Source Code Management (SCM) — part of CI
2. Build — part of CI
3. Test — part of CI
4. Integrate/merge code into main codebase — part of CI
5. Package — part of CD
6. Deploy — if pipeline is doing Continuous Deployment
7. Monitor — if pipeline is doing Continuous Deployment

## Example: 3-job Jenkins pipeline structure
 
**Job 1 — Build/Checkout**
Pulls the latest code from GitHub, installs dependencies, builds the app, runs basic/unit tests.
 
**Job 2 — Test**
Runs deeper testing — integration tests, code coverage, linting, possibly security/dependency scanning.
 
**Job 3 — Deploy**
Takes the tested, built app and deploys it — e.g. SSHing into the app server, copying the code over, and restarting it via PM2.
 
Each job only runs if the previous one passes, so a failure at Job 1 or 2 stops the pipeline before anything broken reaches deployment.


## Alternatives to Jenkins
 
- GitLab
- GitHub Actions
- Azure DevOps
- CircleCI
- Travis CI
- Bamboo
- TeamCity
- GoCD

## Why build a pipeline? Business value?
 
- Faster time to market — get the latest version of the product into users' hands sooner
- Improved quality
- Faster feedback cycle
- Reduced risk
- Increased productivity
**The goal:** get code changes deployed to users as quickly as possible.
 
