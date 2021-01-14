<template>
  <div class="home">
    <div  class="right">
    <v-row>
<!--    <v-col cols="6">-->
<!--    <v-card-->
<!--            v-for="(voting, index) in voting_list" :key="index"-->
<!--            class="mx-auto pa-3 ma-3"-->
<!--            elevation="4"-->
<!--            outlined-->
<!--            width="65%">-->
<!--      <v-btn @click="$router.push(`/poll/${voting.id}/`)" icon depressed color="teal" style="position: absolute; right: 10px;">-->
<!--        <v-icon>mdi-arrow-expand-all</v-icon>-->
<!--      </v-btn>-->
<!--      <Poll v-bind="voting" :user="user"/>-->
<!--    </v-card>-->
<!--    </v-col>-->
    <v-col>
    <v-card
            elevation="4"
            outlined
            width="17%">
    <v-time-picker class="pa-1"
                   position="left"
                   v-model="time"
                   format="24hr"
                   use-seconds
                   header-color="teal"
    ></v-time-picker>
    <v-date-picker class="pa-1"
                    v-model="picker"
                   position="left"
                   color="teal"
                   header-color="teal"
    ></v-date-picker>
      </v-card>
    </v-col>
    </v-row>
  </div>
  </div>
</template>



<script>
  // @ is an alias to /src
  // import Poll from '../components/Poll.vue'

  export default {
    name: 'Home',
    props: ['user'],
    // components: {
    //   Poll
    // },
    data: () => ({
      voting_list: [],
      picker: new Date().toISOString().substr(0, 10),
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
