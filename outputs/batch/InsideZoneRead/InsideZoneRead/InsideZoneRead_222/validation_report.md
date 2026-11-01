# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_222`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_222/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 77 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 444: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '2' (LT) duration 95 frames exceeds threshold 90 frames [start=68, end=162].
> - Segment 'Action_BlockSecondLevel' for track '9' has invalid range: start=115, end=108. Clamping end to start.
> - Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [65–82], lower_priority='Action_ZoneBlock' annotated_start=68, effective_Action_ZoneBlock_start=83.
> - Validation warning: Action 'Action_ZoneBlock' for track '20' (RG) duration 95 frames exceeds threshold 90 frames [start=68, end=162].
> - Validation warning: Action 'Action_ZoneBlock' for track '21' (RT) duration 95 frames exceeds threshold 90 frames [start=68, end=162].
> - Action 'Action_None' range [65-229] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-233] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-211] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-171] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-209] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-267] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [65-244] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-157] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [83-108] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-30] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-122] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [68-148] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [110-154] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [68-99] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [102-106] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [108-157] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [68-96] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-165] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-133] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [129-159] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-141] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-167] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-167] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-170] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-202] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-250] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-269] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-266] for track '31' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.