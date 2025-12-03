flowchart TD

%% NODES
A([🔧 Sensor Data Collection]) 
B([🗄️ Database Storage])
C([📥 Fetch Latest Data])
D([🤖 AI/ML Model Processing])
E([⏳ RUL Prediction])
F([🖥️ Local Website Dashboard])

%% FLOW
A --> B --> C --> D --> E --> F

%% STYLES
style A fill:#ffdd99,stroke:#d48806,stroke-width:2px,color:#000,font-weight:bold
style B fill:#c2e8ff,stroke:#0277bd,stroke-width:2px,color:#000,font-weight:bold
style C fill:#d7ffd9,stroke:#2e7d32,stroke-width:2px,color:#000,font-weight:bold
style D fill:#ffd6e7,stroke:#c2185b,stroke-width:2px,color:#000,font-weight:bold
style E fill:#fff2a8,stroke:#f9a825,stroke-width:2px,color:#000,font-weight:bold
style F fill:#e1d8ff,stroke:#5e35b1,stroke-width:2px,color:#000,font-weight:bold
