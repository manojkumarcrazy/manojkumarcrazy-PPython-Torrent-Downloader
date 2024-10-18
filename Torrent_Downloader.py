import libtorrent as lt
import time
import datetime
link = input("Please paste your Torrent / Magnet link here...")
ses = lt.session(lt.session_params())
ses.listen_on (6881, 6891)
params = {
'save_path': 'D:\project\Python Torrent Downloader\Torrent Downloaded',
'storage_mode': lt.storage_mode_t(2),
'paused': False,
'auto_managed': True,
'duplicate_is_error': True
}
print(link)
handle = lt.add_magnet_uri(ses, link, params)
ses.start_dht()
begin = time.time()
print(datetime.datetime.now())
print('Downloading Metadata.....')
while(not handle. has_metadata()):
   time.sleep(1) 
print('Got Metadata, Starting Torrent Download')
print('Starting', handle.name())
while(handle.status().state != lt.torrent_status. seeding):
  S = handle.status()
state_str = ['queued', 'checking', 'downloading metadata'\
'downloading', 'finished', 'seeding', 'allocating']
print('% 2f %% complete (down: %.1f kb/s up: %.1f kb/s peers: %d) %s ' % \
    (S.progress * 100, S.download_rate / 1000 , S.upload.rate  / 1000, \
     S.num_peers,state_str[S.state]))

time.sleep(5)

end=time.time()
print(handle.name(), "COMPLETED")
print("Elapsed Time:",int((end -begin) // 60),"min: ",int((end - begin) % 60),"sec: " )
print(datetime.datetime.now())