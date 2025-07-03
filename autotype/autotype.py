import keyboard
import pyautogui
import time
import os
import sys


class AutoTyper:
    def __init__(self, input_file="input.txt"):
        self.input_file = input_file
        self.is_running = False

        # Configure pyautogui
        pyautogui.FAILSAFE = True  # Move mouse to corner to stop
        pyautogui.PAUSE = 0.05  # Small delay between actions

    def read_input_file(self):
        """Read content from the input file"""
        try:
            if os.path.exists(self.input_file):
                with open(self.input_file, "r", encoding="utf-8") as file:
                    content = file.read()
                    if content.strip():
                        return content
                    else:
                        print(f"Warning: {self.input_file} is empty")
                        return None
            else:
                print(f"Error: {self.input_file} not found")
                return None
        except Exception as e:
            print(f"Error reading {self.input_file}: {e}")
            return None

    def start_typing(self):
        """Start the auto-typing process"""
        if self.is_running:
            return

        print("🚀 Hotkey detected! Starting auto-type in 2 seconds...")
        print("💡 Tip: Move mouse to top-left corner to emergency stop")

        # Give user time to position cursor
        time.sleep(2)

        content = self.read_input_file()
        if content:
            self.is_running = True
            try:
                # Type the content with realistic speed
                for char in content:
                    if not self.is_running:
                        break
                    pyautogui.write(char, interval=0.02)  # 20ms between characters

                print("✅ Auto-typing completed!")
            except pyautogui.FailSafeException:
                print("🛑 Emergency stop activated!")
            except Exception as e:
                print(f"❌ Error during typing: {e}")
            finally:
                self.is_running = False
        else:
            print("❌ No content to type")

    def stop_typing(self):
        """Stop the auto-typing process"""
        self.is_running = False
        print("⏹️ Auto-typing stopped")

    def run(self):
        """Main loop to listen for hotkeys"""
        print("🎯 AutoTyper Started!")
        print("📁 Reading from:", os.path.abspath(self.input_file))
        print("🔥 Hotkey: Shift + Ctrl + Alt + H (start typing)")
        print("🛑 Hotkey: Shift + Ctrl + Alt + S (stop typing)")
        print("❌ Press Ctrl+C to exit program")
        print("-" * 50)

        # Register hotkeys
        keyboard.add_hotkey("shift+ctrl+alt+h", self.start_typing)
        keyboard.add_hotkey("shift+ctrl+alt+s", self.stop_typing)

        try:
            # Keep the program running
            keyboard.wait("ctrl+c")
        except KeyboardInterrupt:
            print("\n👋 AutoTyper stopped by user")
        except Exception as e:
            print(f"❌ Error: {e}")
        finally:
            # Clean up hotkeys
            keyboard.unhook_all_hotkeys()


def main():
    """Main function"""
    print("=" * 60)
    print("🤖 PYTHON AUTO-TYPER")
    print("=" * 60)

    # Check if required packages are available
    try:
        import keyboard
        import pyautogui
    except ImportError as e:
        print("❌ Missing required package!")
        print("📦 Please install required packages:")
        print("   pip install keyboard pyautogui")
        sys.exit(1)

    # Create and run the auto-typer
    auto_typer = AutoTyper("input.txt")
    auto_typer.run()


if __name__ == "__main__":
    main()
