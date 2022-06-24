from src.s3 import S3

def main():
	s3 = S3()
	s3.clear_input_bucket()
	s3.clear_output_bucket()
	print("Running Test Case 1")
	s3.upload_files("test_case_1")
	print("Running Test Case 2")
	s3.upload_files("test_case_2")

if __name__=="__main__":
	main()