package com.groupfour.coachutd;

import java.lang.runtime.ObjectMethods;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;


@RestController
public class HelloWorldController {
	//GET method for "Hello World" /hello-world is the URI
		@GetMapping(path="/hello-world")
		public String helloWorld() {
			return "Hello World";
		}
}

