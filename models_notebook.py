# # посты
# class Post(SQLAlchemyBaseUserTableUUID, Base):
#     post_id: Mapped[int | None] # уникальный id поста
#     text: Mapped[str | None] # содержание поста
#     type: Mapped[str | None] # личный или в канале (personal/channel)
#     author: Mapped[int | None] # id автора/канала
#     created_at: Mapped[str | None] # дата и время публикации
#
# # подписчики/друзья
# class Relation(SQLAlchemyBaseUserTableUUID, Base):
#     id: Mapped[int | None] # уникальный id связи
#     user_id: Mapped[int | None] # id пользователя
#     sub_id: Mapped[int | None] # id подписчика/друга
#     status: Mapped[str | None] # подписан, друг если вз подписка, заблокирован (subscriber, friend, blocked)
#     created_at: Mapped[str | None] # дата и время подписки
#
# # лайки
# class Likes(SQLAlchemyBaseUserTableUUID, Base):
#     id: Mapped[int | None] # уникальный id лайка
#     post_id: Mapped[int | None] # id поста к которому поставлен лайк
#     user_id: Mapped[int | None] # id лайкнувшего
#     created_at: Mapped[str | None] # дата и время лайка
#
# # комментарии
# class Comm(SQLAlchemyBaseUserTableUUID, Base):
#     id: Mapped[int | None] # уникальный id комментария
#     post_id: Mapped[int | None] # id прокомментированного поста
#     user_id: Mapped[int | None] # id автора
#     text: Mapped[str | None] # текст комментария
#     created_at: Mapped[str | None] # дата и время коммента
#
# #
# class Channels(SQLAlchemyBaseUserTableUUID, Base):
#     id: Mapped[int | None] # уникальный id канала
#     name: Mapped[str | None] # название канала
#     description: Mapped[str | None] # описание канала
#     creator_id: Mapped[int | None] # id созадателя
#     created_at: Mapped[str | None] # дата и время создания
#
# #
# class ChannelMembers(SQLAlchemyBaseUserTableUUID, Base):
#     id: Mapped[int | None] # уникальный id записи
#     channel_id: Mapped[int | None] # id канала
#     user_id: Mapped[int | None] # id пользователя
#     role: Mapped[str | None] # member, admin
#     created_at: Mapped[str | None]  # дата и время подписки
#
# # личные сообщения
# class Messages(SQLAlchemyBaseUserTableUUID, Base):
#     id: Mapped[int | None] # уникальный id сообщения
#     sender_id: Mapped[int | None] # id отправителя
#     receiver_id: Mapped[int | None] # id получателя
#     text: Mapped[str | None] # текст сообщения
#     created_at: Mapped[str | None]  # дата и время отправки сообщения
#
# # уведомления
# class Notifications(SQLAlchemyBaseUserTableUUID, Base):
#     id: Mapped[int | None] # уникальный id уведомлений
#     user_id: Mapped[int | None] # id юзера для которого уведомление
#     type: Mapped[str | None] # тип уведомления(like, comment, message, subscriber, friend_request)
#     related_id: Mapped[int | None] # id связанного с уведомлением объекта, например id лайка или сообщения
#     is_read: Mapped[str | None] # прочитано или нет
#     created_at: Mapped[str | None]  # дата и время уведомления
#
# # формирование ленты
# class Feed(SQLAlchemyBaseUserTableUUID, Base):
#     id: Mapped[int | None] # уникальный id записи
#     user_id: Mapped[str | None] # пользователь, для которого предназначен данный элемент ленты
#     post_id: Mapped[str | None] # id поста
#     created_at: Mapped[str | None]  # дата и время добавления записи в ленту