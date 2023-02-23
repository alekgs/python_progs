import vk
session = vk.Session()
vk_api = vk.API(session)
vk_api.users.get(user_id=1)
