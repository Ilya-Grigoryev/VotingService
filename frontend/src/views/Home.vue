<template>
  <div>
    <v-card class="mx-auto pa-3 ma-3"
            elevation="4"
            outlined
            width="65%">
      <v-carousel>
      <v-carousel-item
        v-for="(item,i) in items"
        :key="i"
        :src="item.src"
        reverse-transition="fade-transition"
        transition="fade-transition"
      ></v-carousel-item>
    </v-carousel>
      <v-divider></v-divider>
      </v-card>

    <v-card class="mx-auto pa-3 ma-3 "
            elevation="4"
            outlined
            width="65%">
          <v-row>
      <v-col cols="3">
      <v-date-picker
        v-model="picker"
        color="teal"
        width="99%"
        @click="date()"
      ></v-date-picker>
      </v-col>
            <v-divider vertical></v-divider>
      <v-col cols="8,5">
      <v-container fluid >
      <v-sparkline
        :value="value"
        :gradient="gradient"
        :smooth="radius || false"
        :padding="padding"
        :line-width="width"
        :stroke-linecap="lineCap"
        :gradient-direction="gradientDirection"
        :fill="fill"
        :type="type"
        :auto-line-width="autoLineWidth"
        auto-draw
      ></v-sparkline>
        <v-divider ></v-divider>
        <v-radio-group
        v-model="radios"
        mandatory
      ><template v-slot:label>
          <div><strong>Choose to show on sparkline:</strong></div>
        </template>
       <v-radio value="Polls" color="teal"  @click="sparkline_of_polls">
          <template v-slot:label >
            <div><strong class="text">Polls</strong></div>
          </template>
        </v-radio>
        <v-radio value="Votes" color="teal"  @click="sparkline_of_votes">
          <template v-slot:label >
            <div><strong class="text">Votes</strong></div>
          </template>
        </v-radio>
      </v-radio-group>
      </v-container>
       </v-col>
    </v-row>
    </v-card>

  </div>
</template>



<script>
  // @ is an alias to /src
  // import Poll from '../components/Poll.vue'

  const gradients = [
  ['#222'],
  ['#42b3f4'],
  ['red', 'orange', 'yellow'],
  ['purple', 'violet'],
  ['#00c6ff', '#F0F', '#FF0'],
  ['#f72047', '#ffd200', '#1feaea'],
]
  export default {
    name: 'Home',
    props: ['user'],

    data: () => ({
      radios: 'teal',
      voting_list: [],
      width: 2,
      radius: 10,
      padding: 8,
      lineCap: 'round',
      gradient: gradients[5],
      value: [0, 2, 5, 9, 5, 10, 3, 5, 0, 0, 1, 8, 2, 9, 0],
      gradientDirection: 'top',
      gradients,
      fill: false,
      type: 'trend',
      autoLineWidth: false,
      date: new Date(),
      time: new Date(),
      items: [
        {
          src: 'https://cdn.vuetifyjs.com/images/carousel/squirrel.jpg',
        },
        {
          src: 'https://cdn.vuetifyjs.com/images/carousel/sky.jpg',
        },
        {
          src: 'https://cdn.vuetifyjs.com/images/carousel/bird.jpg',
        },
        {
          src: 'https://cdn.vuetifyjs.com/images/carousel/planet.jpg',
        },
      ],
      picker: new Date().toISOString().substr(0, 10),
    }),
    methods: {
      date(){

      },
      sparkline_of_polls(){
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
                  if (voted_answer !== -1) {
                    this.voting_list_votes.unshift({
                      id: vote.id,
                      question: vote.title,
                      description: vote.description,
                      author: vote.user,
                      start_date: start,
                      end_date: end,
                      answers: answers,
                      multiple: false,
                      voted_answer: voted_answer,
                      status: vote.status
                    })
                  }
                }
              })
        this.value = this.voting_list
      },
      sparkline_of_votes() {
        this.axios.get('http://localhost:8000/api/voting/')
              .then(response => {
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
                  let end = new Date(vote.end_date)
                  if (voted_answer !== -1) {
                    this.voting_list_votes.unshift({
                      id: vote.id,
                      question: vote.title,
                      description: vote.description,
                      author: vote.user,
                      start_date: start,
                      end_date: end,
                      answers: answers,
                      multiple: false,
                      voted_answer: voted_answer,
                      status: vote.status
                    })
                  }
                }
              })
        this.value = this.voting_list_votes
      },
    },
  }
</script>
