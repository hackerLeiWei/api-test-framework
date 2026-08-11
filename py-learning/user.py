import random


class User:

    def __init__(self, name, id, /, *, phone=None, email=None, **kwargs):
        """ 
        __init__ 对象的“构造函数”,不负责创建对象（创建对象是 __new__ 干的），它只负责给创建好的对象“填充数据”。
        结合你学的 / 和 *（仅限位置与关键字）
        """
        if not name:
            raise ValueError("用户名不能为空")
        if not id:
            raise ValueError("用户年龄不能为空")
        self.name = name
        self.id = id
        self.phone = phone
        self.email = email
        self.extra = kwargs
        self.head = None
        print(f"用户初始化成功:{self}")

    def __str__(self) -> str:
        return str({
            'name': self.name,
            'id': self.id,
            'phone': self.phone,
            'email': self.email,
            'extra': self.extra,
            'head': self.head
        })


# alice = User(name="Alice") # TypeError: User.__init__() got some positional-only arguments passed as keyword arguments: 'name'
# alice = User('Alice') # TypeError: User.__init__() missing 1 required positional argument: 'id'
alice = User('Alice',
             int(random.random() * 100),
             phone='12368881234',
             email='528886@qq.com',
             address="江苏省",
             hobbies=['Swimming', 'Play Game'])

print(f"alice.extra: {alice.extra}")
print(f"alice.extra['address']: {alice.extra['address']}")
print(f"alice.extra['hobbies']: {alice.extra['hobbies']}")
