# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_364`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_364/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 78 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [26–40], lower_priority='Action_ZoneBlock' annotated_start=29, effective_Action_ZoneBlock_start=41.
> - Action 'Action_None' range [26-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-156] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-159] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-163] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-207] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [26-186] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-102] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-177] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-71] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-76] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-182] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [26-135] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [29-69] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [79-80] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-130] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-139] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [29-75] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [79-93] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [99-106] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [26-206] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-25] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-29] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-32] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-73] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-177] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-181] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-193] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-202] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-86] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-90] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-97] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-143] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-149] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-153] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-169] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-169] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-210] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-210] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-210] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-210] for track '30' has 1 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.