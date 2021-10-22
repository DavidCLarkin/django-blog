<template>
    <div>
        <div>
            <h1>{{post.title}}</h1>
        </div>
    </div>
</template>

<script>
export default {
    name: "Post",
    props: [
        'post',
    ]
}
</script>