<template>
<div>
    
    <h5> > <a href="#" v-on:click="$emit('new-url', i.full_url)">{{i.title}}</a>(<button @click="$emit('like-news', i.id)"  class="tuna">like|</button><button class="tuna" @click="click">comment)</button></h5>
   <small>Published at {{i.publishedDate}}</small> <small>| {{i.like}}</small> <small class="bacon">likes</small> <small>| 3 comment</small> <small>| Author {{i.author}} </small> <small>| Sentiment {{i.sentiment}} </small> 
    <hr>
    <form v-if="comment">
        <input type="text" v-model="text" placeholder="comment here...."/> <button @click="$emit('news-comment', i.id, text)" class="tuna">post</button> <button class="tuna" @click="close">X</button>
    </form>
    <hr>
</div>                
</template>

<script>
export default {
    name : 'News',
    props : ['i', 'text'],
    data(){
        return {
            comment : false
        }
    },
    methods : {
        click : function(){
            this.comment = true
        },
        close(){
            this.comment = false
        }
    }
}
</script>

<style scoped>

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
.bacon{
    color: blue;
}

</style>
