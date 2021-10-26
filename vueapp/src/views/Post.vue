<template>
    <div id="post">
        <h1>{{title}}</h1>
        <p>{{text}}</p>
        <span>{{published_date}}</span>
    </div>
</template>

<script>
export default {
    name: "Post",
    props: ['id','title','text', 'published_date', 'author']
}
</script>

<style scoped>
#post {
    background-color: aqua;
}
</style>