<template>
    <div class="root-element">
        <div class="container">
            <h2 class="mt-5">个人信息</h2>
            <div class="row">
                <!-- 个人信息展示区域 -->
                <div class="col-md-6">
                    <div class="mb-3">
                        <label class="form-label">姓名：</label>
                        <p class="form-control-plaintext">张三</p>
                    </div>
                    <div class="mb-3">
                        <label class="form-label">联系方式：</label>
                        <p class="form-control-plaintext">13800000000</p>
                    </div>
    
                    <!-- 可以根据需要添加更多个人信息展示 -->
                </div>

                <!-- 密码修改区域 -->
                <div class="col-md-6">
                    <h4>修改密码</h4>
                    <form action="/change-password" method="post">
                        <div class="mb-3">
                            <label for="current-password" class="form-label">当前密码</label>
                            <input type="password" class="form-control" id="current-password" name="current-password">
                        </div>
                        <div class="mb-3">
                            <label for="new-password" class="form-label">新密码</label>
                            <input type="password" class="form-control" id="new-password" name="new-password">
                        </div>
                        <div class="mb-3">
                            <label for="confirm-password" class="form-label">确认新密码</label>
                            <input type="password" class="form-control" id="confirm-password" name="confirm-password">
                        </div>
                        <button type="submit" class="btn btn-primary">更新密码</button>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>