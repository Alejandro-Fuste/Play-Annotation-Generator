# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_37`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_37/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 97 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '16' (RT) duration 95 frames exceeds threshold 90 frames [start=61, end=155].
> - Validation warning: Action 'Action_ZoneBlock' for track '18' (C) duration 95 frames exceeds threshold 90 frames [start=61, end=155].
> - Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [58–72], lower_priority='Action_ZoneBlock' annotated_start=61, effective_Action_ZoneBlock_start=73.
> - Validation warning: Action 'Action_ZoneBlock' for track '19' (LT) duration 95 frames exceeds threshold 90 frames [start=61, end=155].
> - Segment 'Action_BallCarry' for track '20' has invalid range: start=105, end=78. Clamping end to start.
> - Action 'Action_None' range [58-179] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-188] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [194-208] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-215] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-235] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-150] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [58-181] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-238] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-135] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-168] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-181] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [184-206] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-239] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-154] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-167] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-171] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-95] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [97-167] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-212] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-91] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-239] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [63-101] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [105-155] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [156-178] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-181] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-95] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-101] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-105] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-115] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [118-169] for track '15' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [174-181] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-224] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-182] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-221] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [61-82] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [73-93] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [123-127] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [129-141] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [61-103] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-220] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-78] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-68] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [148-151] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [167-168] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-119] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-124] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-161] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-171] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [184-193] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-202] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-205] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-172] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-226] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-173] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [178-179] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-206] for track '27' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.