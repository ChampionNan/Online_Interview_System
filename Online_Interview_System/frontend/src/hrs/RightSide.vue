<template>
  <div>
    <el-row>
      <el-col :span="20" offset="3">
        <div class="title">面试官</div>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="5" offset="5">
        <el-checkbox v-model="checked1">有空闲时间</el-checkbox>
      </el-col>
      <el-col :span="5" offset="5">
        <el-checkbox v-model="checked2">无空闲时间</el-checkbox>
      </el-col>
    </el-row>
    <el-col :span="18" offset="9">
      <el-row v-for="(item, index) in nameList" v-bind:key="item">
        <el-card class="box-card" shadow="hover" @click="opendialogFormVisible(index)">
          <div class="icon"><el-avatar :size="50" :src="circleUrl"></el-avatar></div>
          <div class="item">Name:{{ item.name }}</div>
          <div class="item">Email:{{ item.email }}</div>
        </el-card>
      </el-row>
    </el-col>
    <el-dialog title="面试官信息" :visible.sync="dialogFormVisible">
      <el-form :model="form">
        <el-form-item label="活动名称" :label-width="formLabelWidth">
          <el-input v-model="form.name" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="活动区域" :label-width="formLabelWidth">
          <el-select v-model="form.region" placeholder="请选择活动区域">
            <el-option label="区域一" value="shanghai"></el-option>
            <el-option label="区域二" value="beijing"></el-option>
          </el-select>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="dialogFormVisible = false">确 定</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
export default {
  name: 'RightSide',
  data () {
    return {
      circleUrl: 'https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png',
      checked1: false,
      checked2: false,
      nameList: [{
        name: '面试官1',
        email: 'fir@ustc.edu.cn',
        state: 1//  有空闲时间
      }, {
        name: '面试官2',
        email: 'sec@ustc.edu.cn',
        state: 1
      }, {
        name: '面试官3',
        email: 'thi@ustc.edu.cn',
        state: 1
      }, {
        name: '面试官4',
        email: 'for@ustc.edu.cn',
        state: 1
      }],
      sequence: 0
    }
  },
  methods: {
    opendialogFormVisible: function (index) {
      this.dialogTableVisible = true
      this.sequence = index // 表示是第几个card
    }
  }
}
</script>

<style scoped>
  .el-row {
    margin-bottom: 25px;
    &:last-child {
      margin-bottom: 0;
    }
  }
  .el-col {
    border-radius: 4px;
  }
  .icon {
    float: left;
  }
  .but {
    padding-top: 0;
  }
  .item {
    padding-left: 20px;
    margin-bottom: 13px;
  }
  .title {
    margin-top: 0px;
    margin-right: 5px;
    font-size: 30px;
    line-height: 50px;
    text-align: center;
  }
  .box-card {
    font-size: 16px;
    width: 400px;
    height: 100px;
    margin-left: -100px;
    border-radius: 20px;
    border-width: 2px;
  }
  .grid-content {
    border-radius: 4px;
    min-height: 26px;
  }
  .row-bg {
    padding: 10px 0;
    background-color: #f9fafc;
  }
</style>
