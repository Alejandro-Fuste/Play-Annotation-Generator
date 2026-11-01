# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_360`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_360/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 85 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [24–38], lower_priority='Action_ZoneBlock' annotated_start=27, effective_Action_ZoneBlock_start=39.
> - Action 'Action_None' range [24-106] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-81] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [86-90] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [92-239] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-183] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [24-192] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-234] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [27-94] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-123] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-239] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [27-43] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [45-60] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [67-69] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [73-84] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-116] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [27-61] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [63-82] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [93-94] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [100-101] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-209] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [24-57] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [62-78] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-66] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-146] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-239] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [39-102] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-198] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [27-47] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [49-86] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-123] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-238] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [24-40] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-45] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_SnapReceive' range [24-28] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_SnapReceive' range [31-33] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_Keep' range [50-59] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_Keep' range [61-71] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [72-94] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-32] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-78] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-140] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-47] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-55] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-78] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-160] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-170] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-107] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-214] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [218-223] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-232] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-201] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [205-239] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [170-235] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [178-189] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-196] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-205] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [225-239] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-226] for track '27' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.