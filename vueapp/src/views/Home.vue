<template>
  <div>
    <div v-for="post in posts" :key="post.title">
      <h1>{{post.title}}</h1>
      <p>{{post.text}}</p>
      <p>{{post.published_date}}</p>
      <p>{{data ? data : 'empty'}}</p>
      <a :href="`http://127.0.0.1:8000/post/${post.id}`">Link</a>
    </div>
    <a href="http://127.0.0.1:8000/accounts/login">Log In</a>
  </div>
</template>

<script>
import axios from 'axios'
axios.defaults.baseURL = "http://127.0.0.1:8000/"

export default {
  name: 'Home',
  props: ['datas'],
  components: {
    
  },
  data() {
    return {
      posts: [],
    }
  },
  mounted() {
    this.getPosts()
  },
  methods: {
    async getPosts() {
      await axios.get('posts')
      .then(response => {
        this.posts = response.data
      })
      .catch(error => {
        console.log(error)
      })
    }
  }
}
</script>
