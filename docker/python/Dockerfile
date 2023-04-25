FROM python:3.9.16-bullseye


ARG USERNAME=dev
ARG GROUPNAME=dev
ARG UID=1000
ARG GID=1000
ENV TZ Asia/Tokyo



COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
# ユーザー追加
RUN groupadd -g $GID $GROUPNAME && \
  useradd -m -s /bin/bash -u $UID -g $GID $USERNAME

# ユーザーのbinaryディレクトリをパスに追加
ENV PATH /home/$USERNAME/.local/bin:$PATH

# ユーザー切り替え
USER $USERNAME

RUN python -m pip install --upgrade --user pip && \
  python -m pip install --upgrade --user wheel && \
  python -m pip install --upgrade --user setuptools &&\
  python -m pip install Flask 

WORKDIR /src

ENTRYPOINT [ "/entrypoint.sh" ]
