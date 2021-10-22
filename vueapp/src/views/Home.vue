<template>
  <div>
    <div v-for="post in posts" :key="post.title">
      <h1>{{post.title}}</h1>
      <p>{{post.text}}</p>
      <p>{{post.published_date}}</p>
      {{post}}
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',
  components: {
    
  },
  data() {
    return {
      posts: []
    }
  },
  mounted() {
    this.getPosts()
  },
  methods: {
    async getPosts() {
      await axios.get('http://127.0.0.1:8000/posts/')
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
