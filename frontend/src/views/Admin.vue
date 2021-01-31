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
        <v-dialog v-model="dialog" persistent max-width="800px">
      <template v-slot:activator="{ on, attrs }">
         <v-btn icon
               outlined
               depressed
               v-bind="attrs"
                v-on="on"
               style="position: absolute; right: 20px;">
          <v-icon>mdi-comment-text-outline</v-icon>
        </v-btn>
          </template>
                <v-card>
                    <v-toolbar
                          color="teal"
                          dark
                        >
                          <v-toolbar-title>Chats</v-toolbar-title>
                          <v-spacer></v-spacer>
                          <v-btn icon small dark style="position: absolute; right: 30px;"
                                  @click="dialog = false">
                                  <v-icon dark>
                                    mdi-close
                                  </v-icon>
                          </v-btn>
                        </v-toolbar>
                    <v-list subheader>
                      <v-subheader>Reports</v-subheader>

                      <v-list-item
                        v-for="chat in reports"
                        :key="chat.question"
                      >
                        <v-list-item-avatar>
                          <v-img
                            :alt="`${chat.question} avatar`"
                            :src="chat.author.avatar"
                          ></v-img>
                        </v-list-item-avatar>

                        <v-list-item-content>
                          <v-list-item-title v-html="chat.question"></v-list-item-title>
                          <v-list-item-subtitle v-text="chat.description"></v-list-item-subtitle>
                        </v-list-item-content>

                        <v-list-item-icon>
                          <v-dialog v-model="dialog" persistent max-width="800px">
                            <template v-slot:activator="{ on, attrs }">
                               <v-btn icon
                                      depressed
                                      v-bind="attrs"
                                      v-on="on"
                                     style="position: absolute; right: 20px;">
                                    <v-icon :color="chat.status === 'active' ? 'deep-purple accent-4' : 'grey'">
                                      mdi-message-outline
                                  </v-icon>
                              </v-btn>
                                </template>
                                      <v-card>
                                          <v-toolbar
                                                color="teal"
                                                dark
                                              >
                                                <v-toolbar-title>{{chat.question}}</v-toolbar-title>
                                                <v-spacer></v-spacer>
                                                <v-btn icon small style="position: absolute; right: 30px;"
                                                        @click="dialog = false">
                                                        <v-icon dark>
                                                          mdi-close
                                                        </v-icon>
                                                </v-btn>
                                              </v-toolbar>
                                          <v-list-group style="border: 1px solid gray;">
                                            <v-list-item v-for="(answer, i) in chat.answers" :key="i">
                                              <v-card class="px-3 ma-2" outlined width="100%" style="text-align: left;">
                                                <v-row justify="space-between">
                                                  <v-col md="auto">
                                                    <strong style="color: #800080; cursor: pointer;"
                                                        @click="$router.push(`/profile/${answer.author.id}`)">
                                                      <u>{{ chat.author }}:</u>
                                                    </strong>
                                                  </v-col>
                                                  <v-col md="7">
                                                    {{ chat.description }}
                                                  </v-col>
                                                </v-row>
                                              </v-card>
                                            </v-list-item>
                                            <br>
                                            <v-row justify="space-between" no-gutters class="px-6">
                                              <v-col md="10">
                                                <v-text-field
                                                        v-model="message"
                                                        label="Message"
                                                        outlined>
                                                </v-text-field>
                                              </v-col>
                                              <v-col md="2">
                                                <v-btn @click="send_message()"
                                                       style="border: 2px solid #16b8fa;"
                                                       color="blue" icon x-large>
                                                  <v-icon>mdi-send</v-icon>
                                                </v-btn>
                                              </v-col>
                                            </v-row>
                                          </v-list-group>
                                      </v-card>
                              </v-dialog>
                        </v-list-item-icon>
                      </v-list-item>
                    </v-list>
                </v-card>
        </v-dialog>

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
                :sort-by="['status', 'id','question', 'description', 'author', 'answers', 'start_date', 'end_date', 'multiple', 'voted_answer']"
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
                :sort-by="[ 'id', 'username', 'is_superuser', 'first_name', 'last_name', 'last_login', 'email', 'data_joined']"
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
            { text: 'Status', value: 'status' },
            { text: 'Id', value: 'id' },
            { text: 'Title', value: 'question'},
            { text: 'Description', value: 'description' },
            { text: 'Author', value: 'user_id' },
            { text: 'Start Date', value: 'start_date' },
            { text: 'End Date', value: 'end_date' },
            { text: 'Answers', value: 'answers'},
            { text: 'Multiple', value: 'multiple' },
            { text: 'Voted answer', value: 'voted_answer' },
      ],
      headers_3: [
            { text: 'Id', value: 'id' },
            { text: 'Username', value: 'username' },
            { text: 'Is superuser', value: 'is_superuser'},
            { text: 'First Name', value: 'first_name'},
            { text: 'Last Name', value: 'last_name'},
            { text: 'Last Login', value: 'last_login'},
            { text: 'Email', value: 'email' },
            { text: 'Data joined', value: 'data_joined' },

      ],
      headers_2: [
            { text: 'Id', value: 'id' },
            { text: 'Title', value: 'question'},
            { text: 'Author', value: 'author' },
            { text: 'Answers', value: 'answers'},
            { text: 'Voted answer', value: 'voted_answer' },
      ],
      headers_4: [
            { text: 'Status', value: 'status' },
            { text: 'Id', value: 'id' },
            { text: 'Title', value: 'question'},
            { text: 'Description', value: 'description' },
            { text: 'Author', value: 'author' },
            { text: 'Answers', value: 'answers'},
      ],
      voting_list: [],
      users: [
        {
          id: 1,
          last_login: 'login',
          is_superuser: 'true',
          username: 'username',
          first_name: 'first_name',
          last_name: 'last_name',
          email: 'email',
          data_joined: 'data_joined',
        }
      ],
      voting_list_polls: [
        // {
        //   status: this.voting.status,
        //   id: this.voting.id,
        //   question: this.voting.question,
        //   description: this.voting.description,
        //   author: this.voting.author,
        //   start_date: this.voting.start,
        //   end_date: this.voting.end,
        //   answers: [],
        //   multiple: this.voting.multiple,
        //   voted_answer: this.voting.voted_answer,
        // }
      ],
      voting_list_votes: [
        //   {
        //   id: this.voting.id,
        //   question: this.voting.question,
        //   author: this.voting.author,
        //   answers: [],
        //   voted_answer: this.voting.voted_answer,
        // }
      ],
      reports: [
        {
          status: 'active',
          id: 'id_1',
          question: 'Question_1',
          description: 'Dear, admin, you have a lot of bags in your website.',
          author: 'user.id1',
          answers: [2,3,4,1],
        },
        {
          status: 'passive',
          id: 'id_2',
          question: 'Question_2',
          description: 'Please, add changing password and changing voting',
          author: 'user.id2',
          answers: [1,2,2,3],
        }
      ],
    }),
    methods: {
      getUsers() {
                this.axios.get('http://localhost:8000/api/users/')
                .then(response => {
                    this.users = response.data
                })
        this.users.unshift({
                id: this.user.id,
                last_login: this.user.last_login,
                is_superuser: this.user.is_superuser,
                username: this.user.username,
                first_name: this.user.first_name,
                last_name: this.user.last_name,
                data_joined: this.user.last_name,
              })
          this.search_3 = this.users
            },
      get_voting_list() {
        this.axios.get('http://localhost:8000/api/voting/')
        .then(response => {
          this.voting_list = []
          this.voting_list_votes = []
          this.voting_list_polls = []
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
            start.setHours(start.getHours()-3)
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
                author: vote.user,
                start_date: start,
                end_date: end,
                answers: answers,
                multiple: false,
                voted_answer: voted_answer
              })
            this.voting_list_votes.unshift({
                id: vote.id,
                question: vote.title,
                author: vote.user,
                answers: answers,
                multiple: false,
                voted_answer: voted_answer
              })
          }
        this.search_1 = this.voting_list_polls
        this.search_2 = this.voting_list_votes
        this.search_4 = this.reports
        })
      },
    },
}

</script>

<style scoped>

</style>