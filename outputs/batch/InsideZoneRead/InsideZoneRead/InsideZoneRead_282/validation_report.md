# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_282`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_282/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 93 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 564: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [3–17], lower_priority='Action_ZoneBlock' annotated_start=6, effective_Action_ZoneBlock_start=18.
> - Action 'Action_None' range [3-210] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [3-84] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-84] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [89-91] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-124] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-110] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [3-108] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-112] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-120] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-199] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-102] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' for track '7' starts at frame 85, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [85-85] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-118] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-210] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_Keep' range [32-48] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [55-60] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [66-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [6-49] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [3-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-50] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [3-148] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [6-26] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-53] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [62-76] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [79-84] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-90] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [18-39] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [3-53] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [56-85] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-48] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [53-61] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-76] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-159] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [36-106] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-46] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-176] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-190] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-199] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-59] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-70] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-108] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-173] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-198] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-142] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [89-169] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [115-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-210] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-134] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-176] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-197] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [205-208] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-140] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-144] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-146] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-152] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-210] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-192] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-209] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-195] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-197] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-199] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-210] for track '35' has 1 frames without a visible bounding box.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.