# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_104`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_104/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 77 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '8' (C): higher_priority='Action_BallSnap' [40–55], lower_priority='Action_ZoneBlock' annotated_start=43, effective_Action_ZoneBlock_start=56.
> - Segment 'Action_BallCarry' for track '15' has invalid range: start=95, end=43. Clamping end to start.
> - Action 'Action_None' range [40-193] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-207] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-216] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-171] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-176] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-200] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-192] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-115] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [40-85] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-89] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-93] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [43-46] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [43-90] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-235] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [43-83] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [93-94] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-145] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-153] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [58-107] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [113-117] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [119-120] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-196] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [40-150] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-43] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-86] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-100] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-110] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-113] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-164] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-172] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-239] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-184] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-221] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [203-210] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-216] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-230] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [232-238] for track '31' has 2 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.