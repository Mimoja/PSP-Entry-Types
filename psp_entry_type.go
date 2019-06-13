package pspentrytype

import (
	"bufio"
	"encoding/csv"
	"encoding/json"
	"fmt"
	"io"
	"log"
	"os"
	"path/filepath"
	"runtime"
	"strconv"
)


type AMDPSPDirectoryEntryType struct {
	Type    uint32
	Name    string
    ProposedName string
	Comment string
}


func Types() []AMDPSPDirectoryEntryType {

	_, filename, _, _ := runtime.Caller(0)

	fpath := filepath.Dir(filename)
	fpath = filepath.Join(fpath, "types.csv")

    csvFile, _ := os.Open(fpath)
    reader := csv.NewReader(bufio.NewReader(csvFile))
    var entryTypes []AMDPSPDirectoryEntryType
    for {
        line, error := reader.Read()
        if error == io.EOF {
            break
        } else if error != nil {
            log.Fatal("Could not read csv: ", error)
        }
        id, _ := strconv.ParseInt(line[0], 0, 64)
        entryTypes = append(entryTypes, AMDPSPDirectoryEntryType{
            Type: uint32(id),
            Name:  line[1],
            ProposedName:  line[2],
            Comment: line[3],
        })
    }
    return entryTypes
}

