# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_174`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_174/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 100 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 348: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [48–62], lower_priority='Action_ZoneBlock' annotated_start=51, effective_Action_ZoneBlock_start=63.
> - Action 'Action_None' range [48-269] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-269] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [48-100] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-110] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-125] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-104] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [107-125] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-198] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-217] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-226] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-258] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [48-147] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-201] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [204-269] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [51-130] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-139] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-144] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-163] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-269] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-80] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-164] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-209] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [48-123] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [143-144] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-159] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-132] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [135-139] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [63-66] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [51-67] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' for track '14' starts at frame 80, but the player has no visible bounding box on this frame.
> - Action 'Action_BlockSecondLevel' range [80-134] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-164] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [94-216] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-220] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [51-74] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [68-77] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-159] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [168-194] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [197-221] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [51-67] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [74-78] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-223] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [226-269] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-193] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-269] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [156-159] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-176] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [178-179] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-183] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-225] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-175] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-203] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [174-198] for track '28' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [203-210] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-216] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-220] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-230] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [233-235] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-240] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-250] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-269] for track '29' has 1 frames without a visible bounding box.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
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