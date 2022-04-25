# Weird PY 

## Write-up

- The challenge let you see any variable present in `GLOBALS` as long as it's different from `Flag`
- The only down side is this line 
`GLOBALS = globals()`
- The **globals()** doesn't not return a static dictionary with all the variables declared above, but rather an object that with every new declaration that object will be updated. That's why we can access the variable `GLOBALS` even though it has been declared after the call to `globals()` and for sure **GLOBALS** will contain the Flag
```python
GLOBALS
```
## Flag
`shellmates{Le4k_V4r5_AAS_Has_jusT_STaRteD!_73298473204632}`
