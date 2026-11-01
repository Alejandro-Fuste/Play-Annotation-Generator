# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_15`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_15/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 83 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [128–139], lower_priority='Action_ZoneBlock' annotated_start=130, effective_Action_ZoneBlock_start=140.
> - Action 'Action_None' range [128-177] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-269] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [130-151] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-266] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-222] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [226-254] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [256-269] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-153] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [163-191] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [194-226] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [228-269] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-174] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-269] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-269] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [130-158] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [160-183] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-224] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-268] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-187] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-197] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' for track '19' starts at frame 140, but the player has no visible bounding box on this frame.
> - Action 'Action_ZoneBlock' range [140-140] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [142-144] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [168-169] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [172-184] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [186-198] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [130-180] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [183-185] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-213] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-254] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [130-160] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-72] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-206] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-230] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-222] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-234] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-243] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-247] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-250] for track '28' has 1 frames without a visible bounding box.
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