# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_311`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_311/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 108 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 622: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_BlockSecondLevel' for track '16' has invalid range: start=44, end=39. Clamping end to start.
> - Validation warning: Action 'Action_ZoneBlock' for track '17' (C) duration 94 frames exceeds threshold 90 frames [start=18, end=111].
> - Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [15–34], lower_priority='Action_ZoneBlock' annotated_start=18, effective_Action_ZoneBlock_start=35.
> - Validation warning: Action 'Action_ZoneBlock' for track '18' (LT) duration 94 frames exceeds threshold 90 frames [start=18, end=111].
> - Validation warning: Action 'Action_ZoneBlock' for track '20' (RG) duration 94 frames exceeds threshold 90 frames [start=18, end=111].
> - Action 'Action_None' range [15-39] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-46] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-137] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [15-41] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-49] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-55] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-69] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-82] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [15-113] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-126] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-184] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [187-239] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-139] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-151] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-239] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [15-148] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-151] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-212] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-239] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [15-137] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-158] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-213] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-74] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-143] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [15-91] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-239] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [15-42] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-93] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [101-156] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [15-239] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [39-43] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_Keep' range [46-56] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [70-84] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [91-227] for track '15' has 5 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [18-39] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [15-25] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [35-89] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-227] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [18-39] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [56-61] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [63-80] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [18-30] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [18-27] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [30-35] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [37-48] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [51-84] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [88-92] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [96-111] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-131] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-82] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-131] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [133-135] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-144] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [152-154] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-189] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [191-206] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [208-217] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [221-223] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-229] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-233] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-237] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-99] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-169] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [173-182] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-234] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-239] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-223] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [227-233] for track '26' has 2 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.