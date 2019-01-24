<template>
<div>
    
    <h5>* ({{i.like}}){{i.title}}(<button @click="$emit('like-news', i.id)"  class="tuna">like|</button><button class="tuna" @click="click">comment)</button></h5>
    <small>34 comments</small>
    <form v-if="comment">
        <input type="text" placeholder="comment here...."/> <button class="tuna">post</button> <button class="tuna" @click="close">X</button>
    </form>
</div>                
</template>

<script>
export default {
    name : 'News',
    props : ['i'],
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

</style>
