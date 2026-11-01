# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_188`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_188/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 45 |
| Player Tracks | 45 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 145 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 375: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [4–18], lower_priority='Action_ZoneBlock' annotated_start=6, effective_Action_ZoneBlock_start=19.
> - Segment 'Action_BallCarry' for track '20' has invalid range: start=47, end=24. Clamping end to start.
> - Segment 'Action_BlockSecondLevel' for track '21' has invalid range: start=24, end=15. Clamping end to start.
> - Action 'Action_None' range [4-199] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-47] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-106] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-118] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-127] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-146] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-156] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-199] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-180] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-199] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-11] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-11] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-68] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-95] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-118] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-123] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-136] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-140] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-155] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-162] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-130] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-156] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-38] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-56] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [4-11] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-16] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-131] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [133-139] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [145-149] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-22] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [25-33] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [36-37] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-41] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-184] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-11] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [6-11] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [74-75] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-119] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-126] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-156] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-196] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [6-11] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-89] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-101] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [38-42] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-105] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-113] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-119] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-126] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-199] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [6-11] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [4-11] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [16-18] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' for track '19' starts at frame 19, but the player has no visible bounding box on this frame.
> - Action 'Action_ZoneBlock' range [19-19] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-24] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [6-11] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [14-15] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-33] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [35-48] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-111] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-51] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-52] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-57] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-62] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-56] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-59] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-103] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [109-190] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-196] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-77] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-90] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-98] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-109] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-119] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-127] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-166] for track '26' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [169-199] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [77-78] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-126] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-91] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-90] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-175] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [179-180] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-120] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-199] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-127] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-132] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-141] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-199] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-127] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-156] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-162] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-166] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-185] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [194-195] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-199] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-127] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-160] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [169-176] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-127] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-126] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-125] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-166] for track '38' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [169-172] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-180] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-185] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [194-195] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-187] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [190-191] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-196] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-185] for track '40' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [187-191] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-199] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-192] for track '41' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [194-196] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-191] for track '42' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [193-196] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-197] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-199] for track '44' has 1 frames without a visible bounding box.
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
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.
> - Player track '42' has undefined position. Will map to Position_Unknown.
> - Player track '42' has undefined team_side. Will map to Team_Unknown.
> - Player track '43' has undefined position. Will map to Position_Unknown.
> - Player track '43' has undefined team_side. Will map to Team_Unknown.
> - Player track '44' has undefined position. Will map to Position_Unknown.
> - Player track '44' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.