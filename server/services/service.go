package services

import (
	"fmt"
	"log"
	"net"
	"os"
)

func CleanUp(sockAddr string) {
	if _, err := os.Stat(sockAddr); err == nil {
		if err := os.RemoveAll(sockAddr); err != nil {
			log.Fatal(err)
		}
	}
}

func Server(listener net.Listener) {
	for {

		fd, err := listener.Accept()
		if err != nil {
			return
		}

		fmt.Printf("Connection from %s", fd.RemoteAddr())
		go process(fd)
	}
}

func process(fd net.Conn) {
	for {

		buf := make([]byte, 512)
		nr, err := fd.Read(buf)
		if err != nil {
			break
		}

		data := buf[0:nr]
		fmt.Printf("Received: %v", string(data))

		_, err = fd.Write(data)
		if err != nil {
			log.Printf("error: %v\n", err)
			break
		}

	}
	fd.Close()
}
