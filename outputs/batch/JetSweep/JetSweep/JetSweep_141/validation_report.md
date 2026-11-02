# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_141`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_141/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 25 |
| Action Segments inferred | 86 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [13–20], lower_priority='Action_ZoneBlock' annotated_start=19, effective_Action_ZoneBlock_start=21.
> - Action 'Action_None' range [13-140] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-149] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-182] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-178] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-210] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [13-68] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-76] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-94] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-188] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-197] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [18-92] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-31] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-210] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [13-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-210] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [19-92] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [40-169] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [172-173] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_SealBlock' range [19-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [21-24] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [26-40] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [19-21] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [70-71] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-138] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [142-169] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-190] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [192-199] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [19-26] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [34-36] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-30] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-75] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [80-81] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-210] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [64-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-68] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-76] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-88] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-121] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-195] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [202-207] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [189-191] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-190] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-195] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-198] for track '32' has 1 frames without a visible bounding box.
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