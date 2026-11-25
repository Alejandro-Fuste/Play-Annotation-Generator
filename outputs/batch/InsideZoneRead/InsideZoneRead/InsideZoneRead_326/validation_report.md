# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_326`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_326/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 88 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 651: Duplicate assignment for track ID '19' in grid. Overwriting previous assignment.
> - Row 651: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_ZoneBlock' for track '12' has invalid range: start=29, end=25. Clamping end to start.
> - Segment 'Action_ZoneBlock' for track '18' has invalid range: start=29, end=18. Clamping end to start.
> - Segment 'Action_BallSnap' for track '22' has invalid range: start=44, end=37. Clamping end to start.
> - Action 'Action_None' range [26-58] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-148] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-179] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-79] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-159] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-46] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-49] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-100] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-131] for track '3' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [26-180] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-179] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-53] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-67] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [26-58] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [26-95] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-109] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [111-112] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-150] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-18] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-56] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-73] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-113] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-56] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-113] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-142] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' for track '12' starts at frame 63, but the player has no visible bounding box on this frame.
> - Action 'Action_BallCarry' range [63-63] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [80-91] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [102-123] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [26-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-37] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [39-180] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [26-33] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-48] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [26-53] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-131] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [29-80] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [94-121] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-13] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-18] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-7] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-42] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-57] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-79] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-129] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [44-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '22' starts at frame 45, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [45-45] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-60] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-65] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-80] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-75] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-80] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-91] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-111] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-84] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-116] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [61-179] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [66-67] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-82] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-179] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [88-95] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-167] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-113] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [115-119] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-116] for track '32' has 1 frames without a visible bounding box.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_326'; source metadata written as null.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.