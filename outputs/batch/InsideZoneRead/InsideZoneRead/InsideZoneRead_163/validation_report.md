# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_163`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_163/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 74 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [29–43], lower_priority='Action_ZoneBlock' annotated_start=32, effective_Action_ZoneBlock_start=44.
> - Action 'Action_None' range [29-99] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-205] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [32-110] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-117] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-133] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [74-210] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [212-218] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [224-226] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-86] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-144] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-215] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-68] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-53] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-63] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-70] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-110] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-115] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-119] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-161] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-183] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-203] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-212] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [216-237] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [178-184] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-190] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-204] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-230] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-239] for track '31' has 1 frames without a visible bounding box.
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