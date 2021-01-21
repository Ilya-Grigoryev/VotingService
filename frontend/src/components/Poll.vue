<template>
    <div class="vue-poll">
        <h2 class="qst"><strong>{{ question }}</strong></h2>
        <h4 class="qst">{{ description }}</h4>
        <div class="ans-cnt">
            <div v-for="(a,index) in calcAnswers" :key="index" :class="{ ans: true, [a.custom_class]: (a.custom_class) }">

                <template v-if="!finalResults">

                    <div v-if="!visibleResults" :class="{ 'ans-no-vote noselect': true, active: a.selected }" @click.prevent="handleVote(a, index)" >
                        <span class="txt" v-html="a.text"></span>
                    </div>
                    <div v-else :class="{ 'ans-voted': true, selected: a.selected }" >
                        <span v-if="a.percent" class="percent" v-text="a.percent"></span>
                        <span class="txt" v-html="a.text"></span>
                    </div>

                    <span class="bg" :style="{ width: visibleResults ? a.percent : '0%' }"></span>
                </template>
                <template v-else>
                    <div class="ans-voted final">
                        <span v-if="a.percent" class="percent" v-text="a.percent"></span>
                        <span class="txt" v-html="a.text"></span>
                    </div>
                    <span :class="{ bg: true, selected: mostVotes === a.votes }" :style="{ width: a.percent }"></span>
                </template>

            </div>
        </div>
        <div class="votes" v-if="showTotalVotes && (visibleResults || finalResults)" v-text="totalVotesFormatted + ' votes'"></div>

        <template v-if="!finalResults && !visibleResults && multiple && totalSelections > 0">
             <a href="#" @click.prevent="handleMultiple" class="submit" v-text="submitButtonText"></a>
        </template>

        <div style="display: flex; justify-content: space-between">
            <div>Author: <u>
                <b style="color: #800080; cursor: pointer;"
                   @click="$router.push(`/profile/${author.id}`)">
                {{ author.name }}
                </b>
            </u></div>
            <v-btn v-if="!finalResults && visibleResults"
                   @click="removeVote" depressed>remove vote</v-btn>
            <div v-if="status === 'active'">will end in: <br>
                <b>{{ time.h }} h.</b> <br>
                <b>{{ time.m }} m.</b> <br>
                <b>{{ time.s }} s.</b>
            </div>
            <div v-else-if="status === 'not started'">will start in: <br>
                <b>{{ time.h }} h.</b> <br>
                <b>{{ time.m }} m.</b> <br>
                <b>{{ time.s }} s.</b>
            </div>
            <div v-else-if="status === 'ended'">
                poll ended
            </div>
        </div>
    </div>
</template>

<script>

    export default{
        name: 'Poll',
        props: {
            status: {
                type: String,
                required: true
            },
            author: {
                type: Object,
                required: true
            },
            start_date: {
                type: Date,
                required: true
            },
            end_date: {
                type: Date,
                required: true
            },
            user: {
                type: Object,
                required: true
            },
            voted_answer: {
                type: Number,
                default: -1
            },
            id: {
                type: Number,
                required: true
            },
            question: {
                type: String,
                required: true
            },
            description: {
                type: String,
                required: true
            },
            answers: {
                type: Array,
                required: true
            },
            showResults: {
                type: Boolean,
                default: false
            },
            showTotalVotes: {
                type: Boolean,
                default: true
            },
            multiple: {
                type: Boolean,
                default: false
            },
            submitButtonText: {
                type: String,
                default: 'Vote!'
            }
        },
        data(){
            return {
                visibleResults: JSON.parse(this.showResults),
                time: {h: 0, m: 0, s: 0},
                interval: null,
                finalResults: false
            }
        },
        computed: {
            totalVotes(){
                let totalVotes = 0
                this.answers.filter(a=>{
                    if (!isNaN(a.votes) && a.votes > 0)
                        totalVotes += parseInt(a.votes)
                })
                return totalVotes
            },
            totalVotesFormatted(){
                 return this.totalVotes.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
            },
            mostVotes(){
                let max = 0
                this.answers.filter(a=>{
                    if (!isNaN(a.votes) && a.votes > 0 && a.votes >= max)
                        max = a.votes
                })

                return max
            },
            calcAnswers(){

                if (this.totalVotes === 0)
                    return this.answers.map(a=>{
                        a.percent = '0%'
                        return a
                    })

                //Calculate percent
                return this.answers.filter(a=>{
                    if (!isNaN(a.votes) && a.votes > 0)
                        a.percent = ( Math.round( (parseInt(a.votes)/this.totalVotes ) * 100) ) + '%'
                    else
                        a.percent =  '0%'

                    return a
                })
            },
            totalSelections(){
                return this.calcAnswers.filter(a => a.selected).length
            }
        },
        methods: {
            getTime () {
                if (this.status === 'active') {
                    let now = new Date(Date.now())
                    let delta = this.end_date - now
                    this.time.h = Math.floor((delta / 1000) / 3600)
                    this.time.m = Math.floor((delta / 1000) % 3600 / 60)
                    this.time.s = Math.floor((delta / 1000) % 60)
                    if (this.time.h < 0 || this.time.m < 0 || this.time.s < 0) {
                        this.finalResults = true
                        this.status = 'ended'
                        clearInterval(this.interval)
                    }
                } else if (this.status === 'not started') {
                    this.finalResults = true
                    let now = new Date(Date.now())
                    now.setHours(now.getHours() + 3)
                    let delta = this.start_date - now
                    this.time.h = Math.floor((delta / 1000) / 3600)
                    this.time.m = Math.floor((delta / 1000) % 3600 / 60)
                    this.time.s = Math.floor((delta / 1000) % 60)
                    if (this.time.h < 0 || this.time.m < 0 || this.time.s < 0) {
                        this.finalResults = false
                        this.status = 'active'
                    }
                } else if (this.status === 'ended'){
                    this.finalResults = true
                    clearInterval(this.interval)
                }
            },
            handleMultiple(){

                let arSelected = []
                this.calcAnswers.filter(a=>{
                    if (a.selected){
                        a.votes++
                        arSelected.push({ id: a.id, votes: a.votes })
                    }
                })

                this.visibleResults = true

                let obj =  { arSelected: arSelected , totalVotes: this.totalVotes }
                console.log(obj)
            },
            handleVote(a, index) { //Callback

                if (this.multiple) {

                    if (a.selected === undefined)
                        console.log("Please add 'selected: false' on the answer object")

                    a.selected = !a.selected
                    return
                }
                let option_id = a.id
                this.axios.post('http://localhost:8000/api/votedusers/',
                    {
                        option_id: option_id,
                    },
                    {
                        headers: { Authorization: `Token ${this.user.token}` }
                    }
                ).then(response => {
                    if (response.data.status === 200) {
                        a.votes++
                        a.selected = true
                        this.visibleResults = true
                        this.voted_answer = index
                    } else {
                        window.alert(`Invalid token!`)
                    }
                })
            },
            removeVote(){
                let option_id = this.answers[this.voted_answer].id
                this.axios.delete('http://localhost:8000/api/votedusers/',
                    {
                        data: { option_id: option_id },
                        headers: { Authorization: `Token ${this.user.token}` }
                    }).then(response => {
                    if (response.data.status === 200) {
                        this.visibleResults = false
                        this.answers[this.voted_answer].selected = false
                        this.answers[this.voted_answer].votes -= 1
                    } else {
                        window.alert(`Invalid token!`)
                    }
                })
            }
        },
        mounted() {
            if (this.voted_answer !== -1) {
                this.answers[this.voted_answer].selected = true
                this.visibleResults = true
            }
            this.getTime()
            this.interval = setInterval(this.getTime, 1000)
        }
    }

