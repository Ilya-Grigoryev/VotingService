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
<!--       <v-sheet-->
<!--        tile-->
<!--        height="54"-->
<!--        class="d-flex"-->
<!--      >-->
<!--        <v-btn-->
<!--          icon-->
<!--          class="ma-2"-->
<!--          @click="$refs.calendar.prev()"-->
<!--        >-->
<!--          <v-icon>mdi-chevron-left</v-icon>-->
<!--        </v-btn>-->
<!--        <v-select-->
<!--          v-model="type"-->
<!--          :items="types"-->
<!--          dense-->
<!--          outlined-->
<!--          hide-details-->
<!--          class="ma-2"-->
<!--          label="type"-->
<!--        ></v-select>-->
<!--        <v-select-->
<!--          v-model="mode"-->
<!--          :items="modes"-->
<!--          dense-->
<!--          outlined-->
<!--          hide-details-->
<!--          label="event-overlap-mode"-->
<!--          class="ma-2"-->
<!--        ></v-select>-->
<!--        <v-select-->
<!--          v-model="weekday"-->
<!--          :items="weekdays"-->
<!--          dense-->
<!--          outlined-->
<!--          hide-details-->
<!--          label="weekdays"-->
<!--          class="ma-2"-->
<!--        ></v-select>-->
<!--        <v-spacer></v-spacer>-->
<!--        <v-btn-->
<!--          icon-->
<!--          class="ma-2"-->
<!--          @click="$refs.calendar.next()"-->
<!--        >-->
<!--          <v-icon>mdi-chevron-right</v-icon>-->
<!--        </v-btn>-->
<!--      </v-sheet>-->
<!--      <v-sheet height="600">-->
<!--        <v-calendar-->
<!--          ref="calendar"-->
<!--          v-model="value1"-->
<!--          :weekdays="weekday"-->
<!--          :type="type1"-->
<!--          :events="events"-->
<!--          :event-overlap-mode="mode"-->
<!--          :event-overlap-threshold="30"-->
<!--          :event-color="getEventColor"-->
<!--          @change="getEvents"-->
<!--        ></v-calendar>-->
<!--      </v-sheet>-->
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
        <v-card class="mx-auto text-center"
                color="teal"
                dark
                width="100%">
      <v-card-text>
        <v-sheet color="white">
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
          </v-sheet>
        </v-card-text>
        <v-divider ></v-divider>
        <v-card-actions class="center">

        <v-btn
          text
          style="right: 5px;"
          @click="sparkline_of_polls"
        ><v-icon>mdi-checkbox-multiple-marked-outline</v-icon>
          Polls
        </v-btn>
          <v-btn
          text
          style="right: 7px;"
          @click="sparkline_of_votes"
        ><v-icon>mdi-checkbox-marked-circle-outline</v-icon>
          Votes
        </v-btn>
      </v-card-actions>
          </v-card>
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
      time: '',
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
      type1: 'month',
      types: ['month', 'week', 'day', '4day'],
      mode: 'stack',
      modes: ['stack', 'column'],
      weekday: [0, 1, 2, 3, 4, 5, 6],
      weekdays: [
        { text: 'Sun - Sat', value: [0, 1, 2, 3, 4, 5, 6] },
        { text: 'Mon - Sun', value: [1, 2, 3, 4, 5, 6, 0] },
        { text: 'Mon - Fri', value: [1, 2, 3, 4, 5] },
        { text: 'Mon, Wed, Fri', value: [1, 3, 5] },
      ],
      value1: '',
      events: [],
      colors: ['blue', 'indigo', 'deep-purple', 'cyan', 'green', 'orange', 'grey darken-1'],
      names: ['Meeting', 'Holiday', 'PTO', 'Travel', 'Event', 'Birthday', 'Conference', 'Party'],
      picker: new Date().toISOString().substr(0, 10),
      time_picker: new Date().getTime()
    }),
    methods: {
      getEvents ({ start, end }) {
      const events = []

      const min = new Date(`${start.date}T00:00:00`)
      const max = new Date(`${end.date}T23:59:59`)
      const days = (max.getTime() - min.getTime()) / 86400000
      const eventCount = this.rnd(days, days + 20)

      for (let i = 0; i < eventCount; i++) {
        const allDay = this.rnd(0, 3) === 0
        const firstTimestamp = this.rnd(min.getTime(), max.getTime())
        const first = new Date(firstTimestamp - (firstTimestamp % 900000))
        const secondTimestamp = this.rnd(2, allDay ? 288 : 8) * 900000
        const second = new Date(first.getTime() + secondTimestamp)

        events.push({
          name: this.names[this.rnd(0, this.names.length - 1)],
          start: first,
          end: second,
          color: this.colors[this.rnd(0, this.colors.length - 1)],
          timed: !allDay,
        })
      }

      this.events = events
    },
    getEventColor (event) {
      return event.color
    },
    rnd (a, b) {
      return Math.floor((b - a + 1) * Math.random()) + a
    },
      sparkline_of_polls(){
        this.axios.get('http://localhost:8000/api/voting/')
              .then(response => {
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
                  let end = new Date(vote.end_date)
                  if (voted_answer !== -1) {
                    this.voting_list_polls.unshift({
                      id: vote.id,
                      question: vote.title,
                      author: vote.user,
                      start_date: start,
                    })
                  }
                }
              })
        this.value = this.voting_list_polls
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
                      answers: answers,
                      voted_answer: voted_answer,
                      start_date: start,
                    })
                  }
                }
              })
        this.value = this.voting_list_votes
      },
    },
  }
</script>
