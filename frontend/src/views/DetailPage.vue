<template>
  <div >
    <div style="margin-left: 5%;margin-right: 5%">
      <a-input  placeholder="Search" style="float: left;width: 50%" ><a-icon slot="prefix" type="search" /></a-input>
      <login-header style="float: right;width: 50%;"></login-header>
      <!--to clear the float-->
      <div style="clear: both"></div>
    </div>
    <div class="view_photos" >

      <div style="float:left;width: 50%">
        <img class="detailImage" src="https://a0.muscache.com/im/pictures/85b4835d-08e6-4962-a233-2ceca64524d1.jpg?aki_policy=large" style="width: 100%;height: 250px;background-size: cover;">
      </div>
      <div style="float:right;width: 50%">
        <div>
          <div style="float:left;width:50%">
            <img class="detailImage" src="https://a0.muscache.com/im/pictures/110652842/160d6e82_original.jpg?aki_policy=large" style="width:100%;height:125px;background-size: cover;">
          </div>
          <div style="float:right;width:50%">
            <img class="detailImage" src="https://a0.muscache.com/im/pictures/b58e00f7-190f-4384-8a0c-532867f5337b.jpg?aki_policy=large" style="width:100%;height:125px;background-size: cover;">
          </div>
        </div>
        <div>
          <div style="float:left;width:50%">
            <img class="detailImage" src="https://a0.muscache.com/im/pictures/6a1cab43-9353-459c-9b54-d3cbac5c8c82.jpg?aki_policy=large" style="width:100%;height:125px;background-size: cover;">
          </div>
          <div style="float:right;width:50%">
            <img class="detailImage" src="https://a0.muscache.com/im/pictures/1ea25be4-7a75-4fdf-b86b-6b2cd43204ba.jpg?aki_policy=large" style="width:100%;height:125px;background-size: cover;">
          </div>
        </div>
      </div>
    </div>
    <!--on the left is information about the house,on the right is the booking option-->
    <div style="margin-top: 50px;margin-left: 15%;margin-right: 15%;text-align: left;float: right">
      <!--left-->
      <div style="width: 58%;float: left">
        <div>
          <h1>Vacation house in etno-eco village Humac</h1>
          <a href="#">kingsford</a>
        </div>

        <!--house information-->
        <div style="padding-top: 15px">
          <a-icon style="float: left;margin-right: 10px" type="home" />
          <h4 style="margin-left: 30px">Entire house</h4>
          <div>
            <h4>
              <div class="houseinfo">7 guests</div>
              <div class="houseinfo">2 bedrooms</div>
              <div class="houseinfo">5 beds</div>
              <div class="houseinfo">2.5 baths</div>
            </h4>
          </div>
        </div>

        <!--line-->
        <div style="margin-top: 55px">
          <a-divider />
        </div>

        <!--imformation part-->
        <div>
          <p>description</p>
          <a-collapse  :bordered="false">
            <a-collapse-panel header="More information" >
              <p>text</p>
            </a-collapse-panel>
          </a-collapse>
        </div>

        <!--Amenities-->
        <div>
          <h2 style="margin-top: 20px;">Amenities</h2>
          <div>
            <div style="float:left;width:50%;margin-top: 15px">
              <span>Kitchen</span>
            </div>
            <div style="float:right;width:50%;margin-top: 15px">
              <span>Wireless Internet</span>
            </div>
          </div>

          <div>
            <div style="float:left;width:50%;margin-top: 15px;margin-bottom: 20px">
              <span>Free parking on premises</span>
            </div>
              <div style="float:right;width:50%;margin-top: 15px;margin-bottom: 20px">
              <span>Shampoo</span>
            </div>
          </div>
          <!--line-->
          <a-divider  style="margin-top: 15px"/>
        </div>

        <!--reviews-->
        <div style="margin-top: 10px;">
          <h2>100 reviews</h2>
          <a-rate :defaultValue="2.5" allowHalf disabled/>
          <a-divider />
        </div>
        <!--review rate-->
        <div>
          <div>
            <div style="float:left;width:50%;margin-top: 15px">
              <div style="float:left;width: 45%">
               <h3>Accuracy</h3>
              </div>
              <div style="float:right;width:55%;">
                <a-rate :defaultValue="2.5" allowHalf disabled />
              </div>
            </div>
            <div style="float:right;width:50%;margin-top: 15px">
              <div style="float:left;width: 45%">
                <h3>Location</h3>
              </div>
              <div style="float:right;width:55%;">
                <a-rate :defaultValue="2.5" allowHalf disabled />
              </div>
            </div>
          </div>

          <div>
            <div style="float:left;width:50%;margin-top: 15px">
              <div style="float:left;width: 45%">
                <h3>Communication</h3>
              </div>
              <div style="float:right;width:55%;">
                <a-rate :defaultValue="2.5" allowHalf disabled />
              </div>
            </div>
            <div style="float:right;width:50%;margin-top: 15px">
              <div style="float:left;width: 45%">
                <h3>Check-in</h3>
              </div>
              <div style="float:right;width:55%;">
                <a-rate :defaultValue="2.5" allowHalf disabled />
              </div>
            </div>
          </div>

          <div>
            <div style="float:left;width:50%;margin-top: 15px;margin-bottom: 20px">
              <div style="float:left;width: 45%">
                <h3>Cleanliness</h3>
              </div>
              <div style="float:right;width:55%;">
                <a-rate :defaultValue="2.5" allowHalf disabled />
              </div>
            </div>
            <div style="float:right;width:50%;margin-top: 15px;margin-bottom: 20px">
              <div style="float:left;width: 45%">
                <h3>Value</h3>
              </div>
              <div style="float:right;width:55%;">
                <a-rate :defaultValue="2.5" allowHalf disabled />
              </div>
            </div>
          </div>
          <!--line-->
          <a-divider  style="margin-top: 15px"/>
        </div>

        <!--review and reply-->
        <a-list
          class="comment-list"
          :header="`${data.length} replies`"
          itemLayout="horizontal"
          :dataSource="data"
          :pagination="pagination"
        >
          <a-list-item slot="renderItem" slot-scope="item, index">
            <a-comment
              :author="item.author"
              :avatar="item.avatar"
            >
              <template slot="actions">
                <span v-for="action in item.actions">{{action}}</span>
              </template>
              <p slot="content">{{item.content}}</p>
              <a-tooltip slot="datetime" :title="item.datetime.format('YYYY-MM-DD HH:mm:ss')">
                <span>{{item.datetime.fromNow()}}</span>
              </a-tooltip>
            </a-comment>
          </a-list-item>
        </a-list>

        <!--reply-->
        <div>
          <a-list
            v-if="comments.length"
            :dataSource="comments"
            :header="`${comments.length} ${comments.length > 1 ? 'replies' : 'reply'}`"
            itemLayout="horizontal"
          >
            <a-list-item slot="renderItem" slot-scope="item, index">
              <a-comment
                :author="item.author"
                :avatar="item.avatar"
                :content="item.content"
                :datetime="item.datetime"
              >
              </a-comment>
            </a-list-item>
          </a-list>
          <a-comment>
            <a-avatar
              slot="avatar"
              src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png"
              alt="Han Solo"
            />
            <div slot="content">
              <a-form-item>
                <a-textarea :rows="4" @change="handleChange" :value="value" ></a-textarea>
              </a-form-item>
              <a-form-item>
                <a-button
                  htmlType="submit"
                  :loading="submitting"
                  @click="handleSubmit"
                  type="primary"
                >
                  Add Comment
                </a-button>
              </a-form-item>
            </div>
          </a-comment>
        </div>

      </div>
      <!--right-->
      <div  class="choose_right" id="right_part" :class="{'is_Fixed':isFixed}">
        <div style="padding: 30px;text-align: left">
          <!--price title-->
          <div>
            <div style="float: left">
              <h2>$135</h2>
            </div>
            <div style="float: left">
              <p>per night</p>
            </div>
          </div>
          <a-divider style="width: 95%"></a-divider>
          <!--check-in-->
          <div>
          <p>Check-in</p>
          <a-date-picker
            :disabledDate="disabledStartDate"
            showTime
            format="YYYY-MM-DD"
            v-model="startValue"
            placeholder="Check-in"
            @openChange="handleStartOpenChange"
            size="large"
            style="width: 95%"
          ></a-date-picker>
        </div>
          <!--check out-->
          <div>
            <p>Check-out</p>
            <a-date-picker
              :disabledDate="disabledEndDate"
              showTime
              format="YYYY-MM-DD"
              placeholder="Check-out"
              v-model="endValue"
              :open="endOpen"
              @openChange="handleEndOpenChange"
              size="large"
              style="width: 95%"
            ></a-date-picker>
          </div>
          <!--guests-->
          <div>
            <p>Guests</p>
            <a-select
              :size="large"
              defaultValue="number of guest"
              style="width: 150px;width: 95%"
              @change="handleChangeGuests"
              v-model="guestValue"
            >
              <a-select-option v-for="i in 5" :key="i">
                {{i}}
              </a-select-option>
            </a-select>
          </div>
          <!--submit-->
          <div style="margin-top: 20px">
          <a-button type="primary" icon="check" :size="size" v-on:click="book" style="width: 95%">book</a-button>
          </div>

          <div style="margin-top: 20px;text-align: center">
            <p>You won’t be charged yet</p>
            <a-divider style="width: 95%"></a-divider>
          </div>

          <div style="margin-top: 20px">
            <p>Enter dates and number of guests to see the total trip price</p>
            <a-divider style="width: 95%"></a-divider>
          </div>

        </div>
      </div>

    </div>
    <!--back to top-->
    <a-back-top  :visibilityHeight="200"/>
  </div>
