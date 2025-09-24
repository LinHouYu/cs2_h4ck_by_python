import pymem
import pymem.process

offset = 0X8E503C #偏移

pm = pymem.Pymem("cs2.exe") #获取游戏进程
print("游戏已启动")

client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll #获取模块

address = client + offset #完整地址👍

pm.write_bytes(address, b"\x90\x90", 2) #写入地址👍 2是两个字节👍
print("写入成功：", hex(address)) 

