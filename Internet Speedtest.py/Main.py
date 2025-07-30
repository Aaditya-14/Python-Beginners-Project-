import speedtest
st=speedtest.Speedtest()


testno=int(input('''What speed do you want to test:  

1) Download Speed  

2) Upload Speed  

3) Ping 

Your Choice: '''))

match testno:
    case 1:
        download_speed = st.download() / 1_000_000  # Convert to Mbps
        print(f"Download Speed: {download_speed:.2f} Mbps")
    case 2:
        upload_speed = st.upload() / 1_000_000  # Convert to Mbps
        print(f"Upload Speed: {upload_speed:.2f} Mbps")
    case 3:
        st.get_servers([])
        ping = st.results.ping
        print(f"Ping: {ping:.2f} ms")
    case _:
        print("Please enter a valid value (1, 2, or 3).")