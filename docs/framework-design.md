# Framework Design (Part 2)

## Folder Structure
- tests/api → API tests
- tests/web → Web UI tests
- tests/integration → Combined tests
- pages/ → Page Object Model
- config/ → Settings
- data/ → Test data

## Key Points
- Used Page Object Model for better maintenance
- Support for multiple tenants from beginning
- Ready for BrowserStack mobile testing
- Configuration managed using YAML + environment variables

## Questions I would ask
1. How should test data be created and cleaned?
2. Which reporting tool do you prefer?
3. How many tests should run in parallel?
4. What is the BrowserStack device coverage needed?
