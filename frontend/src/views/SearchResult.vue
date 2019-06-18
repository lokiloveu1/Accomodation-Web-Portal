<template>
  <div  style="margin-left: 5%;margin-right: 5%">
    <login-header></login-header>
    <div style="margin-top: 10px;text-align: left">
      <a-date-picker
        :disabledDate="disabledStartDate"
        :defaultValue = this.check_in_date
        format="YYYY-MM-DD"
        v-model="startValue"
        placeholder="Check-in"
        @openChange="handleStartOpenChange"
        size="large"></a-date-picker>
      <a-date-picker
        :disabledDate="disabledEndDate"
        :defaultValue = this.check_out_date
        format="YYYY-MM-DD"
        placeholder="Check-out"
        v-model="endValue"
        :open="endOpen"
        @openChange="handleEndOpenChange"
        size="large"></a-date-picker>
      <a-select
        :size="size"
        :defaultValue = this.guestnumber
        style="width: 150px"
        @change="handleChange"
      >
        <a-select-option v-for="i in 5" :key="i">
          {{i}}
        </a-select-option>
      </a-select>
      <a-divider />
    </div>
    <div style="margin-top: 20px;margin-bottom: 80px">
      <!--<div v-for="item in usermsg.slice((currentpage-1)*2,currentpage*2)">
        <p>{{item.username}}</p>
        <p>{{item.date}}</p>
      </div>
      <div>
        <span v-if="currentpage>1" @click="currentpage&#45;&#45;">pre</span>
        <span>{{currentpage}}</span>/<span>{{pagesum}}</span>
        <span v-if="currentpage<pagesum" @click="currentpage++">next</span>
      </div>-->
      <a-list
        itemLayout="vertical"
        size="large"
        :pagination="pagination"
        :dataSource="data"
      >
        <a-list-item slot="renderItem" slot-scope="item, index" key="item.title" style="text-align: left" @click="for_detail">
          <img slot="extra" width="272" alt="logo" src="https://a0.muscache.com/im/pictures/27140516/751a4207_original.jpg?aki_policy=large" />

          <a-list-item-meta
            :description="item.description"
          >
            <a slot="title" :href="item.href">{{item.title}}</a>

          </a-list-item-meta>

          {{item.content}}<br>
          <a-rate></a-rate>
        </a-list-item>
      </a-list>
    </div>
    <!--back to top-->
    <a-back-top  :visibilityHeight="200"/>
  </div>
</template>

<script>
  import LoginHeader from '../components/LoginHeader'

  const data = [
    {
      title: 'Ant Design Title 1',
      description:'Ant Design, a design language for background applications, is refined by Ant UED Team.',
      content:'We supply a series of design principles, practical patterns and high quality design resources (Sketch and Axure), to help people create their product prototypes beautifully and efficiently.'
    },
    {
      title: 'Ant Design Title 2',
      description:'Ant Design, a design language for background applications, is refined by Ant UED Team.',
      content:'We supply a series of design principles, practical patterns and high quality design resources (Sketch and Axure), to help people create their product prototypes beautifully and efficiently.'
    },
    {
      title: 'Ant Design Title 3',
      description:'Ant Design, a design language for background applications, is refined by Ant UED Team.',
      content:'We supply a series of design principles, practical patterns and high quality design resources (Sketch and Axure), to help people create their product prototypes beautifully and efficiently.'
    },
    {
      title: 'Ant Design Title 4',
      description:'Ant Design, a design language for background applications, is refined by Ant UED Team.',
      content:'We supply a series of design principles, practical patterns and high quality design resources (Sketch and Axure), to help people create their product prototypes beautifully and efficiently.'
    },
  ]
    export default {
    components:{
      LoginHeader:LoginHeader
    },
      data() {
        return {
          startValue: null,
          endValue: null,
          endOpen: false,
          size: 'large',
          data,
          /*usermsg:[
            {username:'tom',date:'1',key:1},
            {username:'tom1',date:'2',key:2},
            {username:'tom2',date:'3',key:3},
            {username:'tom3',date:'4',key:4},
          ],
          pagesum:2,
          currentpage:1,
          eachpage:2,*/
          pagination:{
            pageSize:3,
            showTotal:total => 'Total '+total+ ' search results.'
          },
          searchDetail :{}
        }
      },
      methods:{
        disabledStartDate(startValue) {
          const endValue = this.endValue;
          if (!startValue || !endValue) {
            return false;
          }
          return startValue.valueOf() > endValue.valueOf();
        },
        disabledEndDate(endValue) {
          const startValue = this.startValue;
          if (!endValue || !startValue) {
            return false;
          }
          return startValue.valueOf() >= endValue.valueOf();
        },
        handleStartOpenChange(open) {
          if (!open) {
            this.endOpen = true;
          }
        },
        handleEndOpenChange(open) {
          this.endOpen = open;
        },
        handleChange(value) {
          console.log(`Selected: ${value}`);
          this.$store.commit("updateGuestNumber",value)
        },
        for_detail(){
          this.$router.push('/detailpage')
        }
      },
      computed:{
      guestnumber(){
        return this.$store.state.guest_number
      },
        check_in_date(){
        return this.$store.state.check_in_date
        },
        check_out_date(){
        return this.$store.state.check_out_date
        }
      }
    }
</script>

<style scoped>
  input::placeholder {
    color: black
  }

</style>
