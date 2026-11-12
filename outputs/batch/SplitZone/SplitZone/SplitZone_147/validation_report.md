# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_147`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_147/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 96 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 629 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
> - Segment 'Action_BallCarry' for track '4' has invalid range: start=475, end=339. Clamping end to start.
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [455–464], lower_priority='Action_ZoneBlock' annotated_start=458, effective_Action_ZoneBlock_start=465.
> - Action 'Action_SplitBlock' range [457-523] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-339] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [455-629] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [455-517] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [535-554] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [562-564] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [566-629] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [455-524] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [455-499] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [455-486] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [491-629] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [458-492] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [495-534] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [535-623] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [455-470] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [475-484] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [487-516] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [475-624] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [455-528] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [535-537] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [540-551] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [554-591] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [458-493] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [511-518] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [455-603] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [458-479] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [455-464] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [465-475] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [482-490] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [493-494] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [496-497] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [499-514] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [458-464] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [469-470] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [472-474] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [455-610] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [480-501] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [505-514] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [516-629] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [483-486] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [496-500] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [503-531] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [533-565] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [500-506] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [508-509] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [519-520] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [523-531] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [522-524] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [546-548] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [553-555] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [563-564] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [566-572] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [589-628] for track '32' has 2 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.