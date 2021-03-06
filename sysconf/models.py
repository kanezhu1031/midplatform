from django.db import models
from django.db.backends.mysql.base import DatabaseWrapper
DatabaseWrapper.data_types = DatabaseWrapper._data_types

from  mirage import fields
# Create your models here.
class sys_menu(models.Model):
    """
    系统菜单表
    """
    keep_alive_choice = (
        (0, '关闭'),
        (1, '开启'),
    )
    type_choice = (
        (0, '菜单'),
        (1, '按钮'),
    )
    hidden_choice = (
        (0, '否'),
        (1, '是'),
    )
    del_flag_choice = (
        (0, '删除'),
        (1, '正常'),
    )

    title = models.CharField(max_length=300, verbose_name='菜单标题')
    code = models.CharField(null=True,max_length=300, verbose_name='菜单权限标识')
    path = models.CharField(max_length=300, verbose_name='路由URL')
    routerName = models.CharField(max_length=300, verbose_name='路由名称')
    component = models.CharField(null=True,max_length=300, verbose_name='component地址')
    redirect = models.CharField(null=True,max_length=300, verbose_name='重定向地址')
    target = models.CharField(null=True,max_length=300, verbose_name='连接跳转目标')
    parentId = models.IntegerField(verbose_name='父级菜单ID')
    icon = models.CharField(null=True,max_length=120, verbose_name='图标')
    sort = models.IntegerField(null=True, verbose_name='排序值，用于菜单排序')
    KeepAlive = models.IntegerField(default=1,choices=keep_alive_choice,verbose_name='0-关闭，1- 开启')
    type = models.IntegerField(default=0,choices=type_choice,verbose_name='菜单类型 （0-目录 1-菜单 2-按钮')
    hidden = models.IntegerField(default=0,choices=hidden_choice,verbose_name='是否隐藏路由: 0-否,1-是')
    deleted = models.IntegerField(default=1,choices=del_flag_choice,verbose_name='逻辑删除 0-删除， 1-正常')
    createTime = models.DateTimeField(auto_now=True, verbose_name='创建时间')
    updateTime = models.DateTimeField(auto_now=True,verbose_name='更新时间')

class sys_user_role(models.Model):
    """
    用户角色表
    """
    # id = models.AutoField(primary_key=False)
    user_id = models.IntegerField(verbose_name='用户ID')
    role_id = models.IntegerField(verbose_name='角色ID')

class sys_user(models.Model):
    """
    username唯一索引
    status,del_flag Btree索引

    """
    GENDER_CHOICES = (
        (0, 'Male'),
        (1, 'Female'),
    )
    LOCK_CHOICES = (
        (0, 'normal'),
        (1, 'locked'),
    )

    username = models.CharField(unique=True,null=True,max_length=100, verbose_name='用户名')
    nickname = models.CharField(null=True,max_length=100, verbose_name='显示名称')
    password = fields.EncryptedCharField(null=True,max_length=500, verbose_name='显示名称')
    type = models.IntegerField(default=5,verbose_name='0-超级管理员，1-管理员，2-项目管理员，3-开发人员，4-测试人员，5-访客')
    salt = models.CharField(null=True,max_length=100, verbose_name='MD5密码盐')
    avatar = models.CharField(null=True,max_length=100, verbose_name='头像')
    gender = models.IntegerField(choices=GENDER_CHOICES, verbose_name='性别')
    email = models.CharField(null=True,max_length=100, verbose_name='电子邮箱')
    phone = models.CharField(null=True,max_length=100, verbose_name='电话')
    status = models.IntegerField(db_index=True, choices=LOCK_CHOICES, verbose_name='用户状态，锁定 正常')
    deleted = models.CharField(max_length=200, default=0,db_index=True,verbose_name='删除状态，锁定 正常')
    createTime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updateTime = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        unique_together = ('username', 'deleted',)


class sys_role(models.Model):
    """
    username唯一索引
    status,del_flag Btree索引

    """
    DEL_CHOICES = (
        (0, 'normal'),
        (1, 'deleted'),
    )
    name = models.CharField(unique=True,null=True,max_length=100, verbose_name='用户名')
    code = models.CharField(null=True,max_length=100, verbose_name='显示名称')
    note =  models.CharField(null=True,max_length=100, verbose_name='显示名称')
    deleted = models.IntegerField(default=0,db_index=True,choices=DEL_CHOICES, verbose_name='删除状态，锁定 正常')
    createTime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updateTime = models.DateTimeField(auto_now=True, verbose_name='更新时间')

class sys_role_menu(models.Model):
    """
    角色菜单表
    """
    role_id = models.IntegerField(verbose_name='角色ID')
    permission_id = models.IntegerField(verbose_name='菜单ID')



class sys_mailserver(models.Model):
    """
    邮件服务配置
    """
    name = models.CharField(max_length=500,verbose_name='邮件服务器')
    description = models.CharField(max_length=500, verbose_name='描述信息')
    server_type = models.CharField(max_length=32, verbose_name='邮件服务器类型')
    mail_server = models.CharField(max_length=100, verbose_name='邮件服务器地址')
    smtp_port = models.IntegerField(verbose_name='smtp端口')
    protocol = models.CharField(max_length=32, verbose_name='smtp协议')
    mailusername = models.CharField(max_length=300, verbose_name='邮件发送者')
    mailpasswd = fields.EncryptedCharField(max_length=300, verbose_name='邮件密码')

class sys_webhoook(models.Model):
    """
    钉钉机器人配置管理
    """
    name = models.CharField(max_length=150,verbose_name='webhook名称')
    webhook_url = models.CharField(max_length=300, verbose_name='webhook地址')
    keyword = models.CharField(max_length=100, verbose_name='安全信息自定义关键字')
    label = models.CharField(max_length=100, verbose_name='加签')
    ip_range = models.CharField(max_length=100, verbose_name='ip段')
    createTime = models.DateTimeField(auto_now=True, verbose_name='创建时间')
    updateTime = models.DateTimeField(verbose_name='更新时间')

class sys_alarm_log(models.Model):
    """
    告警日志
    """
    name = models.CharField(max_length=300, verbose_name='告警名称')
    alarm_type = models.IntegerField(verbose_name='告警方式')
    alarm_content = models.TextField(verbose_name='告警内容')
    createTime = models.DateTimeField(auto_now=True, verbose_name='创建时间')
    updateTime = models.DateTimeField(verbose_name='更新时间')

class ossconf(models.Model):
    """
    oss配置
    """
    name = models.CharField(max_length=500, verbose_name='名称')
    description = models.CharField(max_length=500, verbose_name='描述信息')
    accessKey = models.CharField(max_length=500, verbose_name='oss访问key')
    accessSecret = fields.EncryptedCharField(max_length=500, verbose_name='oss访问secret')
    endPoint = models.CharField(max_length=500, verbose_name='oss endpoint')
    bucketName = models.CharField(max_length=500, verbose_name='bucketname')


class baseConfig(models.Model):
    name=models.CharField(max_length=50,verbose_name='配置名称')
    confKey=models.CharField(max_length=50,verbose_name='配置键')
    confValue=models.CharField(max_length=50,verbose_name='配置值')
    category=models.CharField(blank=True,max_length=255,verbose_name='分类')
    description=models.CharField(blank=True,max_length=200,verbose_name='描述')
    createTime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updateTime = models.DateTimeField(auto_now=True, verbose_name='更新时间')



