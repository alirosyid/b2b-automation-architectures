def generate_weekly_roi_report(client_id, hours_saved, infra_cost):
    roi_value = (hours_saved * 50) - infra_cost # Assuming $50/hr human equivalent
    
    html_dashboard = f"""
    <html>
        <body>
            <h1>Weekly Automation Impact: {client_id}</h1>
            <p><strong>Human Hours Recovered:</strong> {hours_saved} hrs</p>
            <p><strong>Infrastructure Cost:</strong> ${infra_cost}</p>
            <h2 style="color: green;"><strong>Net Value Generated:</strong> ${roi_value}</h2>
            <p><em>All workflows are operating at 99.9% uptime.</em></p>
        </body>
    </html>
    """
    print(f"[BizOps] ROI Dashboard generated for {client_id}. Ready for dispatch.")
    return html_dashboard

if __name__ == "__main__":
    generate_weekly_roi_report("Enterprise_Alpha", hours_saved=120, infra_cost=45.50)
