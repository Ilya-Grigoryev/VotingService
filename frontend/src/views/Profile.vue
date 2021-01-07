<template>
   <div id="app" class="profile">
  <v-app id="inspire">
    <v-card
      width="65%"
      class="mx-auto"
      elevation="4"
      outlined
    >
      <v-img
        src="https://cdn.vuetifyjs.com/images/lists/ali.png"
        height="400px"
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
              <v-icon>mdi-plus-circle-outline</v-icon>
            </v-btn>

            <v-btn
              dark
              icon
              class="mr-5 mb-16"
            >
              <v-icon> mdi-content-save</v-icon>
            </v-btn>

            <v-btn
              dark
              icon
              class="mr-5 mb-16"
            >
              <v-icon>mdi-dots-vertical</v-icon>
            </v-btn>

          </v-card-title>

          <v-spacer></v-spacer>

<!--          <v-card-title class="white&#45;&#45;text pl-12 pb-1">
              <div class="display-1 pl-12 pb-10">
              {{user.first_name}} {{user.last_name}}
              </div>
              </v-card-title>-->
        </v-row>
      </v-img>

      <v-list three-line>
        <v-list-item>
          <v-list-item-icon>
            <v-icon color="teal">
              mdi-account-outline
            </v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{user.username}}</v-list-item-title>
            <v-list-item-subtitle>Username</v-list-item-subtitle>
          </v-list-item-content>
       <v-btn icon @click="rewrite = true">
          <v-list-item-button>
            <v-icon color="teal" > mdi-pencil</v-icon>
          </v-list-item-button>
       </v-btn>
        </v-list-item>

        <v-list-item>
          <v-list-item-icon>
            <v-icon color="teal">
               mdi-account-circle
            </v-icon>
          </v-list-item-icon>


          <v-list-item-content>
            <v-list-item-title>{{user.first_name}} {{user.last_name}}</v-list-item-title>
            <v-list-item-subtitle>Name</v-list-item-subtitle>
          </v-list-item-content>
           <v-btn @click="rewrite1 = true" icon>
          <v-list-item-button>
            <v-icon color="teal">mdi-pencil</v-icon>
          </v-list-item-button>
           </v-btn>
        </v-list-item>
<!--
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
        </v-list-item>-->


        <v-divider inset></v-divider>

        <v-list-item>
          <v-list-item-icon>
            <v-icon color="teal">
              mdi-email
            </v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{user.email}}</v-list-item-title>
            <v-list-item-subtitle>Email</v-list-item-subtitle>
          </v-list-item-content>
          <v-btn icon @click="rewrite2 = true">
          <v-list-item-button>
            <v-icon color="teal"> mdi-pencil</v-icon>
          </v-list-item-button>
              </v-btn>
        </v-list-item>

        <v-divider inset></v-divider>

        <v-list-item>
          <v-list-item-icon>
            <v-icon color="teal">
              mdi-account-key
            </v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{user.password}}</v-list-item-title>
            <v-list-item-subtitle>Password</v-list-item-subtitle>
          </v-list-item-content>
          <v-btn icon @click="rewrite3 = true">
          <v-list-item-button>
            <v-icon color="teal"> mdi-pencil</v-icon>
          </v-list-item-button>
              </v-btn>
        </v-list-item>
      </v-list>
    </v-card>
    <v-row justify="center">
      <v-dialog
            v-model="rewrite"
            max-width="500px"
          >
            <v-card>
              <v-card-title>
                Username
              </v-card-title>
              <v-card-text>
                <v-text-field
                full-width
                label="New username"
                single-line
                ></v-text-field>
              </v-card-text>
              <v-card-actions>
                <v-btn
                  color="primary"
                  text
                  @click="rewrite = false"
                >
                  Save
                </v-btn>
                <v-btn
                  color="primary"
                  text
                  @click="rewrite = false"
                >
                  Close
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
    </v-row>
    <v-row justify="center">
      <v-dialog
          v-model="rewrite1"
          max-width="500px"
        >
          <v-card>
            <v-card-title>
              Name
            </v-card-title>
            <v-card-text>
              <v-text-field
              full-width
              label="New name"
              single-line
              ></v-text-field>
            </v-card-text>
            <v-card-actions>
              <v-btn
                color="primary"
                text
                @click="rewrite1 = false"
              >
                Save
              </v-btn>
              <v-btn
                color="primary"
                text
                @click="rewrite1 = false"
              >
                Close
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
    </v-row>
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