</template>

<script>
    import LoginHeader from "./../components/LoginHeader"
    import moment from 'moment'
    export default {
      components: {LoginHeader},
      data(){
        return{
          data: [
            {
              actions: ['Reply to'],
              author: 'Han Solo',
              avatar: 'https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png',
              content: 'We supply a series of design principles, practical patterns and high quality design resources (Sketch and Axure), to help people create their product prototypes beautifully and efficiently.',
              datetime: moment().subtract(1, 'days'),
            },
            {
              actions: ['Reply to'],
              author: 'Han Solo',
              avatar: 'https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png',
              content: 'We supply a series of design principles, practical patterns and high quality design resources (Sketch and Axure), to help people create their product prototypes beautifully and efficiently.',
              datetime: moment().subtract(2, 'days'),
            },
          ],
          moment,
          comments: [],
          submitting: false,
          value: '',
          pagination:{
            pageSize:1,
            showTotal:total => 'Total '+total+ ' search results.'
          },
          isFixed:false,
          offsetTop:0,
          startValue: null,
          endValue: null,
          endOpen: false,
        }
      },
      methods: {
        handleSubmit() {
          if (!this.value) {
            return;
          }

          this.submitting = true

          setTimeout(() => {
            this.submitting = false
            this.comments = [
              {
                author: 'Han Solo',
                avatar: 'https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png',
                content: this.value,
                datetime: moment().fromNow(),
              },
              ...this.comments,
            ]
            this.value = ''
          }, 1000)
        },
        handleChange(e) {
          this.value = e.target.value
        },
        handleScroll () {
          let scrollTop = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop
          if (scrollTop > this.offsetTop) {
            this.isFixed = true
          }
          else {
            this.isFixed = false
          }
        },
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
        handleChangeGuests(value) {
          console.log(`Selected: ${value}`);
        },
        /*todo*/
        book(){

        }
      },
      mounted() {
        window.addEventListener('scroll', this.handleScroll)
        this.$nextTick(()=>{
          this.offsetTop = document.querySelector('#right_part').offsetTop
        })
      },
      destroyed() {
        window.removeEventListener('scroll', this.handleScroll)
      }
    }
</script>

<style scoped>
.view_photos{
  height: 250px;
  width: 100%;
  margin-top: 20px;
  float: left;
}
.detailImage{
  cursor: pointer;
  transition: all 0.6s;
}
  .detailImage:hover{
    transform: scale(1.5);
  }
  .houseinfo{
    float: left;
    margin-left: 30px;
  }
  .choose_right{
    width:38%;
    float: right;
    border: solid 1px #e4e4e4;
  }
  .is_Fixed{
    top:10px;
    display: inline-block;/*use display to make sure other css can be applied(to deal with position);*/
    position: fixed;
    width:28%;
    margin-left: 30px;
    float: right
  }
</style>
