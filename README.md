flowchart LR

%% ===========================
%%      SUBGRAPH: DATA PIPELINE
%% ===========================
subgraph DP[📡 DATA PIPELINE]
direction LR

A([🔧 Sensor <br> Data Collection]) 
B([🗄️ Database <br> Storage])
C([📥 Fetch Latest <br> Sensor Data])

A --> B --> C
end

%% ===========================
%%      SUBGRAPH: AI ENGINE
%% ===========================
subgraph AI[🤖 AI ENGINE]
direction LR

D([🧠 AI/ML Model <br> Inference])
E([⏳ RUL Prediction <br> (Remaining Useful Life)])

C --> D --> E
end

%% ===========================
%%      SUBGRAPH: DASHBOARD
%% ===========================
subgraph UI[🖥️ USER INTERFACE]
direction LR

F([📊 Local Web Dashboard <br> Real-Time Status])
end

E --> F

%% ===========================
%%        STYLES
%% ===========================
style DP fill:#fef6d3,stroke:#d4a017,stroke-width:2px,rx:10,ry:10
style AI fill:#fde7f2,stroke:#b3125b,stroke-width:2px,rx:10,ry:10
style UI fill:#e8e3ff,stroke:#5e35b1,stroke-width:2px,rx:10,ry:10

style A fill:#fff2cc,stroke:#c99700,stroke-width:2px,color:#000,font-weight:bold
style B fill:#d6efff,stroke:#0288d1,stroke-width:2px,color:#000,font-weight:bold
style C fill:#d6ffd8,stroke:#2e7d32,stroke-width:2px,color:#000,font-weight:bold

style D fill:#ffd9ec,stroke:#c2185b,stroke-width:2px,color:#000,font-weight:bold
style E fill:#ffef9e,stroke:#ffb300,stroke-width:2px,color:#000,font-weight:bold

style F fill:#e2d9ff,stroke:#5e35b1,stroke-width:2px,color:#000,font-weight:bold
