# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_52`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_52/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 75 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Resolved action overlap for track '3' (C): higher_priority='Action_BallSnap' [115–131], lower_priority='Action_ZoneBlock' annotated_start=118, effective_Action_ZoneBlock_start=132.
> - Action 'Action_None' range [155-192] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-191] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [118-168] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [171-195] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-152] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-209] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-152] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [157-182] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [189-219] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [115-167] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-299] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [118-144] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [147-155] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [115-168] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-180] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [189-209] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-299] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [157-176] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [178-179] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [183-206] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-246] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-253] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [115-185] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-193] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [118-201] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-130] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-185] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [187-188] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-191] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-223] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-130] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-203] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [212-213] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-250] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-252] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-265] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-261] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-289] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-279] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-282] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-283] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-288] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-299] for track '25' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.