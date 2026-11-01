# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_368`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_368/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 35 |
| Ball Tracks | 1 |
| CSV events parsed | 19 |
| Action Segments inferred | 96 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '8' (C): higher_priority='Action_BallSnap' [21–37], lower_priority='Action_ZoneBlock' annotated_start=24, effective_Action_ZoneBlock_start=38.
> - Action 'Action_None' range [21-135] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-47] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-120] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-269] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [24-59] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [85-86] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-135] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-47] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-64] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [68-75] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-90] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-96] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-75] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-269] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [21-93] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [38-56] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [98-153] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [24-39] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [47-49] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [51-91] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-149] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-85] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [88-93] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_Keep' range [46-65] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [69-82] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [87-91] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [98-133] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [21-46] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-59] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-74] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-82] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-129] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-134] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-137] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [24-70] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-122] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-141] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-41] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-75] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-122] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-85] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-122] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-140] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-267] for track '20' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [101-106] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-175] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-190] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-128] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [110-122] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-128] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-137] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [139-269] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-134] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-269] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-149] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-177] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-189] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-197] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [186-189] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [206-269] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-269] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-250] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-259] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-262] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-269] for track '35' has 1 frames without a visible bounding box.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
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