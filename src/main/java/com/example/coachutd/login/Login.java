package com.example.coachutd.login;

import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.example.coachutd.user.User;

import jakarta.persistence.EntityManager;
import jakarta.persistence.EntityManagerFactory;
import jakarta.persistence.Persistence;

@RestController
@RequestMapping("/authentication")
public class Login {

	@PostMapping("/login")
	public String login(Integer id, String password) {
		boolean authenticated = authorizeByIdAndPassword(id, password);
		if (authenticated) {
			return "Welcome!";
		}
		else {
			return "Sorry, please try again";
		}
	}
	private static boolean authorizeByIdAndPassword(Integer id, String password) {
	     EntityManagerFactory entityManagerFactory = Persistence.createEntityManagerFactory("PERSISTENCE");
	     EntityManager entityManager = entityManagerFactory.createEntityManager();
	     entityManager.getTransaction().begin();
	     User student = entityManager.find(User.class, id);
	     
	     if(student.password == password) {
	    	 return true;
	     }
	     return false;
	     
	}
}

