<template>
   <div id="app">
  <v-app id="inspire">
    <v-card
      max-width="500"
      class="mx-auto"
    >
      <v-img
        src="https://cdn.vuetifyjs.com/images/lists/ali.png"
        height="500px"
        dark
      >
        <v-row class="height">
          <v-card-title>
            <v-spacer></v-spacer>

            <v-btn
              dark
              icon
              class="mr-5 mb-16"
            >
              <v-icon>mdi-pencil</v-icon>
            </v-btn>

            <v-btn
              dark
              icon
              class="mb-16"
            >
              <v-icon>mdi-dots-vertical</v-icon>
            </v-btn>
          </v-card-title>

          <v-spacer></v-spacer>

          <v-card-title class="white--text pl-12 pb-10">
            <div class="display-1 pl-12 pb-10">
              {{user.first_name}} {{user.last_name}}
            </div>
          </v-card-title>
        </v-row>
      </v-img>

      <v-list three-line>
        <v-list-item>
          <v-list-item-icon>
            <v-icon color="indigo">
              mdi-account-outline
            </v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{user.username}}</v-list-item-title>
            <v-list-item-subtitle>Username</v-list-item-subtitle>
          </v-list-item-content>
       <v-btn icon>
          <v-list-item-button>
            <v-icon> mdi-pencil</v-icon>
          </v-list-item-button>
       </v-btn>
        </v-list-item>

        <v-list-item>
          <v-list-item-icon>
            <v-icon color="indigo">
               mdi-account-circle
            </v-icon>
          </v-list-item-icon>


          <v-list-item-content>
            <v-list-item-title>{{user.first_name}}</v-list-item-title>
            <v-list-item-subtitle>Firstname</v-list-item-subtitle>
          </v-list-item-content>
           <v-btn icon>
          <v-list-item-button>
            <v-icon>mdi-pencil</v-icon>
          </v-list-item-button>
           </v-btn>
        </v-list-item>

        <v-list-item>
          <v-list-item-icon>
            <v-icon color="indigo">
              mdi-account-circle
            </v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{user.last_name}}</v-list-item-title>
            <v-list-item-subtitle>Lastname</v-list-item-subtitle>
          </v-list-item-content>
           <v-btn icon>
          <v-list-item-button>
            <v-icon> mdi-pencil</v-icon>
          </v-list-item-button>
              </v-btn>
        </v-list-item>


        <v-divider inset></v-divider>

        <v-list-item>
          <v-list-item-icon>
            <v-icon color="indigo">
              mdi-email
            </v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{user.email}}</v-list-item-title>
            <v-list-item-subtitle>Email</v-list-item-subtitle>
          </v-list-item-content>
          <v-btn icon>
          <v-list-item-button>
            <v-icon> mdi-pencil</v-icon>
          </v-list-item-button>
              </v-btn>
        </v-list-item>

               <v-divider inset></v-divider>

        <v-list-item>
          <v-list-item-icon>
            <v-icon color="indigo">
              mdi-account-key
            </v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{user.password}}</v-list-item-title>
            <v-list-item-subtitle>Password</v-list-item-subtitle>
          </v-list-item-content>
          <v-btn icon>
          <v-list-item-button>
            <v-icon> mdi-pencil</v-icon>
          </v-list-item-button>
              </v-btn>
        </v-list-item>
      </v-list>
    </v-card>
  </v-app>
</div>
</template>

<script>
    export default {
        name: "Profile",
        props: ['user']
    }
</script>

<style scoped>

</style>