log_file="/var/log/pihole/pihole.log"
predict_ads_script="predict_ads.py"
blocked_domains_file="blocked_domains.txt"

if [ ! -f "$log_file" ]; then
    echo "Pi-hole log file not found: $log_file"
    exit 1
fi

# Create the blocked domains file if it doesn't exist
touch "$blocked_domains_file"

while read -r line; do
    domain=$(echo "$line" | awk '{print $(NF-2)}')
    if [[ $line == *"forwarded"* ]]; then
        prediction_result=$(python3 "$predict_ads_script" "$domain")
        prediction_value=$(echo "$prediction_result" | awk '{print $NF}')

        # Check if the domain is not already blocked
        if [ "$prediction_value" -eq 1 ] && ! grep -q "$domain" "$blocked_domains_file"; then
            pihole -b "$domain"
            echo "$domain" >> "$blocked_domains_file"
        fi
    fi
done < "$log_file"
rm "$blocked_domains_file"
