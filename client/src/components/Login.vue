<template>
  <body class="text-center">
    <form class="form-signin">
      <h1 class="h3 mb-3 font-weight-normal">Login</h1>
      <label for="inputUsername" class="sr-only">Username</label>
      <input type="text" id="inputUsername" v-model="username" class="form-control" placeholder="Username" required autofocus>

      <label for="inputPassword" class="sr-only">Password</label>
      <input type="password" id="inputPassword" v-model="password" class="form-control" placeholder="Password" required>
 
      <button class="btn btn-lg btn-primary btn-block" v-on:click.prevent="Login" type="submit">Login</button>
      <p class="mt-5 mb-3 text-muted">&copy; 2017-2018</p>
      <h5>New member ? <router-link to="/register">Register</router-link></h5>

    </form>
  </body>
</template>

<script>
import axios from 'axios';
export default {
  name: 'Login',
  data () {
    return {
        username : null,
        password : null,
        erros : []
    }

  },
  methods: {
      Login : function(){
        //Receiving token.....
          axios.post('http://127.0.0.1:8000/api/token/', {
              username : this.username,
              password : this.password
          })
          .then(response => {
            //Store the jwt token by giving proper user credentials
            localStorage.setItem('access_token', response.data.access)
            this.$router.push('/')
          })
          .catch(error => {
              if(error){
                  this.erros.push(error)
                  console.log(error)
                  alert("Error logging")
                  }})
       

          
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

