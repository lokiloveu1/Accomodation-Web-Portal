<template>
  <div style="border: #ececec 1px solid;width: 100%;margin: 0 12px;">
    <!--Coming trip-->
    <div style="background-color: #ececec;width: 100%;text-align: left;height: 45px">
      <h2 style="padding: 6px 12px 0 12px;color: #484848">Coming trip</h2>
    </div>
    <div style="margin-bottom: 20px;text-align: left">
      <a-list
        class="demo-loadmore-list"
        :loading="loading"
        itemLayout="horizontal"
        :dataSource="data"
        :pagination="pagination"
      >
        <a-list-item slot="renderItem" slot-scope="item, index">
          <a slot="actions">edit</a>
          <a slot="actions">more</a>
          <a-list-item-meta
            description="Ant Design, a design language for background applications, is refined by Ant UED Team"
          >
            <a slot="title" href="https://vue.ant.design/">{{item.name}}</a>
            <a-avatar slot="avatar" src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png" />
          </a-list-item-meta>

        </a-list-item>
      </a-list>
    </div>

    <!--My Experience-->
    <div style="background-color: #ececec;width: 100%;text-align: left;height: 45px">
      <h2 style="padding: 6px 12px 0 12px;color: #484848">My Experience</h2>
    </div>

    <div style="margin-bottom: 20px;text-align: left">
      <a-list
        class="demo-loadmore-list"
        :loading="loading"
        itemLayout="horizontal"
        :dataSource="data"
        :pagination="pagination"
      >
        <a-list-item slot="renderItem" slot-scope="item, index">
          <a-list-item-meta
            description="Ant Design, a design language for background applications, is refined by Ant UED Team"
          >
            <a slot="title" href="https://vue.ant.design/">{{item.name}}</a>
            <a-avatar slot="avatar" src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png" />
          </a-list-item-meta>

        </a-list-item>
      </a-list>
    </div>
</div>
</template>

<script>
    export default {
        data(){
          return{
            data:[
              {
               name:'apple',
              },
              {
                name:'apple',
              },
              {
                name:'apple',
              },
              {
                name:'apple',
              },
              {
                name:'apple',
              },
              {
                name:'apple',
              },
              {
                name:'apple',
              },
            ],
            pagination:{
              pageSize:3,
              showTotal:total => 'Total '+total+ ' reviews.'
            },
          }
        }
    }
</script>

<style scoped>

</style>
