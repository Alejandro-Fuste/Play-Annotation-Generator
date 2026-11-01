# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_32`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_32/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 24 |
| Player Tracks | 24 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 81 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 66: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '4' (RG) duration 93 frames exceeds threshold 90 frames [start=66, end=158].
> - Validation warning: Action 'Action_ZoneBlock' for track '9' (RT) duration 93 frames exceeds threshold 90 frames [start=66, end=158].
> - Validation warning: Action 'Action_ZoneBlock' for track '10' (C) duration 93 frames exceeds threshold 90 frames [start=66, end=158].
> - Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [64–78], lower_priority='Action_ZoneBlock' annotated_start=66, effective_Action_ZoneBlock_start=79.
> - Validation warning: Action 'Action_ZoneBlock' for track '11' (LT) duration 93 frames exceeds threshold 90 frames [start=66, end=158].
> - Action 'Action_Handoff' range [98-106] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [108-110] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-114] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-136] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-235] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-238] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-163] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-228] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-234] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [66-126] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-178] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-181] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-140] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-151] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [112-176] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [93-158] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [159-239] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [64-78] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [90-91] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [93-99] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [107-108] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [114-131] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-186] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-206] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [208-209] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-224] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [66-114] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [116-129] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [133-135] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [137-138] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-105] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-116] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-127] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-147] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-82] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-89] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-101] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-196] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-122] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-159] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-161] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-239] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-207] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-228] for track '22' has 1 frames without a visible bounding box.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.