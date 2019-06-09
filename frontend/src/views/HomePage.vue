<template>
  <div style="margin-left: 5%;margin-right: 5%">
    <a-row class="btn-header" type="flex" justify="end" >
      <a-button class="btn-login" v-on:click="login" :size="size">Log in</a-button>
      <a-button   v-on:click="signup" :size="size">Sign up</a-button>
    </a-row>

    <a-carousel autoplay>
      <div
        slot="prevArrow" slot-scope="props"
        class="custom-slick-arrow"
        style="left: 10px;zIndex: 1"
      >
        <a-icon type="left-circle" />
      </div>
      <div
        slot="nextArrow" slot-scope="props"
        class="custom-slick-arrow"
        style="right: 10px"
      >
        <a-icon type="right-circle" />
      </div>
      <div><h3>1</h3></div>
      <div><h3>2</h3></div>
      <div><h3>3</h3></div>
      <div><h3>4</h3></div>
    </a-carousel>
    <h1 style="margin-top: 30px">NSW BNB</h1>
    <h3>Find your ideal hotel in NSW</h3>
    <div id="search-line" style="margin-top: 50px">


      <a-input size="large" placeholder="e.g. Kingsford" style="width: 200px;margin: 0 8px 8px 0;"/>

      <a-date-picker
        :disabledDate="disabledStartDate"
        showTime
        format="YYYY-MM-DD"
        v-model="startValue"
        placeholder="Check-in"
        @openChange="handleStartOpenChange"
        size="large"
      />
      <a-date-picker
        :disabledDate="disabledEndDate"
        showTime
        format="YYYY-MM-DD"
        placeholder="Check-out"
        v-model="endValue"
        :open="endOpen"
        @openChange="handleEndOpenChange"
        size="large"
      />
      <a-select
        :size="size"
        defaultValue="number of guest"
        style="width: 150px"
        @change="handleChange"
      >
        <a-select-option v-for="i in 5" :key="i">
          {{i}}
        </a-select-option>
      </a-select>
      <a-button type="primary" icon="search" :size="size">Search</a-button>

    </div>

    <div style="padding: 20px;margin-top:50px;">
      <a-row :gutter="16">
        <a-col :span="6">
          <a-card title="title" :bordered=true>
            <img
              alt="example"
              src="https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png"
              slot="cover"
            />
            <p>content</p>
          </a-card>
        </a-col>
        <a-col :span="6">
          <a-card title="title" :bordered=true>
            <img
              alt="example"
              src="https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png"
              slot="cover"
            />
            <p>content</p>
          </a-card>
        </a-col>
        <a-col :span="6">
          <a-card title="title" :bordered=true>
            <img
              alt="example"
              src="https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png"
              slot="cover"
            />
            <p>content</p>
          </a-card>
        </a-col>
        <a-col :span="6">
          <a-card title="title" :bordered=true>
            <img
              alt="example"
              src="https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png"
              slot="cover"
            />
            <p>content</p>
          </a-card>
        </a-col>

      </a-row>
    </div>


  </div>

</template>

<script>
  export default {
    data() {
      return {
        startValue: null,
        endValue: null,
        endOpen: false,
        size: 'large'
      }
    },
    watch: {
      startValue(val) {
        console.log('startValue', val)
      },
      endValue(val) {
        console.log('endValue', val)
      }
    },
    methods: {
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
      },
      login(){
        this.$router.push('/login')
      },
      signup(){
        this.$router.push('/signup')
      }
    },
  }
</script>

<style scoped>
  input::placeholder {
    color: black
  }
  .ant-carousel >>> .slick-slide {
    text-align: center;
    height: 300px;
    line-height: 300px;
    background: #364d79;
    overflow: hidden;
  }

  .ant-carousel >>> .custom-slick-arrow {
    width: 25px;
    height: 25px;
    font-size: 25px;
    color: #fff;
    background-color: rgba(31,45,61,.11);
    opacity: 0.3;
  }
  .ant-carousel >>> .custom-slick-arrow:before {
    display: none;
  }
  .ant-carousel >>> .custom-slick-arrow:hover {
    opacity: 0.5;
  }

  .ant-carousel >>> .slick-slide  h3 {
    color: #fff;
  }
  .btn-login {
    margin-right: 10px;
  }
  .btn-header {
    margin-bottom: 10px;
  }

</style>
