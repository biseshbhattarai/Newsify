<template>
    <li><button class="tuna" v-on:click="$emit('follow-url', t.news_pk)">{{t.topics}}</button></li>
</template>

<script>
export default {
    name : 'Category',
    props : ['t']
}
</script>

<style>
ul > li {
    display: inline-block;
    /* You can also add some margins here to make it look prettier */
    zoom:1;
    *display:inline;
    /* this fix is needed for IE7- */
}


.tuna {
    background:none!important;
    /* color:lightblue; */
    border:none; 
    padding:0!important;
    font: inherit;
    /*border is optional*/
    /* border-bottom:1px solid #444;  */
    cursor: pointer;

}
</style>
