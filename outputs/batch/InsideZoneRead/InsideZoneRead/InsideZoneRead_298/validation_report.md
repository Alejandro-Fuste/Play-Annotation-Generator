# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_298`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_298/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 89 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 596: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [11–26], lower_priority='Action_ZoneBlock' annotated_start=14, effective_Action_ZoneBlock_start=27.
> - Action 'Action_None' range [11-210] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [11-130] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [14-40] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [46-71] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-115] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-120] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-86] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [89-165] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-93] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-104] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_Keep' range [38-63] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [64-198] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [202-203] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [207-209] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-111] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-131] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [135-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-87] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [14-51] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-60] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [70-84] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-32] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-98] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [14-82] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [95-142] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [11-24] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [29-32] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [39-41] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-7] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-67] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [70-74] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [79-83] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [90-100] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [109-116] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-120] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-172] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-44] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [47-49] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-59] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-187] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [189-192] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-210] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [89-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-164] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-162] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [164-172] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-178] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-162] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-210] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-210] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-210] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-181] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-205] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-210] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-178] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-210] for track '33' has 1 frames without a visible bounding box.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.