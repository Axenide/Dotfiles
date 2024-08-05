import psutil
import pynvim

def get_nvim_sockets():
    sockets = []
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == 'nvim':
            try:
                for conn in proc.connections(kind='unix'):
                    if conn.laddr:
                        sockets.append(conn.laddr)
            except (psutil.AccessDenied, psutil.NoSuchProcess):
                continue
    return sockets

def reload_nvim():
    sockets = get_nvim_sockets()
    for socket in sockets:
        try:
            nvim = pynvim.attach('socket', path=socket)
            nvim.command('lua require("nvchad.utils").reload("themes")')
            nvim.close()
            print(f"Neovim instance at {socket} reloaded successfully.")
        except Exception as e:
            print(f"Error connecting to Neovim at {socket}: {e}")

reload_nvim()
