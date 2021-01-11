<template>
   <v-app id="app">
      <v-navigation-drawer v-if="user.id != null"
              color="#5A009D"
              mini-variant-width="56"
              dark
              expand-on-hover
              hide-overlay
              permanent
              left
              app>

      <v-list nav shaped dense>
        <v-list-item class="pl-0">
          <v-list-item-avatar>
              <img v-if="user.avatar === 'null'"
                   src="https://ishwortimilsina.com/images/icon_no_avatar.svg">
              <img v-else :src="`http://localhost:8000${user.avatar}/`">
          </v-list-item-avatar>
          <v-list-item-content class="text-left">
            <v-list-item-title class="font-weight-black">{{ user.first_name }} {{ user.last_name }}</v-list-item-title>
            <v-list-item-subtitle>{{ user.email }}</v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
        <v-divider class="my-3"></v-divider>


        <v-list-item link to="/">
          <v-list-item-icon>
            <v-icon>mdi-home-outline</v-icon>
          </v-list-item-icon>
          <v-list-item-content class="text-left">
            <v-list-item-title class="text-left">Главная</v-list-item-title>
          </v-list-item-content>
        </v-list-item>


        <v-list-item link :to="'/profile/'+user.id">
          <v-list-item-icon>
            <v-icon>mdi-account-outline</v-icon>
          </v-list-item-icon>
          <v-list-item-content class="text-left">
            <v-list-item-title class="text-left">Мой профиль</v-list-item-title>
          </v-list-item-content>
        </v-list-item>


        <v-list-item link to="/all-polls">
          <v-list-item-icon>
            <v-icon>mdi-checkbox-multiple-marked-outline</v-icon>
          </v-list-item-icon>
          <v-list-item-content class="text-left">
            <v-list-item-title class="text-left">Все голосования</v-list-item-title>
          </v-list-item-content>
        </v-list-item>


        <v-list-item link to="/users">
          <v-list-item-icon>
            <v-icon>mdi-account-group-outline</v-icon>
          </v-list-item-icon>
          <v-list-item-content class="text-left">
            <v-list-item-title class="text-left">Все пользователиы</v-list-item-title>
          </v-list-item-content>
        </v-list-item>


        <v-list-item link to="/reports">
          <v-list-item-icon>
            <v-icon>mdi-alert-octagon</v-icon>
          </v-list-item-icon>
          <v-list-item-content class="text-left">
            <v-list-item-title class="text-left">Мои жалобы</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        </v-list>
        <br>
        <template v-slot:append>
          <v-list>
            <v-list-item link @click="logout" >
              <v-list-item-icon>
                <v-icon>mdi-logout-variant</v-icon>
              </v-list-item-icon>
              <v-list-item-content class="text-left">
                <v-list-item-title>Logout</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list>
        </template>
        </v-navigation-drawer>

      <v-content class="px-12 py-3">
        <v-container fluid>
          <router-view @login="login" @change-avatar="change_avatar" :user="user"/>
        </v-container>
      </v-content>

    </v-app>
</template>


<script>
export default {
  data(){
    return{
        user: {},
    }
  },
  methods:{
      change_avatar(new_avatar) {
        this.user.avatar = new_avatar
      },
      login(user){
        this.user = user
      },
      logout() {
        this.axios.post('http://localhost:8000/api/logout/',
                {},{headers: {
                  Authorization: `Token ${this.user.token}`}})
        .then(() => {
          this.user = {}
          this.$router.push('/login')
        })
      },
      getUser(token){
        this.axios.get('http://localhost:8000/api/user_by_token/', {
               headers: { Authorization: `Token ${token}`}
        }).then(response => {
          if (response.data.status === 200)
            this.user = response.data
          else
            this.$router.push('/login')
        })
      }
  },
  mounted(){
    let token = localStorage.getItem('token')
    if (token)
      this.getUser(token)
    else
      this.$router.push('/login')
    },
}
</script>


<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
