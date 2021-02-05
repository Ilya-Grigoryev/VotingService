<template>
  <div class="AllPolls">
    <v-card
    class="mx-auto ma-3"
            elevation="4"
            outlined
            width="65%">
         <v-toolbar
          dark
          color="teal">
              <v-text-field
                      @input="filter_polls()"
                      @blur="filter_polls()"
                        ref="search"
                        v-model="request"
                        hide-details
                        label="Search"
                        required clearable
                        hide-no-data
                        flat
                        solo-inverted
              ></v-text-field>
    </v-toolbar>
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
    <v-card
            v-for="(voting, index) in search_2" :key="index"
            class="mx-auto pa-3 ma-3"
            elevation="4"
            outlined
            width="65%">
      <v-btn @click="$router.push(`/poll/${voting.id}/`)" icon depressed color="teal" style="position: absolute; right: 10px;">
        <v-icon>mdi-arrow-expand-all</v-icon>
      </v-btn>
      <Poll v-bind="voting" :user="user"/>
    </v-card>
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
    }),
    methods: {
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
            start.setHours(start.getHours()-3)
              let end
              if (vote.end_date) {
                  end = new Date(vote.end_date)
                  end.setHours(end.getHours() - 3)
              } else
                  end = null
            this.voting_list.unshift({
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
          }
        this.search = this.voting_list
        })
      },
      filter_polls() {
        if (this.request === '') {
          this.search = this.voting_list
          return
        }
        this.search = this.voting_list.filter(poll =>
                poll.description.includes(this.request) || poll.question.includes(this.request))
      }
    },
    mounted() {
      this.get_voting_list()
    }
}

</script>

<style scoped>

</style>