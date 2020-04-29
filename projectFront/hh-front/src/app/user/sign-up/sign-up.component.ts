import { Component, OnInit } from '@angular/core';
import { UserService } from '../../services/user.service';
@Component({
  selector: 'app-sign-up',
  templateUrl: './sign-up.component.html',
  styleUrls: ['./sign-up.component.css'],
  providers: [UserService]
})
export class SignUpComponent implements OnInit {
  register;

  constructor(private userService: UserService) { }

  ngOnInit(): void {
    this.register = {
      username: '',
      password: '',
      email: ''
  };
  }
  registerUser(){
    this.userService.registerUser(this.register).subscribe(
       response => {
        alert('User' + ' ' + this.register.username + ' ' + 'has been created!')
    },
    error => console.log('error', error)
    );
  }

}
