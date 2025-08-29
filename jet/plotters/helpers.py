def find_latency_col(df):
    for col in ["ms", "inference_ms", "time_ms"]:
        if col in df.columns:
            return col
    raise ValueError(f"No known latency column in {df.columns}")
