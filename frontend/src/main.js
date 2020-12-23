import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import VueRouter from 'vue-router'
import router from './router'
import Vuelidate from 'vuelidate'
import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.use(Vuelidate)
Vue.use(VueRouter)
Vue.use(VueAxios, axios)

Vue.config.productionTip = false

new Vue({
  vuetify,
  router,
  render: h => h(App)
}).$mount('#app')
