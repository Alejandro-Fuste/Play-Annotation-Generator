# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_19`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_19/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 101 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 479 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '6' (LT) duration 100 frames exceeds threshold 90 frames [start=255, end=354].
> - Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [253–265], lower_priority='Action_ZoneBlock' annotated_start=255, effective_Action_ZoneBlock_start=266.
> - Validation warning: Action 'Action_ZoneBlock' for track '19' (LG) duration 106 frames exceeds threshold 90 frames [start=255, end=360].
> - Validation warning: Action 'Action_ZoneBlock' for track '20' (RT) duration 106 frames exceeds threshold 90 frames [start=255, end=360].
> - Validation warning: Action 'Action_ZoneBlock' for track '21' (RG) duration 106 frames exceeds threshold 90 frames [start=255, end=360].
> - Action 'Action_None' range [253-295] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-477] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [290-384] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-445] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [454-457] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [255-303] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [315-354] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [253-440] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [445-451] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [453-454] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-386] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-295] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-379] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [386-404] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [406-407] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [415-417] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-479] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-281] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-288] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-311] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [268-280] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-453] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [253-366] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [380-386] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [392-397] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [399-404] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-354] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [358-362] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [367-373] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [375-464] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-355] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [382-429] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [253-265] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [290-325] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [354-355] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [255-343] for track '19' has 4 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [347-357] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '19' starts at frame 361, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [361-361] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [368-369] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [255-267] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [271-295] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [302-360] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [361-448] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-68] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-71] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-254] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [255-278] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [282-360] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [361-449] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-320] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-323] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [340-347] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [350-463] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [383-430] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [383-418] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [388-402] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [404-457] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [389-390] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [455-471] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [457-463] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [461-462] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [466-468] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [473-475] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [477-479] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [472-473] for track '34' has 1 frames without a visible bounding box.
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