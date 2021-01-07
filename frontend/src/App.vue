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
              <v-img src="https://ishwortimilsina.com/images/icon_no_avatar.svg"></v-img>
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

        <v-list-item link :to="'/profile/'+user.id+'/polls'">
          <v-list-item-icon>
            <v-icon> mdi-check-all</v-icon>
          </v-list-item-icon>
          <v-list-item-content class="text-left">
            <v-list-item-title class="text-left">Мои голосования</v-list-item-title>
          </v-list-item-content>
        </v-list-item>

        <v-list-item link to="/votes">
          <v-list-item-icon>
            <v-icon> mdi-checkbox-marked-circle-outline</v-icon>
          </v-list-item-icon>
          <v-list-item-content class="text-left">
            <v-list-item-title class="text-left">Мои голоса</v-list-item-title>
          </v-list-item-content>
        </v-list-item>

        <v-list-item link to="/voting">
          <v-list-item-icon>
            <v-icon>mdi-checkbox-multiple-marked-outline</v-icon>
          </v-list-item-icon>
          <v-list-item-content class="text-left">
            <v-list-item-title class="text-left">Все голосования</v-list-item-title>
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

        </v-navigation-drawer>

      <v-content class="px-12 py-3">
        <v-container fluid>
          <router-view @login="login" :user="user"/>
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
      login(user){
        this.user = user
      },
  },
  mounted(){
        if (this.user.id == null)
            this.$router.push('/login');
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
