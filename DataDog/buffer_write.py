# --- Base FileWrite Class (For Demonstration) ---
class FileWrite:
    """
    Simulates the base class that performs actual low-level file writes.
    """

    def __init__(self, filename, mode='a'):
        self.file = open(filename, mode)
        print(f"[{filename}] File opened.")

    def write(self, data):
        """Writes data directly to the file."""
        self.file.write(data)
        print(f"[{self.file.name}] Low-level write: '{data.strip()}'")

    def close(self):
        """Closes the underlying file handle."""
        self.file.close()
        print(f"[{self.file.name}] File closed.")


# --- BufferFileWrite Implementation ---
class BufferFileWrite:
    """
    A class that buffers writes to a file before performing a single
    physical write operation (flush) when the buffer is full or explicitly called.
    """

    # 1. Constructor
    def __init__(self, filename, buffer_size=1024, mode='a'):
        """
        Initializes the buffer and the underlying FileWrite object.
        :param filename: The name of the file to write to.
        :param buffer_size: The maximum size (in characters) of the buffer.
        :param mode: The file opening mode (e.g., 'a' for append, 'w' for write).
        """
        self.file_writer = FileWrite(filename, mode)
        self.buffer_size = buffer_size
        self.current_buffer = []  # List to hold chunks of data
        self.current_buffer_length = 0

    # 2. Public Write Method
    def buffer_file_write(self, data):
        """
        Writes data to the in-memory buffer, flushing only if the buffer is full.
        """
        data_len = len(data)

        # Check if adding the new data exceeds the buffer size
        if self.current_buffer_length + data_len >= self.buffer_size:
            # First, flush the existing buffer contents
            self.buffer_file_flush()

            # If the new data is still larger than the buffer size,
            # write it directly without buffering.
            if data_len >= self.buffer_size:
                print(f"[Buffer Overflow] Data too large ({data_len} > {self.buffer_size}). Writing directly.")
                self.file_writer.write(data)
                return

        # Add data to the buffer
        self.current_buffer.append(data)
        self.current_buffer_length += data_len
        print(f"[Buffer Add] Data added. Current size: {self.current_buffer_length}/{self.buffer_size}")

    # 3. Public Flush Method
    def buffer_file_flush(self):
        """
        Writes all accumulated data in the buffer to the underlying file.
        """
        if self.current_buffer_length > 0:
            # Join all chunks in the buffer and write them in one go
            full_data_to_write = "".join(self.current_buffer)
            print(f"[Buffer Flush] Flushing {self.current_buffer_length} bytes to disk...")
            self.file_writer.write(full_data_to_write)

            # Reset the buffer after a successful flush
            self.current_buffer = []
            self.current_buffer_length = 0
            print("[Buffer Reset] Buffer cleared.")
        else:
            print("[Buffer Flush] Buffer is empty. Nothing to flush.")

    # 4. Cleanup
    def close(self):
        """
        Ensures any remaining data is flushed and the file is closed.
        """
        self.buffer_file_flush()
        self.file_writer.close()


# --- Demonstration ---
FILENAME = "temp_log.txt"
BUFFER_SIZE = 50

print("--- Starting Buffered Write Demo ---")
buffered_writer = BufferFileWrite(FILENAME, buffer_size=BUFFER_SIZE, mode='w')

# 1. Partial fills
buffered_writer.buffer_file_write("Line 1: This is a short test message.\n")
buffered_writer.buffer_file_write("Line 2: Another short message.\n")

# 2. Automatic flush (This will cause the buffer to exceed 50 characters)
buffered_writer.buffer_file_write("Line 3: This message should trigger an automatic flush before being added.\n")

# 3. Explicit flush
buffered_writer.buffer_file_write("Line 4: This data remains in the buffer.\n")
buffered_writer.buffer_file_flush()

# 4. Clean up (flushes anything left and closes the file)
buffered_writer.close()

# Note: After running, check the contents of 'temp_log.txt' to see
# the low-level writes happened in chunks.