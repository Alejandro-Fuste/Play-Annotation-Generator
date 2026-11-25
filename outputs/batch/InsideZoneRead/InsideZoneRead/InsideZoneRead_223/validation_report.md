# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_223`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_223/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 89 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 445: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - Row 446: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Segment 'Action_BallCarry' for track '16' has invalid range: start=152, end=145. Clamping end to start.
> - Segment 'Action_SnapReceive' for track '17' has invalid range: start=148, end=132. Clamping end to start.
> - Segment 'Action_ReadDefender' for track '17' has invalid range: start=148, end=141. Clamping end to start.
> - Segment 'Action_BallSnap' for track '18' has invalid range: start=150, end=132. Clamping end to start.
> - Action 'Action_None' range [113-129] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-138] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [206-207] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [116-198] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-179] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '3' starts at frame 113, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [113-113] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-203] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [202-205] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [116-170] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-138] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [145-273] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-50] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-63] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-190] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-206] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-104] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-107] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-118] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [128-222] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-143] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-149] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-58] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-69] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-81] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-88] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '11' starts at frame 113, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [113-113] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-118] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-121] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-299] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-129] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [116-151] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [157-192] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [113-259] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-139] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-145] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-177] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '18' starts at frame 151, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [151-151] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-172] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [160-161] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-284] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [170-171] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-212] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-208] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-220] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-235] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [181-259] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [262-275] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [277-279] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-299] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-193] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-214] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [202-233] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [237-238] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-240] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [255-256] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-260] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-264] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-268] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-272] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-296] for track '31' has 1 frames without a visible bounding box.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_223'; source metadata written as null.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.