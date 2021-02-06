<template>
<div class="Admin">
    <v-card class="mx-auto ma-3"
            elevation="4"
            outlined
            width="65%">

      <v-app-bar
        color="teal"
        dark
        flat

      >

        <v-toolbar-title><v-icon> mdi-account-key</v-icon><v-divider vertical></v-divider>
          Admin panel
        </v-toolbar-title>
        <v-spacer></v-spacer>
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
      </v-app-bar>

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
                :headers="headers_1"
                :items="voting_list_polls"
                :search="search_1"
                :sort-by="['status', 'id','question', 'description', 'user_id', 'answers', 'start_date', 'end_date', 'voted_answer']"
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
                :headers="headers_2"
                :items="voting_list_votes"
                :search="search_2"
                :sort-by="['id','question',  'author', 'answers', 'voted_answer']"
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
                :headers="headers_3"
                :items="users"
                :search="search_3"
                :sort-by="[ 'id', 'username', 'is_superuser', 'first_name', 'last_name', 'last_login', 'email', 'date_joined']"
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
                :headers="headers_4"
                :items="reports"
                :search="search_4"
                :sort-by="['status', 'id','question', 'description', 'author', 'answers']"
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
                @click="$router.go(-1);"
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
  props: ['admin', 'user'],
  data: () => ({
    voting: '',
    tabs: null,
    search_1: '',
    search_2: '',
    search_3: '',
    search_4: '',
    headers_1: [
      {text: 'Status', value: 'status'},
      {text: 'Id', value: 'id'},
      {text: 'Title', value: 'question'},
      {text: 'Description', value: 'description'},
      {text: 'Author', value: 'author'},
      {text: 'Start Date', value: 'start_date'},
      {text: 'End Date', value: 'end_date'},
      // {text: 'Answers', value: 'answers'},
      {text: 'Voted answer', value: 'voted_answer'},
    ],
    headers_3: [
      {text: 'Id', value: 'id'},
      {text: 'Username', value: 'username'},
      {text: 'First Name', value: 'first_name'},
      {text: 'Last Name', value: 'last_name'},
      {text: 'Email', value: 'email'},
      {text: 'Votes', value: 'vote_count'},
      {text: 'Polls', value: 'polls_count'},

    ],
    headers_2: [
      {text: 'Id', value: 'id'},
      {text: 'Title', value: 'question'},
      {text: 'Author', value: 'author'},
      // {text: 'Answers', value: 'answers'},
      {text: 'Voted answer', value: 'voted_answer'},
    ],
    headers_4: [
      {text: 'Status', value: 'status'},
      {text: 'Id', value: 'id'},
      {text: 'Title', value: 'title'},
      {text: 'Description', value: 'description'},
    ],
    voting_list: [],
    users: [],
    // answers: [],
    voting_list_polls: [],
    voting_list_votes: [],
    reports: [],
  }),
  methods: {
    getUsers() {
      this.axios.get('http://localhost:8000/api/users/')
          .then(response => {
            this.users = response.data
          })
      this.users.unshift({
        id: this.user.id,
        username: this.user.username,
        first_name: this.user.first_name,
        last_name: this.user.last_name,
        vote_count: this.user.vote_count,
        polls_count: this.user.polls_count,
      })
      this.search_3 = []
    },
    get_voting_list() {
      this.axios.get('http://localhost:8000/api/voting/')
          .then(response => {
            this.voting_list_polls = []
            this.voting_list_votes = []
            let data = response.data
            for (let vote of data) {
              let answers = []
              let voted_answer = -1
              for (let i = 0; i < vote.options.length; i++) {
                for (let j = 0; j < vote.options[i].users.length; j++)
                  if (vote.options[i].users[j].user.id === this.user.id)
                    voted_answer = i

                answers.push({
                  id: vote.options[i].id,
                  text: vote.options[i].text,
                  votes: vote.options[i].users.length
                })
              }
              let start = new Date(vote.start_date)
              start.setHours(start.getHours() - 3)
              let end
              if (vote.end_date) {
                end = new Date(vote.end_date)
                end.setHours(end.getHours() - 3)
              } else
                end = null
              this.voting_list_polls.unshift({
                status: vote.status,
                id: vote.id,
                question: vote.title,
                description: vote.description,
                author: vote.user.id,
                start_date: start,
                end_date: end,
                answers: answers,
                multiple: false,
                voted_answer: voted_answer
              })
              this.voting_list_votes.unshift({
                id: vote.id,
                question: vote.title,
                author: vote.user.id,
                multiple: false,
                voted_answer: voted_answer
              })
            }
            this.search_1 = []
            this.search_2 = []
          })
    },
    get_reports_list() {
      this.axios.get('http://localhost:8000/api/reports/',
            {
              headers: {Authorization: `Token ${this.user.token}`}
            })
            .then(response => {
              this.reports = response.data
            })
      this.reports.unshift({
        status: this.reports.status,
        id: this.reports.id,
        title: this.reports.title,
        description: this.reports.description,
      })
      this.search_4 = []
    }
  },



  mounted() {
      this.get_voting_list()
      this.getUsers()
      this.get_reports_list()
  }
}

</script>

<style scoped>

</style>