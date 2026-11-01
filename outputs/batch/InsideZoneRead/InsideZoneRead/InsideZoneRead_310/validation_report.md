# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_310`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_310/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 37 |
| Player Tracks | 37 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 89 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_BallCarry' for track '8' has invalid range: start=59, end=58. Clamping end to start.
> - Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [13–28], lower_priority='Action_ZoneBlock' annotated_start=16, effective_Action_ZoneBlock_start=29.
> - Action 'Action_None' range [13-95] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-101] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-78] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-108] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-96] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-210] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [13-105] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-114] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-44] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-94] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [96-210] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [13-129] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_Keep' range [36-58] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [29-33] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [39-40] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [66-68] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '9' starts at frame 92, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [92-92] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-96] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [16-77] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-58] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [65-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [16-31] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-12] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-64] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [69-85] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-12] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-34] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-75] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-106] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-210] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [65-179] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-208] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-181] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [81-97] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-102] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-129] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-119] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-124] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-178] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [181-200] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [207-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-210] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [122-123] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-153] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-159] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-177] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [155-158] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-175] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-162] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [157-158] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-185] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-191] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-193] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-210] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-193] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-197] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-210] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [208-210] for track '36' has 1 frames without a visible bounding box.
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
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.