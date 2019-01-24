<template>
  <body class="text-center">
    <form class="form-signin">
      <h5>Already a user ? <router-link to="login">Login</router-link></h5>
      <h1 class="h3 mb-3 font-weight-normal">Please sign in</h1>
      <label for="inputUsername" class="sr-only">Username</label>
      <input type="text" id="inputUsername" class="form-control" v-model="username" placeholder="Username" required autofocus>
      <label for="inputEmail" class="sr-only">Email address</label>
      <input type="email" id="inputEmail" class="form-control" v-model="email" placeholder="Email address" required autofocus>
      <label for="inputPassword" class="sr-only">Password</label>
      <input type="password" id="inputPassword" v-model="password" class="form-control" placeholder="Password" required>
 
      <button class="btn btn-lg btn-primary btn-block" v-on:click.prevent="SignIn" type="submit">Sign in</button>
      <p class="mt-5 mb-3 text-muted">&copy; 2017-2018</p>
    </form>
  </body>
</template>

<script>
import axios from 'axios';
export default {
  name: 'Register',
  data () {
    return {
      username : null,
      email : null,
      password : null,
      erros : []
    }
  },
  methods : {
    //Create user first
    SignIn : function(){
      axios.post('http://127.0.0.1:8000/users/', {
        username : this.username,
        email : this.email,
        password : this.password
      })
      .then(response => {
        //Receive jwt token after user is created
        axios.post('http://127.0.0.1:8000/api/token/', {
          username : this.username,
          password : this.password
        })
        .then(response => {
          //Storing the jwt token in localstorage
          localStorage.setItem('access_token', response.data.access)
          this.$router.push('/newsboard')
        })
        .catch(err => {
          if(err){
            this.erros.push(err)
            console.log(err)
            alert("Error signin")
          }
        })
      })
      .catch(err => {
        if (err){
          this.erros.push(err)
          console.log(err)
          alert("Error signin")
          }
        }
      )
  
    }
}
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
body {
  height: 100%;
}

body {
  display: -ms-flexbox;
  display: flex;
  -ms-flex-align: center;
  align-items: center;
  padding-top: 40px;
  padding-bottom: 40px;
  background-color: #f5f5f5;
}

.form-signin {
  width: 100%;
  max-width: 330px;
  padding: 15px;
  margin: auto;
}
.form-signin .checkbox {
  font-weight: 400;
}
.form-signin .form-control {
  position: relative;
  box-sizing: border-box;
  height: auto;
  padding: 10px;
  font-size: 16px;
}
.form-signin .form-control:focus {
  z-index: 2;
}
.form-signin input[type="email"] {
  margin-bottom: -1px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.form-signin input[type="password"] {
  margin-bottom: 10px;
  border-top-left-radius: 0;
  border-top-right-radius: 0;
}
</style>
