package main

import (
	"fmt"
	"net/http"
)

func main() {

	mux := http.NewServeMux()

	mux.HandleFunc("/health", func(res http.ResponseWriter, req *http.Request) {
		fmt.Fprint(res, "ok")
	})

	http.ListenAndServe(":8000", mux)

}
