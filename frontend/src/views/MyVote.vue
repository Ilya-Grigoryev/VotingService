<template>
   <div id="app" class="profile">
  <v-app id="inspire">
    <v-card flat>
      <v-card-text>
        <v-container
          fluid
          class="pa-0"
        >
          <v-row>
            <v-col
              cols="12"
              sm="3"
            >
               <v-btn
                class="ma-2"
                text
                icon
                color="blue lighten-2"
               >
                <v-icon>mdi-thumb-up</v-icon>
              </v-btn>
              <v-btn
                icon
                color="deep-orange"
              >
                <v-icon>mdi-thumb-down</v-icon>
              </v-btn>
            </v-col>
            <v-col
              cols="12"
              sm="3"
            >
              <v-btn
                icon
                color="pink"
              >
                <v-icon> mdi-comment-outline</v-icon>
              </v-btn>
            </v-col>

            <v-col
              cols="12"
              sm="3"
            >
              <v-btn
                icon
                color="indigo"
              >
                <v-icon>mdi-star</v-icon>
              </v-btn>
            </v-col>

            <v-col
              cols="12"
              sm="3"
            >
              <v-btn
                icon
                color="green"
              >
                <v-icon>mdi-share-variant</v-icon>
              </v-btn>
            </v-col>


          </v-row>
        </v-container>
      </v-card-text>
    </v-card>
  </v-app>
   </div>
</template>

      <v-btn
          class="ma-2"
          text
          icon
          color="blue lighten-2"
        >
          <v-icon>mdi-thumb-up</v-icon>
        </v-btn>

        <v-btn
          class="ma-2"
          text
          icon
          color="red lighten-2"
        >
          <v-icon>mdi-thumb-down</v-icon>
        </v-btn>