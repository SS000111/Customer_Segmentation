/cloud_segmentation_app             <-- ROOT FOLDER
    ├── app.py                      <-- The Server (Phase 3)
    ├── train_hybridmodel.py        <-- The Trainer (Phase 2)
    ├── Procfile                    <-- Cloud Config (Phase 1)
    ├── requirements.txt            <-- Cloud Config (Phase 1)
    ├── artifacts/
    │   └── hybrid_model.pkl        <-- The Brain
    └── templates/                  <-- Interface folder (Phase 4)
        └── index.html              <-- User Interface 