# GitHub Actions Job Failure Fix

## Issue
The "Import Publications From Bibtex" GitHub Actions workflow was showing as "failed" due to a permissions error when trying to apply labels to pull requests.

## Root Cause
The workflow was attempting to add labels `automated-pr, content` to the created pull request, but the GitHub Actions bot didn't have permission to create or assign those labels.

Error message:
```
You do not have permission to create labels on this repository.: {"resource":"Repository","field":"label","code":"unauthorized"}
```

## Solution
Removed the `labels` parameter from the `peter-evans/create-pull-request@v5` action in `.github/workflows/import-publications.yml`.

## What Was Working
- ✅ BibTeX file parsing
- ✅ Publication markdown generation  
- ✅ Pull request creation and updates
- ✅ Hugo site building
- ❌ Only label assignment failed (cosmetic issue)

## Files Changed
- `.github/workflows/import-publications.yml` - Removed labels parameter
- `.gitignore` - Added to prevent committing build artifacts

## Testing
- Verified Hugo site builds successfully
- Confirmed academic package imports work correctly 
- Tested publication markdown generation

The workflow should now complete successfully without the permissions error.