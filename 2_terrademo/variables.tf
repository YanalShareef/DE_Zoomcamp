variable "project" {
  description = "Project "
  default     = "de-zoomcamp-412612"
}

variable "region" {
  description = "Region "
  default     = "us-central1"
}



variable "location" {
  description = "Project Location"
  default     = "US"
}

variable "bq_dataset_name" {
  description = "My BigQuery Dataset name"
  default     = "demo_dataset"
}

variable "gsc_bucker_name" {
  description = "My Storage Bucket Name"
  default     = "de-zoomcamp-412612-terra-bucket"
}

variable "google_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}