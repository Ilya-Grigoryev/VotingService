<template>
<div class="Admin">
    <v-card class="mx-auto ma-3"
            elevation="4"
            outlined
            width="65%">

      <v-toolbar
        color="teal"
        dark
        flat
        prominent
      >

        <v-text-field
          append-icon=" mdi-database-outline"
          class="mx-4"
          flat
          hide-details
          label="Search"
          prepend-inner-icon="mdi-magnify"
          solo-inverted
        ></v-text-field>

        <template v-slot:extension>
          <v-tabs
            v-model="tabs"
            centered
          >
            <v-tab>
              <v-icon> mdi-checkbox-multiple-marked-outline</v-icon>
              Polls
            </v-tab>
            <v-tab>
              <v-icon>mdi-checkbox-marked-circle-outline</v-icon>
              Votes
            </v-tab>
            <v-tab>
               <v-icon> mdi-account-multiple-outline</v-icon>
              Users
            </v-tab>
            <v-tab>
              <v-icon> mdi-alert-octagon</v-icon>
              Reports
            </v-tab>
          </v-tabs>
        </template>
      </v-toolbar>

      <v-tabs-items v-model="tabs">
        <v-tab-item>
          <v-card flat>
            <v-card-text>
           <v-card flat>
              <v-card-title>
                <v-text-field
                  v-model="search_1"
                  append-icon="mdi-magnify"
                  label="Search"
                  single-line
                  hide-details
                ></v-text-field>
              </v-card-title>
              <v-data-table
                :headers="headers"
                :items="desserts"
                :search="search_1"
                :sort-by="['calories', 'fat']"
                :sort-desc="[false, true]"
                multi-sort
                class="elevation-1"
              ></v-data-table>
            </v-card>
            </v-card-text>
          </v-card>
        </v-tab-item>
        <v-tab-item>
          <v-card flat>
            <v-card-text>
           <v-card flat>
              <v-card-title>
                <v-text-field
                  v-model="search_2"
                  append-icon="mdi-magnify"
                  label="Search"
                  single-line
                  hide-details
                ></v-text-field>
              </v-card-title>
              <v-data-table
                :headers="headers"
                :items="desserts"
                :search="search_2"
                :sort-by="['calories', 'fat']"
                :sort-desc="[false, true]"
                multi-sort
                class="elevation-1"
              ></v-data-table>
            </v-card>
            </v-card-text>
          </v-card>
        </v-tab-item>
        <v-tab-item>
          <v-card flat>
            <v-card-text>
           <v-card flat>
              <v-card-title>
                <v-text-field
                  v-model="search_3"
                  append-icon="mdi-magnify"
                  label="Search"
                  single-line
                  hide-details
                ></v-text-field>
              </v-card-title>
              <v-data-table
                :headers="headers"
                :items="desserts"
                :search="search_3"
                :sort-by="['calories', 'fat']"
                :sort-desc="[false, true]"
                multi-sort
                class="elevation-1"
              ></v-data-table>
            </v-card>
            </v-card-text>
          </v-card>
        </v-tab-item>
                <v-tab-item>
          <v-card flat>
            <v-card-text>
           <v-card flat>
              <v-card-title>
                <v-text-field
                  v-model="search_4"
                  append-icon="mdi-magnify"
                  label="Search"
                  single-line
                  hide-details
                ></v-text-field>
              </v-card-title>
              <v-data-table
                :headers="headers"
                :items="desserts"
                :search="search_4"
                :sort-by="['calories', 'fat']"
                :sort-desc="[false, true]"
                multi-sort
                class="elevation-1"
              ></v-data-table>
            </v-card>
            </v-card-text>
          </v-card>
        </v-tab-item>
      </v-tabs-items>
         <v-btn
                @click="$router.push(`/login`);"
                dark
                class="mx-auto ma-3"
                depressed
                color="teal"
                elevation="4"
                style="position: absolute; right: 20px;"
                >exit
              <v-icon>mdi-exit-to-app</v-icon>
            </v-btn>
      </v-card>

</div>
</template>

<script>

export default {
    name: "Admin",
    props: ['admin'],
    data: () => ({
      tabs: null,
      users: [''],
      search_1: '',
      search_2: '',
      search_3: '',
      search_4: '',
      voting_list: [],
      voting_list_polls: [],
      voting_list_votes: [],
      reports: [],
    }),
}

</script>

<style scoped>

</style>