</script>

<style>
    .vue-poll{
      font-family: 'Avenir', Helvetica, Arial, sans-serif;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
      color: #2c3e50;
    }

    .vue-poll .noselect {
        -webkit-touch-callout: none;
        -webkit-user-select: none;
        -khtml-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
    }

    .vue-poll .qst{
        font-weight: normal;
    }
    .vue-poll .ans-cnt{
         margin: 20px 0;
    }
    .vue-poll .ans-cnt .ans{
        position: relative;
        margin-top: 10px;
    }
    .vue-poll .ans-cnt .ans:first-child{
        margin-top: 0;
    }

    .vue-poll .ans-cnt .ans-no-vote{
        text-align: center;
        border: 2px solid #77C7F7;
        box-sizing: border-box;
        border-radius: 5px;
        cursor:pointer;
        padding: 5px 0;
        transition: background .2s ease-in-out;
        -webkit-transition: background .2s ease-in-out;
        -moz-transition: background .2s ease-in-out;
    }

    .vue-poll .ans-cnt .ans-no-vote .txt{
        color: #77C7F7;
        transition: color .2s ease-in-out;
        -webkit-transition: color .2s ease-in-out;
        -moz-transition: color .2s ease-in-out;
    }

    .vue-poll .ans-cnt .ans-no-vote.active{
        background: #77C7F7;
    }

    .vue-poll .ans-cnt .ans-no-vote.active .txt{
        color: #fff;
    }

    .vue-poll .ans-cnt .ans-voted{
        padding: 5px 0;
    }

    .vue-poll .ans-cnt .ans-voted .percent,
    .vue-poll .ans-cnt .ans-voted .txt{
        position: relative;
        z-index: 1;
    }
    .vue-poll .ans-cnt .ans-voted .percent{
        font-weight: bold;
        min-width: 51px;
        display: inline-block;
        margin:0 10px;
    }

	.vue-poll .ans-cnt .ans-voted.selected .txt:after{
		content:'✔';
		margin-left: 10px;
	}

    .vue-poll .ans-cnt .ans .bg{
        position: absolute;
        width: 0%;
        top: 0;
        left: 0;
        bottom: 0;
        z-index: 0;
        background-color: #E1E8ED;
        border-top-left-radius: 5px;
        border-bottom-left-radius: 5px;
        transition: all .3s cubic-bezier(0.5,1.2,.5,1.2);
        -webkit-transition: all .3s cubic-bezier(0.5,1.2,.5,1.2);
        -moz-transition: all .3s cubic-bezier(0.5,1.2,.5,1.2);
    }

    .vue-poll .ans-cnt .ans .bg.selected{
        background-color: #77C7F7;
    }

    .vue-poll .votes{
        font-size: 14px;
        color:#8899A6
    }

    .vue-poll .submit{
        display: block;
        text-align: center;
        margin: 0 auto;
        max-width: 80px;
        text-decoration: none;
        background-color: #41b882;
        color:#fff;
        padding: 10px 25px;
        border-radius: 5px;

    }
</style>