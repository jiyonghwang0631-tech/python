import webview


def main():
    webview.create_window("Timer", html="<h1>Hello World</h1>")
    webview.start(gui="qt")

if __name__ == "__main__":
    main()
