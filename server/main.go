package main

import (
	"log"
	"net"

	"github.com/shunhamm/remote_procedure_call/server/services"
)

func main() {
	protocol := "unix"
	sockAddr := "../tmp/echo.sock"

	services.CleanUp(sockAddr)

	log.Printf("Starting up on %s", sockAddr)
	listener, err := net.Listen(protocol, sockAddr)
	if err != nil {
		log.Fatal(err)
	}

	services.Server(listener)
}
