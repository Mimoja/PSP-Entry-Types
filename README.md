# PSP-Entry-Types

Mini Library to keep track of all known PSP Entry types. Definitions are stored in `types.csv`

## Use in Go

```golang
import	pspentrytype "github.com/Mimoja/PSP-Entry-Types"
import "encoding/json"
import "os"

var AMDPSPDirectoryEntries = pspentrytype.Types()

func main(){
	enc := json.NewEncoder(os.stdout)
	enc.setIndent("", "  ")

	for _, knownType := range AMDPSPDirectoryEntries {
		enc.Encode(knownType)    
	}
}
```

## Use in Python

`pip3 install git+https://github.com/Mimoja/PSP-Entry-Types.git@master`

then

```python
import pspEntries
pspEntries.getEntries()
```
