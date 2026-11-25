# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_254`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_254/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 75 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 508: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - Row 508: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '6' (RG) duration 93 frames exceeds threshold 90 frames [start=21, end=113].
> - Validation warning: Action 'Action_ZoneBlock' for track '9' (RT) duration 93 frames exceeds threshold 90 frames [start=21, end=113].
> - Validation warning: Action 'Action_ZoneBlock' for track '14' (C) duration 93 frames exceeds threshold 90 frames [start=21, end=113].
> - Segment 'Action_ZoneBlock' for track '15' has invalid range: start=21, end=17. Clamping end to start.
> - Segment 'Action_BallSnap' for track '21' has invalid range: start=62, end=33. Clamping end to start.
> - Action 'Action_None' range [18-128] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-106] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-48] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [52-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-45] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-210] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [18-122] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-95] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-178] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-210] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [18-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-43] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-80] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-86] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [21-63] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [67-69] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [72-78] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [84-93] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [95-113] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-156] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-168] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-210] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [18-195] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [18-69] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-161] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [21-79] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [21-67] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_SnapReceive' range [18-33] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_Keep' range [49-65] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [66-200] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-22] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-27] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-37] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [18-26] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [21-113] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-199] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-67] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-191] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-156] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-139] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-186] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [176-207] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [181-200] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-210] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-210] for track '29' has 1 frames without a visible bounding box.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
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
> - Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_254'; source metadata written as null.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.