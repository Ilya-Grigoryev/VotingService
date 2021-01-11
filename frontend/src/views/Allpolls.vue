<template>
  <div class="AllPolls">
    <v-card
    class="mx-auto pa-3 ma-3"
            elevation="4"
            outlined
            width="65%">
        <v-row>
          <v-col cols="11">
              <v-text-field
                        ref="search"
                        v-model="request"
                        hide-details
                        label="Search"
                        single-line
              ></v-text-field>
          </v-col>
          <v-col cols="1">
              <v-btn
                    icon
                    @click="filter_polls"
                  >
                <v-icon>mdi-magnify</v-icon>
              </v-btn>
          </v-col>
        </v-row>
    </v-card>
      <v-card
            v-for="(voting, index) in search" :key="index"
            class="mx-auto pa-3 ma-3"
            elevation="4"
            outlined
            width="65%">
      <v-btn @click="$router.push(`/poll/${voting.id}/`)" icon depressed color="teal" style="position: absolute; right: 10px;">
        <v-icon>mdi-arrow-expand-all</v-icon>
      </v-btn>
      <Poll v-bind="voting" :user="user"/>
    </v-card>
    <div class="text-center">
    <v-pagination
        v-model="request_page"
        :length="6"
        @click="page"
      ></v-pagination>
    </div>
  </div>
</template>

<script>
import Poll from '../components/Poll.vue'

  export default {
    name: "AllPolls",
    props: ['user'],
    components: {
      Poll
    },
    data: () => ({
      voting_list: [],
      search: [],
      request: '',
      page_poll: [],
      request_page: "1"
    }),
    methods: {
      page() {
        for(let page of "3"){
          if (page === (this.request_page)) {
            this.page_poll = this.voting_list.filter(poll => poll.id.includes(this.request_page))
          }
        }
      },
      filter_polls() {
        this.search = this.voting_list.filter(poll => poll.question.includes(this.request))
      },
      get_voting_list() {
        this.axios.get('http://localhost:8000/api/voting/')
        .then(response => {
          this.voting_list = []
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
            let end = new Date(vote.end_date)
            this.voting_list.unshift({
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
          }
        this.search = this.voting_list
        })
      }
    },
    mounted() {
      this.get_voting_list()
    }
  }
</script>

<style scoped>

</style>