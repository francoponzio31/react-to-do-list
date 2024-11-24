package main

import (
	"log"
	appPkg "to_do_list/app"
	configPkg "to_do_list/app/config"
)

func main() {
	config := configPkg.GetConfig()
	app := appPkg.CreateApp()

	log.Fatal(app.Run(config.AppHost + ":" + config.AppPort))
}
