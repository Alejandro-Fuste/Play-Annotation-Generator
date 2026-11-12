# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_28`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_28/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 82 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 509 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 509 as fallback play end.
> - Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [189–204], lower_priority='Action_ZoneBlock' annotated_start=192, effective_Action_ZoneBlock_start=205.
> - Action 'Action_None' range [189-273] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-367] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [189-280] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [192-277] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [237-287] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [192-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [224-232] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [234-242] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [192-231] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [238-242] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [245-253] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [260-279] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-288] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-289] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-293] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [192-279] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-301] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-248] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-291] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-446] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [448-450] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [467-470] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-236] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-295] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [237-266] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-244] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-417] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [419-425] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-306] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-394] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-330] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [368-373] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [406-416] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [421-423] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [425-427] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [429-439] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [441-456] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [440-441] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [444-462] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [485-491] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [494-508] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [442-443] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [445-446] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [447-450] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [456-460] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [478-480] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [485-487] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [495-497] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [501-507] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [453-454] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [486-497] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [501-509] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [495-505] for track '32' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [500-503] for track '34' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.