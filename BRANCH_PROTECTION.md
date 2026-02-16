# Branch Protection Rules Configuration

This document describes the recommended branch protection rules for the CodeMentor-AI repository.

## Main Branch Protection

### Recommended Settings for `main` branch:

#### Pull Request Requirements
- **Require pull request before merging**: ✅ Enabled
  - **Require approvals**: 1 approval minimum
  - **Dismiss stale reviews**: ✅ Enabled (when new commits are pushed)
  - **Require review from Code Owners**: ⬜ Optional (if CODEOWNERS file exists)

#### Status Checks
- **Require status checks to pass before merging**: ✅ Enabled
  - **Require branches to be up to date**: ✅ Enabled
  - Required status checks:
    - `test` (if CI/CD is configured)
    - `lint` (if CI/CD is configured)
    - `build` (if CI/CD is configured)

#### Additional Settings
- **Require conversation resolution before merging**: ✅ Enabled
- **Require signed commits**: ⬜ Optional (recommended for high-security projects)
- **Require linear history**: ⬜ Optional (prevents merge commits)
- **Include administrators**: ⬜ Disabled (allows admins to bypass rules if needed)
- **Allow force pushes**: ❌ Disabled
- **Allow deletions**: ❌ Disabled

## How to Apply These Rules

### Option 1: Via GitHub Web Interface

1. Go to your repository on GitHub
2. Click **Settings** → **Branches**
3. Under "Branch protection rules", click **Add rule**
4. Enter branch name pattern: `main`
5. Configure the settings as described above
6. Click **Create** or **Save changes**

### Option 2: Via GitHub CLI

```bash
# Protect main branch with PR requirement
gh api repos/{owner}/{repo}/branches/main/protection \
  --method PUT \
  --field required_pull_request_reviews[required_approving_review_count]=1 \
  --field required_pull_request_reviews[dismiss_stale_reviews]=true \
  --field enforce_admins=false \
  --field required_conversation_resolution=true \
  --field allow_force_pushes=false \
  --field allow_deletions=false
```

Replace `{owner}` with `ChanchalSen09` and `{repo}` with `CodeMentor-AI`.

### Option 3: Via Terraform (Infrastructure as Code)

```hcl
resource "github_branch_protection" "main" {
  repository_id = github_repository.repo.node_id
  pattern       = "main"

  required_pull_request_reviews {
    required_approving_review_count = 1
    dismiss_stale_reviews          = true
  }

  required_status_checks {
    strict = true
  }

  require_conversation_resolution = true
  enforce_admins                  = false
  allows_deletions                = false
  allows_force_pushes             = false
}
```

## Development Branch Protection

For development or feature branches, consider lighter protection:

### Recommended Settings for `develop` or `dev` branch:

- **Require pull request before merging**: ✅ Enabled
  - **Require approvals**: 0-1 approvals (more flexible for development)
- **Allow force pushes**: ⬜ Optional (for rebasing)
- Other settings can mirror the main branch

## Why Branch Protection?

Branch protection rules help:
- 🛡️ **Prevent accidental changes** to important branches
- 👥 **Ensure code review** before merging
- ✅ **Maintain code quality** through required status checks
- 📝 **Require documentation** through conversation resolution
- 🔒 **Protect history** by preventing force pushes

## Best Practices

1. **Always protect your main/master branch**
2. **Require at least one review** for production code
3. **Enable status checks** once CI/CD is set up
4. **Require conversation resolution** to ensure discussions are addressed
5. **Regularly review and update** protection rules as the project evolves

## Notes

- These settings can be adjusted based on team size and project needs
- Stricter rules are recommended for production/main branches
- More flexible rules can be used for development branches
- Consider enabling signed commits for enhanced security
