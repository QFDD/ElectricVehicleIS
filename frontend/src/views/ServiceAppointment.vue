<template>
    <div class="root-element">
        <div class="container">
        <h2 class="mt-5">服务预约表单</h2>
        <form action="/submit-appointment" method="post" class="mt-3">
            <div class="mb-3">
                <label for="service-type" class="form-label">服务类型：</label>
                <select id="service-type" name="service-type" class="form-select">
                    <option value="routine-check">常规检查</option>
                    <option value="repair">维修</option>
                    <option value="battery-replacement">电池更换</option>
                </select>
            </div>
    
            <div class="mb-3">
                <label for="appointment-date" class="form-label">预约日期：</label>
                <input type="date" id="appointment-date" name="appointment-date" class="form-control">
            </div>
    
            <div class="mb-3">
                <label for="service-center" class="form-label">服务中心：</label>
                <select id="service-center" name="service-center" class="form-select">
                    <!-- 服务中心选项将基于数据库或API动态生成 -->
                </select>
            </div>
    
            <div class="mb-3">
                <label for="vehicle-info" class="form-label">车辆信息：</label>
                <input type="text" id="vehicle-info" name="vehicle-info" class="form-control" placeholder="车牌号或VIN">
            </div>
    
            <button type="submit" class="btn btn-primary">提交预约</button>
        </form>
    </div>
    <div class="container">
        <h2 class="mt-5">我的预约</h2>
            <div id="appointments-list" class="mt-3">
                <!-- 预约列表项将基于用户数据动态生成，示例结构如下 -->
                <div class="appointment mb-3 p-3 border rounded">
                    <p>服务类型：常规检查</p>
                    <p>预约时间：2024-04-15 14:00</p>
                    <p>服务中心：上海市浦东新区XXX服务中心</p>
                    <button onclick="editAppointment('appointmentId')" class="btn btn-secondary btn-sm">修改</button>
                    <button onclick="cancelAppointment('appointmentId')" class="btn btn-danger btn-sm">取消</button>
                </div>
                <!-- 更多预约项... -->
            </div>
        </div>
    </div>
</template>