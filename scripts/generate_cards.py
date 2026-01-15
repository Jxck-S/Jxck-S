import os
import base64
import html

def get_base64_img(path):
    if not os.path.exists(path):
        return ""
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode('utf-8')

def generate_svg(name, title, url, description, color, logo_path):
    logo_b64 = get_base64_img(logo_path)
    safe_title = html.escape(title)
    safe_description = html.escape(description)
    
    svg_content = f"""<svg width="400" height="200" viewBox="0 0 400 200" fill="none" xmlns="http://www.w3.org/2000/svg">
  <foreignObject width="100%" height="100%">
    <div xmlns="http://www.w3.org/1999/xhtml">
      <style>
        .container {{
          width: 100%;
          height: 100%;
          display: flex;
          justify-content: center;
          align-items: center;
        }}
        .card {{
          width: 360px;
          height: 160px;
          background: #0d1117;
          border-radius: 12px;
          border: 1px solid #30363d;
          padding: 20px;
          font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
          color: #c9d1d9;
          display: flex;
          flex-direction: column;
          justify-content: center;
          border-left: 6px solid {color};
          box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        }}
        .header {{
          display: flex;
          align-items: center;
          gap: 15px;
          margin-bottom: 12px;
        }}
        .logo {{
          width: 48px;
          height: 48px;
          border-radius: 8px;
          background: #1a1a1a;
          object-fit: contain;
        }}
        .title {{
          font-size: 20px;
          font-weight: 700;
          margin: 0;
          color: #f0f6fc;
          letter-spacing: -0.5px;
        }}
        .url {{
          font-size: 13px;
          color: {color};
          margin-top: 2px;
          font-weight: 500;
        }}
        .description {{
          font-size: 14px;
          line-height: 1.5;
          margin: 0;
          color: #8b949e;
        }}
      </style>
      <div class="container">
        <div class="card">
          <div class="header">
            <img class="logo" src="data:image/png;base64,{logo_b64}" />
            <div>
              <h2 class="title">{safe_title}</h2>
              <div class="url">{url}</div>
            </div>
          </div>
          <p class="description">{safe_description}</p>
        </div>
      </div>
    </div>
  </foreignObject>
</svg>"""
    
    os.makedirs("assets/cards", exist_ok=True)
    with open(f"assets/cards/{name}.svg", "w") as f:
        f.write(svg_content)
    print(f"Generated assets/cards/{name}.svg")

if __name__ == "__main__":
    # Ground Control
    generate_svg(
        name="groundcontrol",
        title="Ground Control",
        url="grndcntrl.net",
        description="Targeted jet tracking and alerting platform for aircraft of interest. Optimized for precision and real time intelligence.",
        color="#58a6ff",
        logo_path="assets/icons/groundcontrol_logo.png"
    )
    
    # TheAirTraffic
    generate_svg(
        name="theairtraffic",
        title="TheAirTraffic",
        url="theairtraffic.com",
        description="Global ADS-B data aggregator and sharing service. The backbone for aviation intelligence and open data transparency.",
        color="#990000",
        logo_path="assets/icons/theairtraffic_logo.png"
    )
