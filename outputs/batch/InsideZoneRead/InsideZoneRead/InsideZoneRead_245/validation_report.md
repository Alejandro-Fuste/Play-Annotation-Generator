# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_245`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_245/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 104 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 490: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [7–18], lower_priority='Action_ZoneBlock' annotated_start=10, effective_Action_ZoneBlock_start=19.
> - Action 'Action_None' range [7-153] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [158-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-159] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-167] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-136] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [146-159] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [162-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-36] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-180] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-122] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [133-134] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-180] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [7-64] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [87-180] for track '6' has 7 frames without a visible bounding box.
> - Action 'Action_None' range [7-81] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [95-116] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [133-134] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-79] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [10-42] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [44-82] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-102] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_Keep' for track '11' starts at frame 43, but the player has no visible bounding box on this frame.
> - Action 'Action_Keep' range [43-51] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [52-157] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [7-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [10-62] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [65-68] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-138] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [7-17] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [30-33] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-80] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-102] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [105-110] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [113-114] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-180] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-42] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-76] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-81] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-110] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-40] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [10-27] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-116] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-120] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-138] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-154] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-169] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [172-180] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [10-71] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [75-77] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-102] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [105-116] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [118-122] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [129-138] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [161-162] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-168] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-66] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-70] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-180] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-166] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [169-180] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [118-155] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [163-165] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-175] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-180] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-140] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [142-157] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-165] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-176] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-180] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-169] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-179] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [162-180] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [165-166] for track '29' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.