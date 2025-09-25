# AWS S3 Enumeration Tool

A simple script to solve the http://flaws.cloud lab by enumerating AWS S3 buckets.

## How to Use

1. **Clone the repository**
   ```bash
   https://github.com/debanandsingha/aws_s3_enum.git
   cd awsS3_enum
   ```

2. **Create virtual environment**
   ```bash
   python3 -m venv myenv
   ```

3. **Activate the virtual environment**
   ```bash
   source myenv/bin/activate
   ```

4. **Install requirements**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the script**
   ```bash
   python3 aws_s3_enum.py http://flaws.cloud
   ```
