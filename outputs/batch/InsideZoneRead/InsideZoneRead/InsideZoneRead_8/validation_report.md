# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_8`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_8/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 23 |
| Player Tracks | 23 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 63 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [85–96], lower_priority='Action_ZoneBlock' annotated_start=89, effective_Action_ZoneBlock_start=97.
> - Action 'Action_None' range [85-203] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [251-257] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [168-314] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-111] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-222] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [89-158] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-119] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [128-185] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [188-346] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-311] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-185] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-331] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-183] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [97-133] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [137-143] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-317] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [85-183] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-153] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [162-326] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [85-100] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-105] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-112] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-359] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-153] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-159] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-186] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-332] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [159-359] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-182] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-182] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-273] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-293] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-292] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [220-301] for track '21' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.