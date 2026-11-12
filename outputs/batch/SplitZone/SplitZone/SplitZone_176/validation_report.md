# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_176`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_176/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 97 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [129–138], lower_priority='Action_ZoneBlock' annotated_start=132, effective_Action_ZoneBlock_start=139.
> - Action 'Action_None' range [129-206] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [226-291] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-199] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-254] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [163-170] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [132-200] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [129-139] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-177] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-251] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [254-261] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [263-290] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-299] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [132-173] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [176-204] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-264] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [132-183] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [221-257] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [259-325] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [221-261] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-202] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-226] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-49] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-154] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [138-170] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [172-189] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [221-245] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-273] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-21] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-28] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-36] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-138] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [139-145] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [148-165] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-310] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [314-315] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-136] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-171] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-17] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-22] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-25] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [42-67] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-155] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [161-163] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-174] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-316] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-171] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [137-138] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-159] for track '20' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [172-248] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-300] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-184] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-203] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [205-209] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-258] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-217] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-241] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-255] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-259] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-262] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-220] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-264] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [219-255] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-290] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-297] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [268-310] for track '27' has 1 frames without a visible bounding box.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.