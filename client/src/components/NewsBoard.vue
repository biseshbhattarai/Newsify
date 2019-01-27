<template>
<div>
    <a href="#">Logged in as {{current_user}}</a>  <button class="tuna" v-on:click="Logout">| Logout</button>
    <br>
    <button id="bacon" v-if="show" class="tuna" v-on:click="Load">Load more</button>
    <span v-if="refresh_loading" style="text-align:center">Please wait....</span>
    <div v-if="loading" class="lds-ring"><div></div><div></div><div></div><div></div></div>
    <div v-else >
        <main role="main" class="container">
        <div class="jumbotron">
            <h5 class="jacob"><strong>Filter news from these recent buzzword</strong></h5>
            <br>
            <hr>
           <ul v-for="t in topics" v-bind:key="t.news_pk">
               <Category v-bind:t="t" v-on:follow-url="FollowUrl"/>
           </ul>
           <br>
           <hr>
           <h5 class="jacob"><strong>OR</strong></h5>
        </div>
        </main>
        <main role="main" class="container">
        <div class="jumbotron">
  
           <span v-for="i in news" v-bind:key="i.title">
               <News  v-bind:i="i" v-on:like-news="like" v-on:new-url="getNew" v-on:news-comment="Comment"/>
           </span>
           
        </div>
        </main>
        <div class="footer">

        </div>
</div>
    
</div>

</template>

<script>
import News from './News.vue';
import Category from './Category.vue';
import axios from 'axios';
export default {
    name : 'NewsBoard',
    components : {
        News,
        Category
    },
    data (){
        return {
            loading : true,
            news: [],
            status_like : 'like',
            topics : [],
            refresh_loading : false,
            show : true,
            text: '',
            current_user : ''
        
        }
    },
    methods : {
        Logout : function(){
            //Clearing the storage automatically logout the user as jwt token is not been set in header.....
            localStorage.clear()
            this.$router.push('/login')
        },
        gettime(){
            let now = new Date()
            let time = now.getTime()
            console.log(time)
        },
        //Received from child component.....
        like(id){
            axios.post(`http://127.0.0.1:8000/like/${id}/`)
            .then(response => {
                console.log(response.data)
                this.$router.go()
                })
        },
        getNew(url){
            window.location.href = url
        },
        FollowUrl(id){
            axios.get(`http://127.0.0.1:8000/news/${id}`)
            .then(response => {
                alert(`You will be redirected to ${response.data.full_url}`)
                window.location.href = response.data.full_url

            })
        },
        Comment(id, text){
               // fields = ('id','author' ,'title','comment' ,'sentiment','trending', 'summary', 'like', 'full_url', 'publishedDate')
        axios.post('http://127.0.0.1:8000/comment/' , {
            text : text,
            news : id
        })
        .then(response => {
            console.log(response.data)
            this.$router.go()
        })
        .catch(err => console.log(err))
       
        },
    
        Load(){
            
            this.refresh_loading = true;
            axios.get('http://127.0.0.1:8000/fetch/')
            .then(response => {
                this.refresh_loading = false
                this.$router.go()
            })
            this.show = false
            localStorage.setItem('show', this.show)
            var self = this;
            setTimeout(function(){
                self.show = true;
            }, 1000000);
        }      
     
    },
    mounted(){
        if(localStorage.getItem('access_token') == null){
            alert('Please login to continue')
            this.$router.push('/login')
        }
   
        //Setting the headers value just after the component is mounted........
        axios.defaults.headers.common['Authorization'] = 'Bearer ' + localStorage.getItem('access_token');
        axios.get('http://127.0.0.1:8000/news/')
        .then(response => {
            console.log(response.data)
            response.data.forEach(i => this.news.push(i))
            })
            .catch(err => {
                console.log(err)
            if (err){
                console.log(err)
                if(err.response.status == 401){
                    alert("Oops ! Looks like your token has expired")
                    this.$router.push('/login')
                }
                }})
        //Fetching categories
        axios.get('http://127.0.0.1:8000/category/')
        .then(response => {
            response.data.forEach(i => this.topics.push(i))
            console.log(response.data)
            this.loading = false
            
        })
        .catch(err => {
            console.log(err)
            if(err.response.status == 401){
                this.$router.push('/login')
            }
        })
        axios.get('http://127.0.0.1:8000/user/')
        .then(response => {
            this.current_user = response.data
        })
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
ul{
    display: inline-block;
    list-style-type: none;
}

.jacob{
    text-align: center;
}

main{
    background-color: lightyellow
}
#bacon{
    margin : 0 auto;
}

.footer{
  position: fixed;
  left: 0;
  bottom: 0;
  width: 100%;
  background-color: red;
  color: white;
  text-align: center;

}

</style>
