<template>
  <div class="home">
    <v-btn width="65%"
           color="teal"
           elevation="10"
           @click="$router.push('/new-poll')">
      add new poll
    </v-btn>
    <v-card
            v-for="(voting, index) in voting_list" :key="index"
            class="mx-auto pa-3 ma-3"
            elevation="4"
            outlined
            width="65%">
      <v-btn icon depressed color="teal" style="position: absolute; right: 10px;">
        <v-icon @click="$router.push(`/poll/${voting.id}/`)">mdi-arrow-expand-all</v-icon>
      </v-btn>
      <Poll v-bind="voting" :user="user"/>
    </v-card>
  </div>
</template>



<script>
  // @ is an alias to /src
  import Poll from '../components/Poll.vue'

  export default {
    name: 'Home',
    props: ['user'],
    components: {
      Poll
    },
    data: () => ({
      voting_list: []
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
                if (vote.options[i].users[j].id === this.user.id)
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
        })
      }
    },
    mounted() {
      this.get_voting_list()
    }
  }
</script>
