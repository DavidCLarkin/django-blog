import App from './App.vue'
import Post from './views/Post.vue'
import Home from './views/Home.vue'
//import Vue from 'vue'
import router from './router'
import Vue from 'vue/dist/vue.js'

Vue.config.productionTip = false
Vue.use(router)

/*
new Vue({
  router,
  delimiters: ['[[', ']]'],
  render: h => h(App)
}).$mount('#app')
*/

new Vue({
  el: "app",
  components: {App}
});

new Vue({
  el: "post",
  components:{Post}
});

new Vue({
  el: "home",
  components: {Home}
})