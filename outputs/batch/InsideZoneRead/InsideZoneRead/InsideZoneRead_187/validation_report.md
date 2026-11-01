# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_187`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_187/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 24 |
| Player Tracks | 24 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 84 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 479 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
> - Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [326–335], lower_priority='Action_ZoneBlock' annotated_start=328, effective_Action_ZoneBlock_start=336.
> - Action 'Action_ZoneBlock' range [328-367] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-362] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [368-448] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [450-452] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [328-371] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [394-448] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-425] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-343] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [352-390] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [392-479] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-132] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-142] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-146] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-153] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-384] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [418-431] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [436-437] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [394-464] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-394] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [326-422] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [426-438] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [440-448] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [450-458] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [460-461] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-133] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-325] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-374] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-334] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [383-479] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-126] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-130] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-343] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [351-399] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [394-471] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-92] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [356-359] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [368-376] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [383-385] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [409-429] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [432-446] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [450-468] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [417-421] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [418-426] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [431-466] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [470-479] for track '23' has 1 frames without a visible bounding box.
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