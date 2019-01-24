<template>
<div>
    <div v-if="loading" class="lds-ring"><div></div><div></div><div></div><div></div></div>
    <div v-else >
        <main role="main" class="container">
        <div class="jumbotron">
           <span v-for="i in news" v-bind:key="i.title">
               <News v-bind:i="i" v-on:like-news="like"/>
           </span>
           
        </div>
        </main>
</div>
    
</div>

</template>

<script>
import News from './News.vue';
import axios from 'axios';
export default {
    name : 'NewsBoard',
    components : {
        News
    },
    data (){
        return {
            loading : true,
            news: [],
            status_like : 'like'
        
        }
    },
    methods : {
        Logout : function(){
            //Clearing the storage automatically logout the user as jwt token is not been set in header.....
            localStorage.clear()
            this.$router.push('/')
        },
        //Received from child component.....
        like(id){
            axios.post(`http://127.0.0.1:8000/like/${id}/`)
            .then(response => {
                console.log(response.data)
                this.$router.go()
                })
        }
      
     
    },
    mounted(){
        //Setting the headers value just after the component is mounted........
        axios.defaults.headers.common['Authorization'] = 'Bearer ' + localStorage.getItem('access_token');
        axios.get('http://127.0.0.1:8000/news/')
        .then(response => {
            console.log(response.data)
            response.data.forEach(i => this.news.push(i))
            })
            .catch(err => {
            if (err){
                console.log(err)
                }})
        //Fetching categories
        axios.get('http://127.0.0.1:8000/category/')
        .then(response => {
            console.log(response.data)
            this.loading = false
            
        })
        .catch(err => console.log(err))
    },
    

}
</script>

<style scoped>

.lds-ring {
    
  margin: 0 auto;
  width: 64px;
  height: 64px;
}
.lds-ring div {
  box-sizing: border-box;
  display: block;
  position: absolute;
  width: 51px;
  height: 51px;
  margin: 6px;
  border: 6px solid #000;
  border-radius: 50%;
  animation: lds-ring 1.2s cubic-bezier(0.5, 0, 0.5, 1) infinite;
  border-color: #000 transparent transparent transparent;
}
.lds-ring div:nth-child(1) {
  animation-delay: -0.45s;
}
.lds-ring div:nth-child(2) {
  animation-delay: -0.3s;
}
.lds-ring div:nth-child(3) {
  animation-delay: -0.15s;
}
@keyframes lds-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
.btn-like {
    background-color: #fff;
    border: 1px solid #ddd;
    padding: 10px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 20px;
    margin: 3px 1px;
}

.tuna {
     background:none!important;
     color:lightblue;
     border:none; 
     padding:0!important;
     font: inherit;
     /*border is optional*/
     /* border-bottom:1px solid #444;  */
     cursor: pointer;
}


</style>
