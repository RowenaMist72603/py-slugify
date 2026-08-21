# String slugify

```
slugify.py
```
I usually write TypeScript, but this Python script handles URL slugs without pulling in heavy packages. Every extra dependency is a tax on deploy time. Check the test file next to the implementation to see how it handles edge cases. It relies strictly on the standard library. No external services and no extra installs. Just standard Python doing its job so I can get back to shipping features.