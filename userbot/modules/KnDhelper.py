""" Userbot module for other small commands. """
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.kndhelp$")
async def usit(e):
    await e.edit(
        f"**Hai tuan {DEFAULTUSER} Kalo Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.help` Atau Bisa Minta Bantuan Ke:\n"
        "\n[Telegram](pornhub.com)"
        "\n[Repo](https://github.com/rifky81/KnD-Userbot)"
        "\n[Instagram](Instagram.com/xnxx)")


@register(outgoing=True, pattern="^.kndvar$")
async def var(m):
    await m.edit(
        f"**Disini Daftar Vars Dari {DEFAULTUSER}:**\n"
        "\n[DAFTAR VARS](https://raw.githubusercontent.com/rifky81/KnD-Userbot/KnD/varshelper.txt)")


CMD_HELP.update({
    "KnDhelper":
    "`.kndhelp`\
\nUsage: Bantuan Untuk KnD-Userbot.\
\n`.kndvar`\
\nUsage: Melihat Daftar Vars."
})
